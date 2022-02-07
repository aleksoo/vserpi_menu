PYTHON = python3

.PHONY: init run

init: requirements.txt
	pip3 install -r requirements.txt

run:
	$(PYTHON) Menu.py



.DEFALT: help
help:
	@echo "Options are: init, run"