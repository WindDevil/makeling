# makeling exercise: 04_targets/05_all_from_a_variable
# title: Build the all rule from a variable
# objective: Keep the list of targets in a variable and let all expand it instead of writing the names out.
# reference: The all target
# hint: A variable is expanded with $(NAME). Writing the bare word NAME makes make look for a file of that name instead.

TARGETS := one two three

all: $(TARGETS)

one:
	@echo "building one"

two:
	@echo "building two"

three:
	@echo "building three"

list:
	@echo "all depends on: $(TARGETS)"
