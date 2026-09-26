# makeling exercise: 06_fancy_rules/09_static_pattern_filter
# title: Picking targets with $(filter ...)
# objective: Use $(filter) to give .o files and .result files their own static pattern rules, so that each kind is built from the right source.
# reference: Static Pattern Rules and Filter
# hint: $(filter %.o,$(obj_files)) keeps only the .o names, so the rule after the colon only applies to those.  .PHONY matters here: without it make tries to link the program all from its prereqs.

obj_files = foo.result bar.o lose.o
src_files = foo.raw bar.c lose.c

all: $(obj_files)
# PHONY is important here: without it, implicit rules would try to build
# the executable "all", since the prerequisites are .o files.
.PHONY: all

# Ex 1: .o files come from .c files.
$(filter %.o,$(obj_files)): %.o: %.c
	echo "target: $@ prereq: $<"

# Ex 2: .result files come from .raw files.
$(filter %.result,$(obj_files)): %.result: %.raw
	echo "target: $@ prereq: $<"

# A pattern rule that creates a missing source file, empty.
%.c %.raw:
	touch $@

clean:
	rm -f $(src_files)
