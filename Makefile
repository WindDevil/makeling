# makeling - a Makefile tutorial you can run.
#
# This Makefile is itself part of the teaching material, so it follows the
# advice the tutorial gives: one variable per tool, .PHONY for every target
# that is not a file, and a self-documenting help target.

PYTHON   ?= python3
MAKELING ?= ./makeling

.DEFAULT_GOAL := help

.PHONY: help list run next verify selftest generate check-generated doctor clean format lint

help: ## Show this help
	@printf '%s\n' 'makeling targets:'
	@grep -hE '^[a-zA-Z0-9_-]+:.*?## ' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  make %-17s %s\n", $$1, $$2}'

list: ## List every exercise and its progress
	$(MAKELING) list

run: ## Run the next unsolved exercise
	$(MAKELING) run

next: ## Show the next unsolved exercise
	$(MAKELING) next

verify: ## Run every solution against its checks
	$(MAKELING) verify

selftest: ## Check that every exercise starts unsolved and every solution passes
	$(MAKELING) selftest

generate: ## Regenerate exercises from tools/specs_*.py
	$(PYTHON) tools/generate_exercises.py

check-generated: ## Fail if the generated files are stale
	$(PYTHON) tools/generate_exercises.py --check

doctor: ## Print the detected toolchain
	$(MAKELING) doctor

clean: ## Remove staged working copies
	$(MAKELING) clean

format: ## Run clang-format over the C files, if it is installed
	@if command -v clang-format >/dev/null 2>&1; then \
		find exercises solutions -name '*.c' -print0 | xargs -0 clang-format -i; \
		echo 'formatted the C sources'; \
	else \
		echo 'clang-format is not installed; skipping'; \
	fi

lint: ## Byte-compile the tooling and validate every checks.json
	$(PYTHON) -m compileall -q tools $(MAKELING)
	@find . -name checks.json -not -path './build/*' -print0 \
		| xargs -0 -n1 $(PYTHON) -m json.tool > /dev/null
	@echo 'tooling compiles and every checks.json parses'
