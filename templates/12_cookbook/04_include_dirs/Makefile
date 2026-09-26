# makeling exercise: 12_cookbook/04_include_dirs
# title: Every folder in src is an include directory
# objective: Collect ./src and its subdirectories with $(shell find ... -type d) and prefix each one with -I.
# reference: Makefile Cookbook
# hint: $(addprefix -I,$(INC_DIRS)) puts -I in front of every word of the list. Without it the compiler is handed bare directory names, and main.c can no longer find greet.h and thing.h.

BUILD_DIR := ./build
SRC_DIRS := ./src

# Every folder in ./src will need to be passed to the compiler so that it can
# find the header files. -type d lists the directories, not the files in them.
INC_DIRS := $(shell find $(SRC_DIRS) -type f)
# Add a prefix to INC_DIRS, so ./src/moduleA becomes -I./src/moduleA.
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

.PHONY: flags
flags:
	@for dir in $(INC_DIRS); do echo "include dir: $$dir"; done
	@$(CC) $(INC_FLAGS) -c $(SRC_DIRS)/main.c -o main.o
	@echo "main.c compiled with $(INC_FLAGS)"
	@rm -f main.o
