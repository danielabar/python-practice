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
* Update linter-pep8 settings in Atom, set pep8 executable path to result from previous command

## Exercises

[Tick tac toe](http://www.practicepython.org/exercise/2016/08/03/28-tic-tac-toe-game.html) | [Solution](solutions/tic_tac_toe.py)

```shell
python tic_tac_toe_test.py -v
```

[Pick Word](http://www.practicepython.org/exercise/2016/09/24/30-pick-word.html) | [Solution](solutions/pick_word.py)

[Guessing Game Two](http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html) | [Solution](solutions/guess_game_2.py)

[File Overlap](http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html) | [Solution](solutions/file_overlap.py)
