# makefiling exercise: 12_cookbook/02_object_paths
# title: Prepending the build directory
# objective: Turn the source list into the object list the cookbook uses: $(BUILD_DIR)/./src/hello.cpp.o.
# reference: Makefile Cookbook
# hint: $(SRCS:%=$(BUILD_DIR)/%.o) is the substitution-reference spelling; $(patsubst %,$(BUILD_DIR)/%.o,$(SRCS)) says the same thing. The suffix-only $(SRCS:.cpp=.o) cannot add a directory.

BUILD_DIR := ./build
SRC_DIRS := ./src

SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

# Prepends BUILD_DIR and appends .o to every src file.
# As an example, ./your_dir/hello.cpp turns into ./build/./your_dir/hello.cpp.o
OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

# The same list spelled with patsubst. Here % stands for the whole word.
OBJS_PATSUBST := $(patsubst %,$(BUILD_DIR)/%.o,$(SRCS))

# Matching the ./src prefix instead gives the shorter ./build/main.c.o.
OBJS_SHORT := $(patsubst ./src/%,$(BUILD_DIR)/%.o,$(SRCS))

# The suffix-only form substitutes in place: it cannot add a directory, and
# words that do not end in .cpp are left alone.
OBJS_SUFFIX := $(SRCS:.cpp=.o)

.PHONY: objs
objs:
	@test "$(OBJS)" = "$(OBJS_PATSUBST)" && echo "patsubst agrees with the % substitution"
	@for obj in $(OBJS); do echo "object: $$obj"; done
	@for obj in $(OBJS_SHORT); do echo "short: $$obj"; done
	@for obj in $(OBJS_SUFFIX); do echo "in place: $$obj"; done
