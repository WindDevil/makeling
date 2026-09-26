# makeling exercise: 09_conditionals/10_empty_means_stripped
# title: Check whether a variable is empty
# objective: Use the $(strip) idiom to recognise that foo holds only a space, and still detect a variable that was never given a value.
# reference: Check if a variable is empty
# hint: The space before the # is part of the value, so $(foo) is a single space and does not equal the empty string. $(strip) removes the surrounding whitespace before the comparison.

nullstring =
foo = $(nullstring) # end of line; there is a space here

all:
ifeq ($(foo),)
	echo "foo is empty after being stripped"
else
	echo "foo is not empty"
endif
ifeq ($(foo),)
	echo "foo is empty without stripping"
else
	echo "without strip, foo holds only a space"
endif
ifeq ($(nullstring),)
	echo "nullstring doesn't even have spaces"
endif
