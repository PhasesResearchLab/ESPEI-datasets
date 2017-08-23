# ESPEI datasets

Datasets to be used with ESPEI

## Using the data

See the [Cu-Mg example](http://espei.org/en/latest/cu-mg-example.html) on [espei.org](http://espei.org) for an example of using these datasets with ESPEI to automatically generate and fit CALPHAD models with pycalphad.
The data here is Creative Commons Attribution 4.0 (CC-BY-4.0) licensed.

## Contributing

Unsolicted pull requests are welcome!
* Please include your references in the references.bib file and make sure your datasets are labelled with references where applicable.
* Datasets should go in the folder of the subsystem they belong to. Split up the data (even from the same reference) into binary, ternary, etc. subsystem folders.
* Add yourself to the contributors with your email and any systems you have contributed to, e.g. `Brandon Bocklund; bocklund@psu.edu; CU-MG, CU-MG-NI`

It is also suggested that you run `check_script.py` file before commiting (requires ESPEI installed).
This way every commit will have a fully checked and working database.
Even better would be to set up a [pre-commit hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) in git with the following command:

``` bash
test -x "$(command -v espei)" && echo 'Checking datasets' && python check_script.py
```
