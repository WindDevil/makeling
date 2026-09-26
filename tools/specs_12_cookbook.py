"""Exercises for the tutorial's "Makefile Cookbook" chapter.

The cookbook Makefile is built up one piece at a time: every exercise is a
working subset of the real file, and the last one is the whole thing.  The
project the Makefile is written for never changes, only the Makefile does:
three source files in three directories, one header per module, and one C++
translation unit that the C code calls.

Recipe lines inside the ``makefile`` strings are indented with a ``\\t``
escape.  Python turns that into a real tab, which is what make requires;
writing a literal tab into the source would be invisible and easy to lose.
"""

from spec import ex, mk, step

TOPIC = "12_cookbook"

REFERENCE = "Makefile Cookbook"

# The small multi-directory project the cookbook Makefile builds.  Every
# directory under src/ is on the include path, so the sources include each
# other's headers by their base name.
PROJECT = {
    "src/main.c": """
#include <stdio.h>

/* Every directory under src/ is on the include path, so the headers of the
   other modules are included by their base name. */
#include "greet.h"
#include "thing.h"

int main(void) {
    printf("%s: value=%d\\n", greeting(), thing_value());
    return 0;
}
""",
    "src/moduleA/thing.h": """
#ifndef THING_H
#define THING_H

int thing_value(void);

#endif
""",
    "src/moduleA/detail.h": """
#ifndef DETAIL_H
#define DETAIL_H

/* Included by thing.c alone, so touching it must not rebuild anything else. */
#define THING_BASE 5

#endif
""",
    "src/moduleA/thing.c": """
#include "detail.h"
#include "thing.h"

int thing_value(void) {
    return THING_BASE + 2;
}
""",
    "src/util/greet.h": """
#ifndef GREET_H
#define GREET_H

#ifdef __cplusplus
extern "C" {
#endif

const char *greeting(void);

#ifdef __cplusplus
}
#endif

#endif
""",
    "src/util/greet.cpp": """
#include "greet.h"

const char *greeting(void) {
    return "hello from C++";
}
""",
}

# A file that sits at the top of the project but is not part of the build.
# With an unquoted find pattern the shell expands *.c to this name before
# find is even started.
SCRATCH = """
/* A scratch file at the top of the project. It is not part of the build. */
int scratch(void) {
    return 0;
}
"""

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_find_sources",
        title="Discovering the sources with find",
        objective=(
            "Let make collect every C and C++ file under ./src with "
            "$(shell find ...), leaving the patterns quoted."
        ),
        reference=REFERENCE,
        hint=(
            "SRCS is $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c'). "
            "Keep the single quotes: an unquoted *.c is expanded by the shell "
            "against the current directory before find ever sees it."
        ),
        makefile="""
SRC_DIRS := ./src

# Find all the C and C++ files we want to compile.
# Note the single quotes around the * expressions: the shell expands them
# against the current directory otherwise, and find never sees the pattern.
# (-or is find's own spelling of -o, which means "or" here as well.)
SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

.PHONY: sources
sources:
\t@for src in $(SRCS); do echo "found: $$src"; done
\t@echo "count: $(words $(SRCS))"
""",
        steps=[
            mk(
                "sources",
                stdout=(
                    "found: ./src/main.c\n"
                    "found: ./src/moduleA/thing.c\n"
                    "found: ./src/util/greet.cpp\n"
                    "count: 3"
                ),
                stdout_mode="contains_lines",
                description="find reports the three sources, in any directory order",
            ),
            mk(
                "sources",
                stdout="scratch",
                stdout_mode="not_contains",
                description="the scratch file in the project root is not a source",
            ),
        ],
        breaks=[("-name '*.c'", "-name *.c")],
        files={**PROJECT, "scratch.c": SCRATCH},
    ),
    ex(
        topic=TOPIC,
        slug="02_object_paths",
        title="Prepending the build directory",
        objective=(
            "Turn the source list into the object list the cookbook uses: "
            "$(BUILD_DIR)/./src/hello.cpp.o."
        ),
        reference=REFERENCE,
        hint=(
            "$(SRCS:%=$(BUILD_DIR)/%.o) is the substitution-reference spelling; "
            "$(patsubst %,$(BUILD_DIR)/%.o,$(SRCS)) says the same thing. The "
            "suffix-only $(SRCS:.cpp=.o) cannot add a directory."
        ),
        makefile="""
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
\t@test "$(OBJS)" = "$(OBJS_PATSUBST)" && echo "patsubst agrees with the % substitution"
\t@for obj in $(OBJS); do echo "object: $$obj"; done
\t@for obj in $(OBJS_SHORT); do echo "short: $$obj"; done
\t@for obj in $(OBJS_SUFFIX); do echo "in place: $$obj"; done
""",
        steps=[
            mk(
                "objs",
                stdout="patsubst agrees with the % substitution",
                stdout_mode="contains",
                description="both spellings of the object list agree",
            ),
            mk(
                "objs",
                stdout=(
                    "object: ./build/./src/main.c.o\n"
                    "object: ./build/./src/moduleA/thing.c.o\n"
                    "object: ./build/./src/util/greet.cpp.o"
                ),
                stdout_mode="contains_lines",
                description="every object lives under $(BUILD_DIR), in any order",
            ),
            mk(
                "objs",
                stdout=(
                    "short: ./build/main.c.o\n"
                    "short: ./build/moduleA/thing.c.o\n"
                    "short: ./build/util/greet.cpp.o"
                ),
                stdout_mode="contains_lines",
                description="matching the ./src prefix drops it from the result",
            ),
            mk(
                "objs",
                stdout=(
                    "in place: ./src/util/greet.o\n"
                    "in place: ./src/moduleA/thing.c\n"
                    "in place: ./src/main.c"
                ),
                stdout_mode="contains_lines",
                description="the suffix-only form substitutes in place",
            ),
        ],
        breaks=[("OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)", "OBJS := $(SRCS:%=%.o)")],
        files=dict(PROJECT),
    ),
    ex(
        topic=TOPIC,
        slug="03_dependency_files",
        title="One dependency file per object",
        objective=(
            "Derive the .d files from the object list with the suffix-only "
            "substitution $(OBJS:.o=.d)."
        ),
        reference=REFERENCE,
        hint=(
            "$(OBJS:.o=.d) swaps the ending of every word in the list: "
            "./build/hello.cpp.o becomes ./build/hello.cpp.d."
        ),
        makefile="""
BUILD_DIR := ./build
SRC_DIRS := ./src

SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

# String substitution (suffix version without %).
# As an example, ./build/hello.cpp.o turns into ./build/hello.cpp.d
DEPS := $(OBJS:.o=.d)

.PHONY: deps
deps:
\t@test "$(DEPS)" = "$(patsubst %.o,%.d,$(OBJS))" && echo "the suffix form matches patsubst %.o -> %.d"
\t@for dep in $(DEPS); do echo "dependency file: $$dep"; done
""",
        steps=[
            mk(
                "deps",
                stdout="the suffix form matches patsubst %.o -> %.d",
                stdout_mode="contains",
                description="the two spellings of the dependency list agree",
            ),
            mk(
                "deps",
                stdout=(
                    "dependency file: ./build/./src/main.c.d\n"
                    "dependency file: ./build/./src/moduleA/thing.c.d\n"
                    "dependency file: ./build/./src/util/greet.cpp.d"
                ),
                stdout_mode="contains_lines",
                description="every object has a matching .d file, in any order",
            ),
        ],
        breaks=[("DEPS := $(OBJS:.o=.d)", "DEPS := $(OBJS:.d=.o)")],
        files=dict(PROJECT),
    ),
    ex(
        topic=TOPIC,
        slug="04_include_dirs",
        title="Every folder in src is an include directory",
        objective=(
            "Collect ./src and its subdirectories with $(shell find ... -type d) "
            "and prefix each one with -I."
        ),
        reference=REFERENCE,
        hint=(
            "$(addprefix -I,$(INC_DIRS)) puts -I in front of every word of the "
            "list. Without it the compiler is handed bare directory names, and "
            "main.c can no longer find greet.h and thing.h."
        ),
        makefile="""
BUILD_DIR := ./build
SRC_DIRS := ./src

# Every folder in ./src will need to be passed to the compiler so that it can
# find the header files. -type d lists the directories, not the files in them.
INC_DIRS := $(shell find $(SRC_DIRS) -type d)
# Add a prefix to INC_DIRS, so ./src/moduleA becomes -I./src/moduleA.
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

.PHONY: flags
flags:
\t@for dir in $(INC_DIRS); do echo "include dir: $$dir"; done
\t@$(CC) $(INC_FLAGS) -c $(SRC_DIRS)/main.c -o main.o
\t@echo "main.c compiled with $(INC_FLAGS)"
\t@rm -f main.o
""",
        steps=[
            mk(
                "flags",
                stdout=(
                    "include dir: ./src\n"
                    "include dir: ./src/moduleA\n"
                    "include dir: ./src/util"
                ),
                stdout_mode="contains_lines",
                description="src and both of its subdirectories are collected",
            ),
            mk(
                "flags",
                stdout="main.c compiled with -I",
                stdout_mode="contains",
                description="the -I flags are what let main.c compile at all",
            ),
            mk(
                "flags",
                missing=["main.o"],
                description="the probe cleans up after itself",
            ),
        ],
        breaks=[("INC_DIRS := $(shell find $(SRC_DIRS) -type d)",
                 "INC_DIRS := $(shell find $(SRC_DIRS) -type f)")],
        files=dict(PROJECT),
    ),
    ex(
        topic=TOPIC,
        slug="05_compile_rules",
        title="The compile rules for C and C++",
        objective=(
            "Write the two pattern rules that compile every source into "
            "$(BUILD_DIR), creating the object's directory first."
        ),
        reference=REFERENCE,
        hint=(
            "The target pattern is $(BUILD_DIR)/%.c.o with %.c as the "
            "prerequisite, and the C++ rule is the same with .cpp. Every "
            "recipe starts with mkdir -p $(dir $@): on a first build there is "
            "no build/ tree at all."
        ),
        makefile="""
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
\tmkdir -p $(dir $@)
\t$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Build step for C++ source
$(BUILD_DIR)/%.cpp.o: %.cpp
\tmkdir -p $(dir $@)
\t$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@
""",
        steps=[
            mk(
                "-B",
                "objects",
                stdout="-c src/main.c -o build/./src/main.c.o",
                stdout_mode="contains",
                description="the C rule compiles main.c into the build directory",
            ),
            mk(
                "-B",
                "objects",
                stdout="-c src/util/greet.cpp -o build/./src/util/greet.cpp.o",
                stdout_mode="contains",
                description="the C++ rule compiles greet.cpp the same way",
            ),
            mk(
                "-B",
                "objects",
                stdout="mkdir -p build/./src/moduleA/",
                stdout_mode="contains",
                description="the rule creates the object's directory first",
            ),
            step(
                "test",
                "-f",
                "build/src/main.c.o",
                "-a",
                "-f",
                "build/src/moduleA/thing.c.o",
                "-a",
                "-f",
                "build/src/util/greet.cpp.o",
                description="all three objects exist under build/",
            ),
            mk(
                "objects",
                stdout="Nothing to be done for 'objects'.",
                stdout_mode="contains",
                description="a second make has nothing left to compile",
            ),
        ],
        breaks=[("\tmkdir -p $(dir $@)\n\t$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@",
                 "\t$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@")],
        files=dict(PROJECT),
    ),
    ex(
        topic=TOPIC,
        slug="06_dependency_flags",
        title="-MMD -MP write the dependency files",
        objective=(
            "Add -MMD -MP to CPPFLAGS so that every compile also writes a .d "
            "file listing the headers it read."
        ),
        reference=REFERENCE,
        hint=(
            "-MMD makes the compiler drop a dependency file next to each "
            "object as a side effect of the compile. -MP adds a phony target "
            "for every header, so that deleting a header does not break make."
        ),
        makefile="""
BUILD_DIR := ./build
SRC_DIRS := ./src

SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

DEPS := $(OBJS:.o=.d)

INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

# The -MMD and -MP flags together generate Makefiles for us!
# These files will have .d instead of .o as the output.
CPPFLAGS := $(INC_FLAGS) -MMD -MP

.PHONY: objects
objects: $(OBJS)

# Build step for C source
$(BUILD_DIR)/%.c.o: %.c
\tmkdir -p $(dir $@)
\t$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Build step for C++ source
$(BUILD_DIR)/%.cpp.o: %.cpp
\tmkdir -p $(dir $@)
\t$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@
""",
        steps=[
            mk(
                "objects",
                stdout="-MMD -MP",
                stdout_mode="contains",
                description="every compile carries the dependency flags",
            ),
            step(
                "cat",
                "build/src/main.c.d",
                stdout="src/util/greet.h:\nsrc/moduleA/thing.h:",
                stdout_mode="contains_lines",
                description="-MP wrote a phony target for each header main.c uses",
            ),
            step(
                "cat",
                "build/src/moduleA/thing.c.d",
                stdout="src/moduleA/detail.h:",
                stdout_mode="contains_lines",
                description="each object gets a dependency file of its own",
            ),
            step(
                "cat",
                "build/src/main.c.d",
                stdout="stdio.h",
                stdout_mode="not_contains",
                description="-MMD keeps system headers out of the dependency file",
            ),
        ],
        breaks=[("CPPFLAGS := $(INC_FLAGS) -MMD -MP", "CPPFLAGS := $(INC_FLAGS)")],
        files=dict(PROJECT),
    ),
    ex(
        topic=TOPIC,
        slug="07_link_executable",
        title="The final build step",
        objective=(
            "Link the objects into $(BUILD_DIR)/$(TARGET_EXEC) with "
            "$(CXX) $(OBJS) -o $@."
        ),
        reference=REFERENCE,
        hint=(
            "$@ is the target of the rule, so -o $@ puts the program in the "
            "build directory instead of the default a.out. $(OBJS) as the "
            "prerequisite is what makes the compiles happen first."
        ),
        makefile="""
TARGET_EXEC := final_program

BUILD_DIR := ./build
SRC_DIRS := ./src

SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

DEPS := $(OBJS:.o=.d)

INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

CPPFLAGS := $(INC_FLAGS) -MMD -MP

# The final build step.
$(BUILD_DIR)/$(TARGET_EXEC): $(OBJS)
\t$(CXX) $(OBJS) -o $@ $(LDFLAGS)

# Build step for C source
$(BUILD_DIR)/%.c.o: %.c
\tmkdir -p $(dir $@)
\t$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Build step for C++ source
$(BUILD_DIR)/%.cpp.o: %.cpp
\tmkdir -p $(dir $@)
\t$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@
""",
        steps=[
            mk(
                stdout="-o build/final_program",
                stdout_mode="contains",
                missing=["a.out"],
                description="bare make builds the program into the build directory",
            ),
            step(
                "sh",
                "-c",
                "./build/final_program",
                stdout="hello from C++: value=7",
                description="the linked program runs and prints its line",
            ),
            mk(
                stdout="'build/final_program' is up to date.",
                stdout_mode="contains",
                description="a second make has nothing left to link",
            ),
        ],
        breaks=[("$(CXX) $(OBJS) -o $@ $(LDFLAGS)", "$(CXX) $(OBJS) $(LDFLAGS)")],
        files=dict(PROJECT),
    ),
    ex(
        topic=TOPIC,
        slug="08_include_deps",
        title="-include the generated dependency files",
        objective=(
            "Pull the .d files into the Makefile with -include, so that "
            "touching a header recompiles only the objects that include it."
        ),
        reference=REFERENCE,
        hint=(
            "The leading dash matters: on the very first build not one .d file "
            "exists yet, and a plain include would stop make with \"No rule to "
            "make target\" before it compiles anything."
        ),
        makefile="""
TARGET_EXEC := final_program

BUILD_DIR := ./build
SRC_DIRS := ./src

SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

DEPS := $(OBJS:.o=.d)

INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

CPPFLAGS := $(INC_FLAGS) -MMD -MP

# The final build step.
$(BUILD_DIR)/$(TARGET_EXEC): $(OBJS)
\t$(CXX) $(OBJS) -o $@ $(LDFLAGS)

# Build step for C source
$(BUILD_DIR)/%.c.o: %.c
\tmkdir -p $(dir $@)
\t$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Build step for C++ source
$(BUILD_DIR)/%.cpp.o: %.cpp
\tmkdir -p $(dir $@)
\t$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@

# Include the .d makefiles. The - at the front suppresses the errors of missing
# Makefiles. Initially, all the .d files will be missing, and we don't want
# those errors to show up.
-include $(DEPS)
""",
        steps=[
            mk(
                stdout="-c src/main.c -o build/./src/main.c.o",
                stdout_mode="contains",
                description="the first build compiles everything from nothing",
            ),
            mk(
                stdout="'build/final_program' is up to date.",
                stdout_mode="contains",
                description="a second make has nothing to do",
            ),
            step(
                "touch",
                "src/moduleA/detail.h",
                description="make the header that only thing.c includes newer",
            ),
            mk(
                "-n",
                stdout="-c src/main.c -o",
                stdout_mode="not_contains",
                description="main.c does not include detail.h, so it is not recompiled",
            ),
            mk(
                "-n",
                stdout="-c src/moduleA/thing.c -o",
                stdout_mode="contains",
                description="the .d file says thing.c does include detail.h",
            ),
            mk(
                stdout="-c src/moduleA/thing.c -o",
                stdout_mode="contains",
                description="the rebuild recompiles exactly that one object",
            ),
            mk(
                stdout="'build/final_program' is up to date.",
                stdout_mode="contains",
                description="and then everything is up to date again",
            ),
        ],
        breaks=[("-include $(DEPS)", "include $(DEPS)")],
        files=dict(PROJECT),
    ),
    ex(
        topic=TOPIC,
        slug="09_full_cookbook",
        title="The whole cookbook Makefile",
        objective=(
            "Assemble the complete cookbook Makefile: sources, objects, "
            "dependency files, include flags, both compile rules, the link "
            "step and clean."
        ),
        reference=REFERENCE,
        hint=(
            "Read your Makefile next to the tutorial's, top to bottom. Every "
            "source is compiled by a pattern rule of its own language, so a "
            "missing C++ rule leaves greet.cpp without a way to become an "
            "object."
        ),
        makefile="""
# Thanks to Job Vranish (https://spin.atomicobject.com/2016/08/26/makefile-c-projects/)
TARGET_EXEC := final_program

BUILD_DIR := ./build
SRC_DIRS := ./src

# Find all the C and C++ files we want to compile
# Note the single quotes around the * expressions. The shell will incorrectly
# expand these otherwise, but we want to send the * directly to the find command.
SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

# Prepends BUILD_DIR and appends .o to every src file
# As an example, ./your_dir/hello.cpp turns into ./build/./your_dir/hello.cpp.o
OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

# String substitution (suffix version without %).
# As an example, ./build/hello.cpp.o turns into ./build/hello.cpp.d
DEPS := $(OBJS:.o=.d)

# Every folder in ./src will need to be passed to GCC so that it can find
# header files
INC_DIRS := $(shell find $(SRC_DIRS) -type d)
# Add a prefix to INC_DIRS. So moduleA would become -ImoduleA. GCC understands
# this -I flag
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

# The -MMD and -MP flags together generate Makefiles for us!
# These files will have .d instead of .o as the output.
CPPFLAGS := $(INC_FLAGS) -MMD -MP

# The final build step.
$(BUILD_DIR)/$(TARGET_EXEC): $(OBJS)
\t$(CXX) $(OBJS) -o $@ $(LDFLAGS)

# Build step for C source
$(BUILD_DIR)/%.c.o: %.c
\tmkdir -p $(dir $@)
\t$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Build step for C++ source
$(BUILD_DIR)/%.cpp.o: %.cpp
\tmkdir -p $(dir $@)
\t$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@

.PHONY: clean
clean:
\trm -r $(BUILD_DIR)

# Include the .d makefiles. The - at the front suppresses the errors of missing
# Makefiles. Initially, all the .d files will be missing, and we don't want
# those errors to show up.
-include $(DEPS)
""",
        steps=[
            mk(
                stdout="-c src/main.c -o build/./src/main.c.o",
                stdout_mode="contains",
                description="the C source is compiled into the build directory",
            ),
            mk(
                "-B",
                stdout="-c src/util/greet.cpp -o build/./src/util/greet.cpp.o",
                stdout_mode="contains",
                description="the C++ source gets its own rule",
            ),
            mk(
                "-B",
                stdout="-o build/final_program",
                stdout_mode="contains",
                description="both kinds of object are linked into the program",
            ),
            step(
                "sh",
                "-c",
                "./build/final_program",
                stdout="hello from C++: value=7",
                description="the program actually runs",
            ),
            mk(
                "clean",
                stdout="rm -r ./build",
                stdout_mode="contains",
                missing=["build"],
                description="clean removes the whole build directory",
            ),
            mk(
                stdout="-o build/final_program",
                stdout_mode="contains",
                description="a clean tree builds again from nothing",
            ),
            step(
                "touch",
                "src/moduleA/detail.h",
                description="make a header newer than the objects",
            ),
            mk(
                stdout="-c src/moduleA/thing.c -o",
                stdout_mode="contains",
                description="only the object that includes it is recompiled",
            ),
            mk(
                stdout="'build/final_program' is up to date.",
                stdout_mode="contains",
                description="and the build settles",
            ),
        ],
        breaks=[
            (
                "# Build step for C++ source\n"
                "$(BUILD_DIR)/%.cpp.o: %.cpp\n"
                "\tmkdir -p $(dir $@)\n"
                "\t$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@",
                "# Build step for C++ source\n"
                "# greet.cpp still has no rule that turns it into an object.",
            )
        ],
        files=dict(PROJECT),
    ),
]
