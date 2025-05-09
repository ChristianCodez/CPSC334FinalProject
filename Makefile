# This is my makefile for the Python application DataFrame

# Variables
PYTHON = python3
PIP = pip3
TEST_DIR = tests
SRC_DIR = src
APP_NAME = DataFrame
VERSION = v2.0.0
BUILD_DIR = build
DEB_NAME = $(APP_NAME)-$(VERSION)

# default target
all: help

# run the application
run:
	python3 DataFrame.py

# test the application
test:
	pytest

# build the application (for packaging)
build:
	mkdir -p $(BUILD_DIR)
	cp $(APP_NAME).py $(BUILD_DIR)/$(APP_NAME)

# installs dependencies
install:
	$(PIP) install -r requirements.txt

# clean temp files
clean:
	rm -rf $(BUILD_DIR) *.deb *.tar.gz package

# build the debian package
build-deb: build
	./build_deb.sh

# lint the debian package
lint-deb: build-deb
	- lintian $(DEB_NAME).deb


# help
help:
	@echo "Makefile for Python Counter Project"
	@echo "Usage:"
	@echo " make build      - Build the application"
	@echo " make run        - Run the application"
	@echo " make test       - Run the tests"
	@echo " make install    - Install dependencies"
	@echo " make clean      - Clean up temporary files"
	@echo " make build-deb  - Build the Debian package"
	@echo " make lint-deb   - Lint the Debian package"
	@echo " make help       - Show this help message"
