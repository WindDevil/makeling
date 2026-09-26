# makeling exercise: 08_variables_pt2/06_undefined_is_empty
# title: An undefined variable is an empty string
# objective: Append a variable that nothing defines to a flag list, and confirm it contributes nothing until a value is supplied.
# reference: Flavors and modification
# hint: $(NAME) of a variable nobody set expands to nothing at all, so appending it is harmless. Writing the name without $() makes it literal text instead.

CFLAGS := -Wall
# EXTRA_CFLAGS is never defined anywhere in this Makefile.
CFLAGS += EXTRA_CFLAGS

all:
	echo "cflags: $(CFLAGS)"
