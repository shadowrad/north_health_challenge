.PHONY: lint format typecheck test all

lint:
	flake8 .
	isort --check-only .
	black --check .

format:
	isort .
	black .

typecheck:
	mypy .

test:
	pytest

all: lint typecheck test