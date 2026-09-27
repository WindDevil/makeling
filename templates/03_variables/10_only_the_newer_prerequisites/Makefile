# makefiling exercise: 03_variables/10_only_the_newer_prerequisites
# title: $? lists only what is out of date
# objective: Make one of two prerequisites newer than the target and watch $? shrink while $^ stays the same.
# reference: Automatic Variables
# hint: $^ and $< never change; $? reports only the prerequisites whose timestamp is newer than the target's, which is the list you would hand to a compiler.

hey: one two
	echo "newer: $^"
	echo "all: $^"
	echo "first: $<"
	touch hey

one:
	touch one

two:
	touch two
