
.PHONY: test env

test:
	. env/bin/activate && py.test omdb

env:
	virtualenv env
	env/bin/pip install -r requirements.txt
