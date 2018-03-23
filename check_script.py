"""
Check all of the datasets.
Print errors of failed files and the error.
Return exit code 1 if there was 1 or more errors.
"""

import argparse
import os, shutil
from espei.datasets import recursive_glob, load_datasets, DatasetError

class DatasetFileNameError(Exception):
    """Exception raised when dataset file names are invalid."""
    pass


def suggest_filename(dataset, include_extension=False, upper_case_elements=True):
    """
    Check that file names match requirements.

    Must be the raw filename without any extra paths parts.

    Parameters
    ----------
    dataset : espei.PickleableTinyDB
        TinyDB of the dataset
    include_extension : bool
        Whether to include the filename extension ('.json') in the final string
    upper_case_elements : bool
        Whether to force the elements to be all caps (True) or regular case capitialized.

    Returns
    -------
    str
        String of the suggested file name.

    Notes
    -----
    An exmaple filename would be:

    ``AL-CO-ZPF-BCC_A2-FCC_A1-ishikawa1998phase.json``

    The elements and phase names should be sorted.
    Everything should be caps (as in the dataset, but we don't check that here) except the reference should be exactly the same case.
    """
    ds = dataset.all()[0]  # there should only be one entry in the dataset
    if upper_case_elements:
        elements = '-'.join(sorted(set(ds['components'])-set(['VA']))).upper()
    else:
        elements = '-'.join(sorted([el.lower().capitalize() for el in set(ds['components']) - set(['VA'])]))
    output = ds['output'].upper()
    phases = '-'.join(sorted(ds['phases'])).upper()
    refkey = ds['reference']

    return '-'.join([elements, output, phases, refkey])


def _move_no_overwrite(src, dst):
    """Move a file if the destination does not exist. If successful return false."""
    if not os.path.exists(dst):
        shutil.move(src, dst)
        return True
    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check datasets at the chosen paths.')
    parser.add_argument('paths', metavar='PATH', type=str, nargs='*', default=['.'], help='Path(s) to search')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    checked_files = 0
    errors = []
    for path in args.paths:
        dataset_filenames = sorted(recursive_glob(path, '*.json'))
        for dataset in dataset_filenames:
            d = None
            # lint the dataset
            try:
                d = load_datasets([dataset])
            except KeyError as e:
                # this is likely from an input.json
                pass
            except (ValueError, DatasetError) as e:
                errors.append(e)
            finally:
                checked_files += 1

    if len(errors) > 0:
        print(*errors, sep='\n')
        exit(1)
    else:
        print('Successfully checked {} datasets for errors'.format(checked_files))
        # We do this here because we don't want to generate any commits for moved files if there are errors. Linted files should be the last step.
        print('Checking if files need to be moved...')
        for dataset in dataset_filenames:
            # move the successfully checked files to their nice renamed state
            suggested_filename = suggest_filename(d, upper_case_elements=True)
            # remove the extra path parts and the extension
            filename_no_ext = os.path.splitext(os.path.basename(dataset))[0]
            # check that they're the same, we can accept arbitrary differentiating endings
            n_moved_files = 0
            if not filename_no_ext.startswith(suggested_filename):
                # try to move the file to the proper name
                new_path = os.path.join(os.path.dirname(dataset), suggested_filename)
                ext = '.json'
                unique_ext = '' + ext  # some unique string to differentiate the filename from others.
                i = 0
                while not _move_no_overwrite(dataset, new_path + unique_ext):
                    unique_ext = '-{}{}'.format(i, ext)
                    i += 1
                print('Moved {} to {}'.format(dataset, new_path + unique_ext))
                n_moved_files += 1
        if n_moved_files:
            print('Moved {} files.'.format(n_moved_files))
        else:
            print('No files to be moved.')
        exit(0)
