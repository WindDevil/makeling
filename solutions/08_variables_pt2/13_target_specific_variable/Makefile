# makeling exercise: 08_variables_pt2/13_target_specific_variable
# title: A variable that belongs to one target
# objective: Give the all target its own flavour without letting the other target see it.
# reference: Target-specific variables
# hint: Write target: variable = value before the rule. Making the assignment global instead would let every target see it.

all: flavor = vanilla

all:
	echo the all target uses $(flavor)

other:
	echo the other target sees [$(flavor)]
