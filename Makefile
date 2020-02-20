.PHONY: build

build:
	python3 setup.py sdist bdist_wheel
publish: build
	python3 -m twine upload  dist/*
