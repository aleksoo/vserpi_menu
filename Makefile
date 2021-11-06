PYTHON = python3

.PHONY: init run

init: requirements.txt
	pip install -r requirements.txt

run:
	$(PYTHON) main.py



.DEFALT: help
help:
	@echo "Options are: init, run"