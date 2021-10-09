# ESPEI datasets

Datasets to be used with ESPEI.

## Using the data

See [espei.org](https://espei.org) for an example of using these datasets with ESPEI to automatically generate and fit CALPHAD models with pycalphad.

## Steps to contribute new datasets

Anyone is invited to use and contribute to this repository. Unsolicited contributions are welcome!

By contributing your data to this repository, you agree to license that data as [Creative Commons Attribution 4.0 (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/).

1. Clone this repository and start working in a new branch
#. Organize each dataset in to a folder for that system (see the Organization structure section below)
#. For each dataset, ensure that there is a BibTeX citation key in the `"bibtex"` key and your name in the `"author"` key.
#. Add the BibTeX entries corresponding to the added datasets to the `references.bib` file, making sure there are no conflicts in the chosen key name.
#. Commit your work, push to your fork and open a Pull Request.

## Organization structure

The organization structure is _for humans_.
When ESPEI loads datasets from a directory, all of the datasets are flattened and read at the same level.

`datasets/<number components>/<elements (alphabetically sorted)>/<data type>/<optional data type specific organization>/<JSON files>`

### Examples:

- `datasets/1-unary/Al/non-equilibrium-thermochemical/HM/<JSON files>`
- `datasets/2-binary/Al-Ni/zpf/<JSON files>`
- `datasets/2-binary/Al-Ni/equilibrium-thermochemical/SM/<JSON files>`
