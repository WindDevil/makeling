# makeling exercise: 09_conditionals/07_ifneq
# title: ifneq runs when the values differ
# objective: Use ifneq to choose the architecture message, for both the file's value of arch and an override on the command line.
# reference: Conditional if/else
# hint: ifneq is the negation of ifeq: its text-if-true is read when the two arguments are not equal. The else branch covers the equal case.

os = linux
arch = x86

all:
ifneq ($(os),windows)
	echo "using unix paths"
endif
ifneq ($(arch),x86)
	echo "64 bit build"
else
	echo "32 bit build"
endif
