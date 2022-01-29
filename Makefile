.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	pre-commit run --all-files

test: ## run tests quickly with the default Python
	py.test

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/poc_semantic_release.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ poc_semantic_release
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

release: dist ## package and upload a release
	twine upload dist/*

install: clean ## install the package to the active Python's site-packages
	install install .

develop: clean ## install the package in development mode
	pip install -e '.[dev]'
	git init  # it is safe to run it more than one time
	pre-commit install
