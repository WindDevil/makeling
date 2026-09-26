# makeling exercise: 10_functions/11_wildcard
# title: Finding files with $(wildcard)
# objective: Collect the C sources in the current directory and in the sub/ directory, and confirm that a pattern with no matches gives an empty list.
# reference: First Functions
# hint: $(wildcard pattern) expands to the sorted list of files matching the glob, and to nothing at all when nothing matches. Unlike the * in a rule, it runs as soon as the variable is expanded.

sources := $(wildcard *.h)

$(info sources=[$(sources)])
$(info count=[$(words $(sources))])
$(info none=[$(wildcard *.zzz)])
$(info nested=[$(wildcard sub/*.c)])

all:
	@echo sources: $(sources)
