.PHONY: all clean dependencies lint mac-dependencies mac-python python-depdencies test

HOMEBREW = $(shell which homebrew)

all:
ifdef HOMEBREW
	$(MAKE) mac-dependencies
else
	$(info HOMEBREW undefined, assuming python3 and pip3 are installed...)
	$(MAKE) python-dependencies
endif

clean:
	rm -rf htmlcov venv

cover:
	PYTHONPATH=./ pipenv run pytest -v --cov python_scratch .
	coverage html
	open htmlcov/index.html

lint:
	pylama python_scratch/ tests/

mac-dependencies: mac-python python-dependencies

mac-python:
	brew install python3

python-dependencies:
	pip install pipenv
	pipenv install

test:
	PYTHONPATH=./ pipenv run pytest -s -v
