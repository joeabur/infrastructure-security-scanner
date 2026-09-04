.PHONY: test scan

test:
	python3 -m pytest

scan:
	PYTHONPATH=src python3 -m scanner.cli --target localhost --format terminal
