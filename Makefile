PYTHON := env/bin/python


test:
	$(PYTHON) -m unittest discover tests


.PHONY: test
