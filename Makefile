build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

install:
	poetry install

gendiff:
	poetry run gendiff -h

reinstal:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff