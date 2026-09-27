# makefiling exercise: 09_conditionals/09_ifdef_does_not_expand
# title: ifdef looks at the text, ifeq at the value
# objective: Show both sides of the trap: an empty variable and an undefined one compare equal, while ifdef still calls foo set.
# reference: Check if a variable is defined
# hint: ifeq expands its arguments, so $(foo) turns into nothing and an unassigned name looks exactly the same to it. ifdef expands nothing: it asks whether the text make recorded for foo is a non-empty string, and '$(bar)' is one.

bar =
foo = $(bar)
empty =
# never_set is not assigned anywhere in this file

all:
ifeq ($(foo),)
	echo "ifeq expands the value and finds it empty"
else
	echo "ifeq found something"
endif
ifeq ($(empty),$(never_set))
	echo "ifeq cannot tell an empty variable from an undefined one"
endif
ifndef foo
	echo "ifdef reads the unexpanded value and finds it set"
else
	echo "ifdef found nothing"
endif
