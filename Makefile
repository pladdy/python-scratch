.PHONY: dependencies lint mac-dependencies mac-python python-depdencies test

HOMEBREW = $(shell which homebrew)

all:
ifdef HOMEBREW
	$(MAKE) mac-dependencies
else
$(info HOMEBREW undefined, cannott proceed)
endif

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
	pipenv install

test:
	PYTHONPATH=./ pipenv run pytest -s -v
