# makeling exercise: 09_conditionals/11_whitespace_is_not_empty
# title: A value of only whitespace is not empty
# objective: Show that ifdef is true for a variable whose value is one space, while ifeq only sees it as empty once it is stripped.
# reference: Check if a variable is defined
# hint: padded holds one space, and a space is a non-empty value, so ifdef padded is true and ifeq ($(padded),) is false. Only the stripped comparison is true.

space =
padded = $(space) # the space before this comment is part of the value

all:
ifdef space
	echo "ifdef sees a non-empty value"
else
	echo "ifdef sees nothing"
endif
ifeq ($(padded),)
	echo "ifeq says padded is empty"
else
	echo "ifeq says padded is not empty"
endif
ifeq ($(strip $(padded)),)
	echo "only strip says it is empty"
endif
