# makeling exercise: 05_wildcards_and_automatic_variables/01_wildcard_function_in_a_variable
# title: $(wildcard) expands at parse time
# objective: Collect every .c file with $(wildcard *.c) and use the resulting list as the prerequisites of a target.
# reference: * Wildcard
# hint: The wildcard function is the safe way to use *: it runs while make reads the file and returns the matching names, separated by spaces.

sources := $(wildcard *.c)

show: $(sources)
	@echo target: $@
	@echo sources: $(sources)
	@echo prereqs: $^
