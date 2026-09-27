# makefiling exercise: 09_conditionals/06_spaces_in_the_values
# title: Commas separate, spaces do not
# objective: Compare a value that itself contains a space, and rely on the space after the comma being ignored.
# reference: Conditional if/else
# hint: The comma is the only separator ifeq knows about, so the space in the tutorial's 'ifeq ($(foo), ok)' is decoration. A space that belongs to a value is compared like any other character.

name = Grace Hopper
lang = c

all:
ifeq ($(name),Grace)
	echo "a space inside a value is compared"
endif
ifeq ($(lang), c)
	echo "the space after the comma is ignored"
endif
