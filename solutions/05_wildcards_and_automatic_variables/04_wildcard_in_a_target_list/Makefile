# makeling exercise: 05_wildcards_and_automatic_variables/04_wildcard_in_a_target_list
# title: An empty wildcard leaves a rule with no prerequisites
# objective: Write all: $(wildcard *.o) so that it still works when no object file exists, and see why a bare *.o in the same place does not.
# reference: * Wildcard
# hint: When $(wildcard) matches nothing the prerequisite list is simply empty and the rule is still valid. The string *.o written directly into the rule is not: make tries to build a file with that name.

# No .o files exist, so this list is empty.
objects := $(wildcard *.o)

all: $(objects)
	@echo objects: [$(objects)]
	@echo prerequisites of all: [$^]

bare: *.o
	@echo bare ran
