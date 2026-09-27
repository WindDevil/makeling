# makefiling exercise: 06_fancy_rules/12_pattern_rule_no_prereq
# title: A pattern rule with no prerequisites
# objective: Add a %.c rule that has no prerequisite pattern, so make can always create a missing .c file -- empty.
# reference: Pattern Rules
# hint: A pattern rule whose target has no counterpart in the prerequisites can be used for any matching file, and there is nothing to check first.  touch $@ creates the needed file and leaves it empty.

# A pattern rule that has no pattern in the prerequisites.  This just
# creates empty .c files when they are needed.
%.c:
	touch $@

stub: stub.c
	echo "stub.c is ready"
