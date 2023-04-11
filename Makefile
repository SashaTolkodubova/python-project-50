install:
	poetry install
build:
	poetry build

run:
	poetry run gendiff ${file1_path} ${file2_path}

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=gendiff --cov-report=xml