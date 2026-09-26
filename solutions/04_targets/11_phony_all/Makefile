# makeling exercise: 04_targets/11_phony_all
# title: Stray files that shadow the aggregate
# objective: Declare all, one and two phony so that files of those names do not stop make from running the recipes.
# reference: .phony
# hint: Without .PHONY the file one is newer than nothing and make treats it as up to date. Declare every name in the aggregate that is not a real output.

.PHONY: all one two

all: one two

one:
	echo "building one"
two:
	echo "building two"
