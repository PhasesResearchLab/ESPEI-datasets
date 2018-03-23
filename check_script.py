"""
Check all of the datasets.
Print errors of failed files and the error.
Return exit code 1 if there was 1 or more errors.
"""

import argparse
import os
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

            try:
                # lint the filename
                if d is not None:
                    suggested_filename = suggest_filename(d, upper_case_elements=False)
                    # remove the extra path parts and the extension
                    filename_no_ext = os.path.splitext(os.path.basename(dataset))[0]
                    # check that they're the same, we can accept arbitrary differentiating endings
                    if not filename_no_ext.startswith(suggested_filename):
                        raise DatasetFileNameError('File name for dataset {} does not match the suggested file name of {}.'.format(dataset, suggested_filename))
            except DatasetFileNameError as e:
                errors.append(e)

    if len(errors) > 0:
        print(*errors, sep='\n')
        exit(1)
    else:
        print('Successfully checked {} files'.format(checked_files))
        exit(0)
