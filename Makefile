run_packages: install build publish package-install

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	#python3 -m pip install --user dist/*.whl
	#start from virtual environment
	python3 -m pip install dist/*.whl --force-reinstall
