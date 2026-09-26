# makeling exercise: 09_conditionals/01_ifeq_else
# title: Pick a recipe line with ifeq/else
# objective: Branch on the value of foo so that make prints the matching message for both the file's value and an override on the command line.
# reference: Conditional if/else
# hint: The else directive separates the two branches and endif closes the conditional. A make with an override needs the recipe that runs when the comparison fails, and that recipe is missing.

foo = ok

all:
ifeq ($(foo), ok)
	echo "foo equals ok"
else
	echo "foo is not ok"
endif
