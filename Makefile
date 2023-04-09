install:
	poetry install

run:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=python-project-50 --cov-report xml
