# makefiling - a Makefile tutorial you can run.
#
# This Makefile is itself part of the teaching material, so it follows the
# advice the tutorial gives: one variable per tool, .PHONY for every target
# that is not a file, and a self-documenting help target.

PYTHON   ?= python3
MAKEFILING ?= ./makefiling

.DEFAULT_GOAL := help

.PHONY: help start list run next verify selftest generate check-generated check-tracked doctor clean format lint test

help: ## Show this help
	@printf '%s\n' 'makefiling targets:'
	@grep -hE '^[a-zA-Z0-9_-]+:.*?## ' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  make %-17s %s\n", $$1, $$2}'

list: ## List every exercise and its progress
	$(MAKEFILING) list

start: ## Start the guided beginner route
	$(MAKEFILING) start

run: ## Run the next unsolved exercise
	$(MAKEFILING) run

next: ## Show the next unsolved exercise
	$(MAKEFILING) next

verify: ## Run every solution against its checks
	$(MAKEFILING) verify

selftest: ## Check original templates fail and every solution passes
	$(MAKEFILING) selftest

generate: ## Regenerate exercises from tools/specs_*.py
	$(PYTHON) tools/generate_exercises.py

check-generated: ## Fail if the generated files are stale
	$(PYTHON) tools/generate_exercises.py --check

doctor: ## Print the detected toolchain
	$(MAKEFILING) doctor

check-tracked: ## Fail if an exercise file would be missing from a clone
	@ignored=$$(git ls-files --others --ignored --exclude-standard \
		exercises solutions templates); \
	if [ -n "$$ignored" ]; then \
		echo 'these files are ignored by .gitignore, so a clone would not have them:'; \
		echo "$$ignored"; \
		exit 1; \
	fi; \
	untracked=$$(git ls-files --others --exclude-standard \
		exercises solutions templates); \
	if [ -n "$$untracked" ]; then \
		echo 'these files exist but are not committed:'; \
		echo "$$untracked"; \
		exit 1; \
	fi; \
	echo 'every file under exercises/, solutions/ and templates/ is committed'

clean: ## Remove staged working copies
	$(MAKEFILING) clean

format: ## Run clang-format over the C files, if it is installed
	@if command -v clang-format >/dev/null 2>&1; then \
		find exercises solutions -name '*.c' -print0 | xargs -0 clang-format -i; \
		echo 'formatted the C sources'; \
	else \
		echo 'clang-format is not installed; skipping'; \
	fi

lint: ## Byte-compile the tooling and validate every checks.json
	$(PYTHON) -m compileall -q tools $(MAKEFILING)
	@find . -name checks.json -not -path './build/*' -print0 \
		| xargs -0 -n1 $(PYTHON) -m json.tool > /dev/null
	@echo 'tooling compiles and every checks.json parses'

test: ## Run focused CLI regression tests
	$(PYTHON) -m unittest discover -s tests -v
