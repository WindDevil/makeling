# makeling exercise: 08_variables_pt2/03_appending_recursive_vs_simply_expanded
# title: Appending to a recursive and to a simply expanded variable
# objective: Append the same text to both flavours of variable, then change the variable they both refer to, and show that only the recursive one follows the change.
# reference: Flavors and modification
# hint: += on a simply expanded variable appends the already expanded text; on a recursive variable it appends the raw text, which is expanded again on every use.

source = early

# Recursive: += appends the text $(source), expanded when used.
recursive = $(source)
recursive += $(source)

# Simply expanded: += appends the current value of $(source).
simple := $(source)
simple += $(source)

source = late

all:
	echo recursive: $(recursive)
	echo simple: $(simple)
