.PHONY: deps lint test run

deps: requirements.txt test_requirements.txt
	pip install -r requirements.txt
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

test:
	PYTHONPATH=. pytest

run:
	python hello_world/main.py