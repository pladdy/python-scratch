.PHONY: requirements.txt requirements-dev.txt

APP = python_scratch
TEST = poetry run pytest -x -s -rA --durations=10 -vv --cov $(APP) $(TESTS)
TESTS = tests

all: poetry install

bump-major:
	poetry run bumpversion major

bump-minor:
	poetry run bumpversion minor

bump-patch:
	poetry run bumpversion patch

bump-reset:
	git reset HEAD~1

clean:
	find ./ -type d -name *__pycache__ -exec rm -rf {} \;
	rm .coverage coverage.xml
	rm -rf .pytest_cache htmlcov

cov-reports:
	$(TEST) --cov-report html

cover: cov-reports
	open htmlcov/index.html

cover-codacy: cov-reports
	poetry run coverage xml
	source .env && poetry run python-codacy-coverage -r coverage.xml

install:
	poetry install

lint: pre-commit

pre-commit:
	poetry run pre-commit run --all-files

release:
	git push && git push --tags

test:
	$(TEST)

vulnerability:
	poetry run safety check
