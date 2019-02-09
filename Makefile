.PHONY: dependencies mac-dependencies

# should i be using pip3 directly?
dependencies:
	pip3 install --user pipenv
	pip3 install --user pytest

mac-dependencies:
	brew install python3

test:
	pipenv run pytest
