.PHONY: build test testall clean release

build:
	rm -rf env
	virtualenv env
	env/bin/pip install -r requirements.txt

test:
	. env/bin/activate; py.test omdb tests

testall:
	. env/bin/activate; tox

clean:
	rm -rf env
	rm -f *.pyc omdb/*.pyc tests/*.pyc
	rm -rf omdb/__pycache__ tests/__pycache__
	rm -rf dist *.egg*

release:
	python setup.py sdist upload
	python setup.py bdist_wheel upload
	rm -r dist *.egg*

