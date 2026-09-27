# makefiling exercise: 08_variables_pt2/05_spaces_and_the_null_string
# title: Spaces at the ends of an assignment
# objective: Build a value that ends in three spaces and a variable holding exactly one space, using the empty variable as the trick.
# reference: Flavors and modification
# hint: Spaces before the = are stripped but spaces at the end of the line are kept, comment or not. Set an empty variable and put a space before the # when you need one space.

# The three spaces before the comment are part of the value.
with_spaces = hello   # three spaces live here
after = $(with_spaces)there

nullstring =
space = $(nullstring) # one space, thanks to the space before the comment

all:
	echo "$(after)"
	echo start"$(space)"end
