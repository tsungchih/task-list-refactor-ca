ifneq (,$(wildcard ./.env))
  include .env
  export
endif

.PHONY: tests
.DEFAULT_GOAL := help

# Define COLORS
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

TARGET_MAX_CHAR_NUM=20

# project settings
WORKING_DIR := $(shell pwd)
PROJ_NAME := $(shell poetry version | cut -d ' ' -f 1)
PROJ_VERSION := $(shell poetry version --short)
LIB_NAME := $(shell echo ${PROJ_NAME} | sed -e "s/-/_/g")
PYTEST_DIRS := $(shell ls -d tests)

## Show help information
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

# Check if a command exists
cmd-exists-%:
	@hash $(*) > /dev/null 2>&1 || \
		(echo "Forget to run 'poetry shell'???\nERROR: '$(*)' must be installed and available on your PATH."; exit 1)
## Build Python package
build-pkg:
	@poetry build

## Run pytest to all the packages in the repository
tests: cmd-exists-poetry
	@echo "=> Running pytest"
	@poetry run pytest
	@echo "==> Running pytest complete"
