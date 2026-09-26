# makeling exercise: 08_variables_pt2/02_simply_expanded_appending
# title: A variable cannot be extended from itself with =
# objective: Extend one variable with its own old value plus a suffix, so that make prints the combined value instead of refusing to run.
# reference: Flavors and modification
# hint: := expands the right-hand side before assigning, so ${one} is the old value. With = the reference is stored unevaluated and the variable ends up referring to itself.

one = hello

# := expands ${one} right now, so this reads "hello" + " there".
one := ${one} there

all:
	echo $(one)
