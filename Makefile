.PHONY: all clean dependencies lint mac-dependencies mac-python python-depdencies test

HOMEBREW = $(shell which homebrew)
TEST = PYTHONPATH=./ pipenv run pytest -s -v

all:
ifdef HOMEBREW
	$(MAKE) mac-dependencies
else
	$(info HOMEBREW undefined, assuming python3 and pip3 are installed...)
	$(MAKE) python-dependencies
endif

clean:
	rm -rf htmlcov venv

cover: htmlcov
	coverage html
	open htmlcov/index.html

htmlcov:
	$(TEST) --cov data_structures

lint:
	pylama python_scratch/ tests/

mac-dependencies: mac-python python-dependencies

mac-python:
	-brew install python3
	-brew install pandoc

python-dependencies:
	pip3 install pipenv
	pipenv install

test:
	$(TEST)

test-with-cov: test htmlcov
