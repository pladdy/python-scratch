.PHONY: all bandit black clean dependencies docs lint mac-dependencies mac-python python-depdencies test

HOMEBREW = $(shell which homebrew)
TEST = PYTHONPATH=./ pipenv run pytest -s -v
DIRS = data_structures/ algorithms/ tests/

all:
ifdef HOMEBREW
	$(MAKE) mac-dependencies
else
	$(info HOMEBREW undefined, assuming python3 and pip3 are installed...)
	$(MAKE) python-dependencies
endif

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
	$(TEST) --cov data_structures

lint:
	pylama python_scratch/ tests/

mac-dependencies: mac-python python-dependencies

mac-python:
	-brew install python3
	-brew install pandoc

python-dependencies:
	pip3 install pipenv
	pip3 install black
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
