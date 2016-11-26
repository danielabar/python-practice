# Practice Python

> Practice [exercises](http://www.practicepython.org/)

To reload modules interactively in python shell:

```python
>>> import importlib
>>> import my_module
>>> # make some changes to my_module source...
>>> importlib.reload(tic_tac_toe)
```

Linting with Atom, PEP8, and pyenv:

* At terminal, run `pip install pep8`
* Install linter-pep8 plugin for Atom
* At terminal run `pyenv which pep8`
* Update linger-pep8 settings in Atom, set pep8 executable path to result from previous command

## Tic Tac Toe

[Problem](http://www.practicepython.org/exercise/2016/08/03/28-tic-tac-toe-game.html) | [Solution](tic_tac_toe.py)

### Run Tests

```shell
python tic_tac_toe_test.py -v
```

[Pick Word](http://www.practicepython.org/exercise/2016/09/24/30-pick-word.html)
