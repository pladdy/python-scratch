.PHONY: dependencies freeze mac-dependencies mac-python test

HOMEBREW = $(shell which homebrew)

all:
ifdef HOMEBREW
	$(MAKE) mac-dependencies
else
$(info HOMEBREW undefined, cannott proceed)
endif

coverage:
	PYTHONPATH=./ pipenv run pytest --cov python_scratch .
	coverage html
	open htmlcov/index.html

freeze:
	pip3 freeze > requirements.txt

install:
	pip3 install -r requirements.txt

# should i be using pip3 directly?
mac-dependencies: mac-python python-dependencies

mac-python:
	# installs pip3 and some others
	brew install python3

python-dependencies:
	pip3 install --user cookiecutter
	pip3 install --user sphinx
	pip3 install --user pipenv
	pip3 install --user pytest
	pip3 install --user pytest-cov
	pip3 install --user pylama

test:
	PYTHONPATH=./ pipenv run pytest
