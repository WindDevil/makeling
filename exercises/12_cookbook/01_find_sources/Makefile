# makefiling exercise: 12_cookbook/01_find_sources
# title: Discovering the sources with find
# objective: Let make collect every C and C++ file under ./src with $(shell find ...), leaving the patterns quoted.
# reference: Makefile Cookbook
# hint: SRCS is $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c'). Keep the single quotes: an unquoted *.c is expanded by the shell against the current directory before find ever sees it.

SRC_DIRS := ./src

# Find all the C and C++ files we want to compile.
# Note the single quotes around the * expressions: the shell expands them
# against the current directory otherwise, and find never sees the pattern.
# (-or is find's own spelling of -o, which means "or" here as well.)
SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name *.c -or -name '*.s')

.PHONY: sources
sources:
	@for src in $(SRCS); do echo "found: $$src"; done
	@echo "count: $(words $(SRCS))"
