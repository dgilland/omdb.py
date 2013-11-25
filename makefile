
.PHONY: test env build pypi

test:
	. env/bin/activate; py.test omdb tests

env:
	virtualenv env
	env/bin/pip install -r requirements.txt

build:
	. env/bin/activate; python build.py

pypi:
	python setup.py sdist upload

