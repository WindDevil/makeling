# makeling exercise: 09_conditionals/04_both_sides_expanded
# title: ifeq expands both arguments
# objective: Compare two variables whose values are themselves variable references, so that the branch is taken.
# reference: Conditional if/else
# hint: ifeq expands its two arguments before comparing them, so a variable that holds a reference to another one is followed. Writing the argument without $(...) compares it as literal text.

flavour = chocolate
choice = $(flavour)
default = $(choice)

all:
ifeq ($(default),$(flavour))
	echo "left and right are both expanded"
else
	echo "the two sides differ"
endif
