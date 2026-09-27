# makefiling exercise: 04_targets/06_multiple_targets_one_rule
# title: Several targets on one rule line
# objective: Put f1.o and f2.o on a single rule line and confirm that the recipe runs once for each target.
# reference: Multiple targets
# hint: f1.o f2.o: is shorthand for two rules with the same recipe. $@ expands to whichever target is being built.

all: f1.o f2.o

f1.o:
	echo $@
