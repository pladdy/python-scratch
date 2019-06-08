.PHONY: all bandit black clean dependencies docs lint mac-dependencies mac-python python-depdencies test

HOMEBREW = $(shell which homebrew)
TEST = PYTHONPATH=./ pipenv run pytest -s -v
LIB = python_scratch/
DIRS = $(LIB) tests/

all:
ifdef HOMEBREW
	$(MAKE) mac-dependencies
else
	$(info HOMEBREW undefined, assuming python3 and pip3 are installed...)
	$(MAKE) python-dependencies
endif

all-tests: black test lint bandit cover

bandit:
	bandit -c bandit.yaml -r $(DIRS)

black:
	black --exclude git --exclude venv ./

clean:
	rm -rf htmlcov venv

cover: htmlcov
	coverage html
	open htmlcov/index.html

docs:
	pipenv run pdoc --html data_structures --overwrite
	pipenv run pdoc --html algorithms --overwrite
	open html/data_structures/index.html
	open html/algorithms/index.html

htmlcov:
	$(TEST) --cov $(LIB)

lint:
	pylama -o pylama.ini $(DIRS)

mac-dependencies: mac-python python-dependencies

mac-python:
	-brew install python3
	-brew install pandoc

python-dependencies:
	pip3 install pipenv
	pip3 install black
	pipenv --python 3.7
	pipenv install

test:
	$(TEST)

test-name:
ifdef name
	$(TEST) -k $(name)
else
	@echo Syntax is 'make $@ name=<test name>'
endif

test-with-cov: test htmlcov
