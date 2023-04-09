install:
	poetry install

run:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv