PYTHON		= python
PIP			= pip
PYTEST		= pytest

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -rf .pytest_cache/
	find . -name '*.egg-info' -exec rm -fr {} +

clean: clean-build
	echo "****** CLEAN ******"

dist: clean
	$(PYTHON) setup.py sdist

devel:
	$(PIP) install -e .[dev]

install:
	$(PIP) install -e .

test: clean
	$(PYTEST) -p no:cacheprovider
