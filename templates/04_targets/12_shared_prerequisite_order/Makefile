# makefiling exercise: 04_targets/12_shared_prerequisite_order
# title: all builds a shared prerequisite once
# objective: Give one and two the same prerequisite base so that make builds base first and only once.
# reference: The all target
# hint: make walks all's prerequisites left to right and depth first, and it never builds the same target twice in one run.

all: one two

one:
	echo "one after base"

two: base
	echo "two after base"

base:
	echo "base first"
