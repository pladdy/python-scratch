# python-scratch
My sandbox/playground to play with python.

## Goals
- Use/learn python 3
- do work in a isolated environment (meaning libraries aren't installed globally, but locally like you can with bundler in ruby)
- see how testing works in python

### How I set up on my mac
I installed python3 via brew:
`brew install python3`

Then I added some aliases to my .alias file:
```
alias pip='pip3'
alias python='python3'
```

Then I installed cookiecutter and used a cookiecutter template to create the project:
Reference: https://github.com/kragniz/cookiecutter-pypackage-minimal
```
pip install cookiecutter
git clone https://github.com/kragniz/cookiecutter-pypackage-minimal.git
cookiecutter cookiecutter-pypackage-minimal/
# followed the prompts and made this shiny pile of bits
```

Then I decided on using virtualenv for my environment control.  I based this on some stack overflow reading and finally just going
through this: https://docs.python-guide.org/dev/virtualenvs/

At this point I had a project, so I started using pipenv to do the things.  I had to install pipenv first, then used it
to install other things.  This ends up creating a Pipfile of dependencies which I checked in.  Now one can just use `make`
and dependencies should be taken care of with pipenv and the Pipfile.
```
pip install pipenv
pipenv install cookiecutter
pipenv install sphinx
pipenv install pipenv
pipenv install pytest
pipenv install pytest-cov
pipenv install pylama
pipenv install pylama-pylint
```

### How to set up now
Below installs pipenv, which also installs virtualenv:
```
make
# assuming that went well, run tests to verify
make test
```

### Using virtualenv
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
* Python Guide: https://docs.python-guide.org/
  * It covers a lot of topics from tools like logging, build/deploy, concurrency, etc.
* Testing with pytest: https://docs.pytest.org/en/latest/
* Documenting Tool: http://www.sphinx-doc.org/en/master/
