# makeling exercise: 09_conditionals/08_ifdef_and_ifndef
# title: ifdef and ifndef
# objective: Report that foo is defined even though its value is a reference to the empty variable bar, and that bar itself is not.
# reference: Check if a variable is defined
# hint: ifdef and ifndef take a variable name, not a $(...) reference. foo was assigned something, so ifdef foo is true; bar was assigned the empty string, so ifndef bar is true.

bar =
foo = $(bar)

all:
ifdef foo
	echo "foo is defined"
endif
ifndef bar
	echo "but bar is not"
endif
