# ESPEI datasets

Datasets to be used with ESPEI

## Using the data

See the [Cu-Mg example](http://espei.org/en/latest/cu-mg-example.html) on [espei.org](http://espei.org) for an example of using these datasets with ESPEI to automatically generate and fit CALPHAD models with pycalphad.
The data here is Creative Commons Attribution 4.0 (CC-BY-4.0) licensed.

## Contributing Checklist

1. Organize each dataset in to a folder for that system (e.g. `CU-MG`) and a sub-folder called `input-data`
2. Make sure each dataset has a BibTeX citation key in the "reference" field. 
	* To get this from Mendeley right click an entry and do "Copy As" -> "BIbTeX Entry"
	* The the first piece of information in that text is the citation key. Your Mendeley entry should have a new field for Citation Key as well for you to customize it for next time you copy.
	* Mendeley defaults to LastnameYEAR format, but I suggest something like LastnameYEARfirst_unique_title_words (with words separated by underscores). This ensures that the key is unique
3. Make sure each dataset is named consistently. I suggest doing the `Components-DATATYPE-PHASE_NAMES-citation_key.json` e.g. `AL-Co-ZPF-BCC_A2-FCC_A1-ishikawa1998phase.json`
4. Add the BibTeX Entry to `references.bib` and make sure there are no conflicts in the citation key. 
5. Add yourself to the contributors with your email and any systems you have contributed to, e.g. `Brandon Bocklund; bocklund@psu.edu; CU-MG, CU-MG-NI`

It is also suggested that you run `check_script.py` file before commiting (requires ESPEI installed).
This way every commit will have a fully checked and working database.
Even better would be to set up a [pre-commit hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) in git with the following command:

``` bash
test -x "$(command -v espei)" && echo 'Checking datasets' && python check_script.py
```
