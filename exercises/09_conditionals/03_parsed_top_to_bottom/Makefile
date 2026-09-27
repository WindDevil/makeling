# makefiling exercise: 09_conditionals/03_parsed_top_to_bottom
# title: The conditional is decided while the file is read
# objective: Assign MODE before the conditional that tests it, so that a bare make reports the debug build.
# reference: Conditional if/else
# hint: make reads the file from the first line to the last and resolves each conditional the moment it reaches it. An assignment further down the file has not happened yet.

all:
ifeq ($(MODE),debug)
	echo "debug build"
else
	echo "release build"
endif

MODE = debug
