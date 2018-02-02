init:
	pip install -r requirements.txt

test:
	nosetests tests -v
.PHONY: init test