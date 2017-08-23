"""
Check all of the datasets.
Print errors of failed files and the error.
Return exit code 1 if there was 1 or more errors.
"""

import argparse
from espei.datasets import recursive_glob, load_datasets, DatasetError

parser = argparse.ArgumentParser(description='Check datasets at the chosen paths.')
parser.add_argument('paths', metavar='PATH', type=str, nargs='*',
                   default=['.'], help='Path(s) to search')
args = parser.parse_args()

checked_files = 0
errors = []
for path in args.paths:
    dataset_filenames = sorted(recursive_glob(path, '*.json'))
    for dataset in dataset_filenames:
       try:
           load_datasets([dataset])
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
    print('Successfully checked {} files'.format(checked_files))
    exit(0)
