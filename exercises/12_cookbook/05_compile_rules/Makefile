# makefiling exercise: 12_cookbook/05_compile_rules
# title: The compile rules for C and C++
# objective: Write the two pattern rules that compile every source into $(BUILD_DIR), creating the object's directory first.
# reference: Makefile Cookbook
# hint: The target pattern is $(BUILD_DIR)/%.c.o with %.c as the prerequisite, and the C++ rule is the same with .cpp. Every recipe starts with mkdir -p $(dir $@): on a first build there is no build/ tree at all.

BUILD_DIR := ./build
SRC_DIRS := ./src

SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

# Flags for every compile: the include directories for now.
CPPFLAGS := $(INC_FLAGS)

.PHONY: objects
objects: $(OBJS)

# Build step for C source
$(BUILD_DIR)/%.c.o: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Build step for C++ source
$(BUILD_DIR)/%.cpp.o: %.cpp
	mkdir -p $(dir $@)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@
