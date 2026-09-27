# makefiling exercise: 03_variables/11_one_rule_two_targets
# title: One rule, several targets
# objective: Write a single rule for f1.o and f2.o and let $@ name the output of each run.
# reference: Automatic Variables
# hint: When a rule lists several targets, make runs the recipe once per target with $@ set to that target. That is what lets the same recipe build both files.

all: f1.o f2.o

f1.o f2.o:
	echo "building $@"
	touch $@
