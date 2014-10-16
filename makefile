##
# Variables
##

ENV_NAME = env
ENV_ACT = . env/bin/activate;
PIP = $(ENV_NAME)/bin/pip
PYTEST_ARGS = --doctest-modules -v -s
PYTEST_TARGET = omdb tests
COVERAGE_ARGS = --cov-config setup.cfg --cov-report term-missing --cov
COVERAGE_TARGET = omdb


##
# Targets
##

.PHONY: build
build: clean install

.PHONY: clean
clean: clean-env clean-files

.PHONY: clean-env
clean-env:
	rm -rf $(ENV_NAME)

.PHONY: clean-files
clean-files:
	rm -rf .tox
	rm -rf .coverage
	find . -name \*.pyc -type f -delete
	find . -name \*.test.db -type f -delete
	find . -depth -name __pycache__ -type d -exec rm -rf {} \;
	rm -rf dist *.egg* build

.PHONY: install
install:
	rm -rf $(ENV_NAME)
	virtualenv --no-site-packages $(ENV_NAME)
	$(PIP) install -r requirements.txt

.PHONY: test
test:
	$(ENV_ACT) py.test $(PYTEST_ARGS) $(COVERAGE_ARGS) $(COVERAGE_TARGET) $(PYTEST_TARGET)

.PHONY: test-full
test-full: lint test-tox clean-files

.PHONY: test-tox
test-tox:
	rm -rf .tox
	$(ENV_ACT) tox

.PHONY: lint
lint: pylint pep8

.PHONY: pep8
pep8:
	$(ENV_ACT) pep8 $(PYTEST_TARGET)

.PHONY: pylint
pylint:
	$(ENV_ACT) pylint $(COVERAGE_TARGET)

.PHONY: release
release:
	$(ENV_ACT) python setup.py sdist bdist_wheel
	$(ENV_ACT) twine upload dist/*
	rm -rf dist *.egg* build

##
# TravisCI
##

.PHONY: travisci-install
travisci-install:
	pip install -r requirements.txt

.PHONY: travisci-test
travisci-test:
	pep8 $(PYTEST_TARGET)
	pylint -E $(COVERAGE_TARGET)
	py.test $(PYTEST_ARGS) $(COVERAGE_ARGS) $(COVERAGE_TARGET) $(PYTEST_TARGET)
