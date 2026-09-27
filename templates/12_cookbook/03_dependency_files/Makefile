# makefiling exercise: 12_cookbook/03_dependency_files
# title: One dependency file per object
# objective: Derive the .d files from the object list with the suffix-only substitution $(OBJS:.o=.d).
# reference: Makefile Cookbook
# hint: $(OBJS:.o=.d) swaps the ending of every word in the list: ./build/hello.cpp.o becomes ./build/hello.cpp.d.

BUILD_DIR := ./build
SRC_DIRS := ./src

SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

# String substitution (suffix version without %).
# As an example, ./build/hello.cpp.o turns into ./build/hello.cpp.d
DEPS := $(OBJS:.d=.o)

.PHONY: deps
deps:
	@test "$(DEPS)" = "$(patsubst %.o,%.d,$(OBJS))" && echo "the suffix form matches patsubst %.o -> %.d"
	@for dep in $(DEPS); do echo "dependency file: $$dep"; done
