# python-scratch
My sandbox/playground to play with python

## Setup/Install for Mac
Goal is to use python 3.x with `virtualenv`.  I based this on some stack overflow reading and finally just going
through this: https://docs.python-guide.org/dev/virtualenvs/

I used home brew to install:
```
brew install python3
pipenv install cookiecutter
pipenv install sphinx
pipenv install pipenv
pipenv install pytest
pipenv install pytest-cov
pipenv install pylama
pipenv install pylama-pylint
```

Edited my .aliases file
```sh
alias pip='pip3'
alias python='python3'
```

Installed dependences (check Makefile for list)
`make`

### Cookiecutter
Used a template to set up project:
Reference: https://github.com/kragniz/cookiecutter-pypackage-minimal

```
git clone https://github.com/kragniz/cookiecutter-pypackage-minimal.git
cookiecutter cookiecutter-pypackage-minimal/
```

Below installs pipenv, which also installs virtualenv
`make dependencies`

### Virtualenv
Using the virtual environment manually:
```
source venv/bin/activate
# do some stuff in a virtual python env
deactivate
```

Add aliases to make this less verbose:
```
vim ~/.aliases
alias act='source venv/bin/activate'
alias deact='deactivate'
```

## References
Python Guide: https://docs.python-guide.org/
- It covers a lot of topics from tools like logging, build/deploy, concurrency, etc.
Testing: https://docs.pytest.org/en/latest/
Documenting: http://www.sphinx-doc.org/en/master/
