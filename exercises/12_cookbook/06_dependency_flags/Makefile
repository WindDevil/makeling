# makeling exercise: 12_cookbook/06_dependency_flags
# title: -MMD -MP write the dependency files
# objective: Add -MMD -MP to CPPFLAGS so that every compile also writes a .d file listing the headers it read.
# reference: Makefile Cookbook
# hint: -MMD makes the compiler drop a dependency file next to each object as a side effect of the compile. -MP adds a phony target for every header, so that deleting a header does not break make.

BUILD_DIR := ./build
SRC_DIRS := ./src

SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

DEPS := $(OBJS:.o=.d)

INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

# The -MMD and -MP flags together generate Makefiles for us!
# These files will have .d instead of .o as the output.
CPPFLAGS := $(INC_FLAGS)

.PHONY: objects
objects: $(OBJS)

# Build step for C source
$(BUILD_DIR)/%.c.o: %.c
	mkdir -p $(dir $@)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Build step for C++ source
$(BUILD_DIR)/%.cpp.o: %.cpp
	mkdir -p $(dir $@)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@
