.PHONY: build build27 build33 test test27 test33 testall clean release

build:
	rm -rf env
	virtualenv env
	env/bin/pip install -r requirements.txt

build27:
	rm -rf env27
	virtualenv --python=python2.7 env27
	env27/bin/pip install -r requirements.txt

build33:
	rm -rf env33
	virtualenv --python=python3.3 env33
	env33/bin/pip install -r requirements.txt

test:
	. env/bin/activate; py.test omdb tests

test27:
	. env27/bin/activate; py.test omdb tests

test33:
	. env33/bin/activate; py.test omdb tests

testall: test27 test33

clean:
	rm -rf env
	rm -rf env27
	rm -rf env33
	rm -f *.pyc omdb/*.pyc tests/*.pyc
	rm -rf dist *.egg*

release:
	python setup.py sdist upload
	rm -r dist *.egg*

