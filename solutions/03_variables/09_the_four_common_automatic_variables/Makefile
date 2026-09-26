# makeling exercise: 03_variables/09_the_four_common_automatic_variables
# title: $@, $?, $^ and $<
# objective: Print the target name, the out-of-date prerequisites, every prerequisite, and the first prerequisite from one recipe.
# reference: Automatic Variables
# hint: $@ is the target being built, $^ is every prerequisite, $< is just the first of them, and $? is the ones that are newer than the target.

hey: one two
	echo "target: $@"
	echo "newer: $?"
	echo "all: $^"
	echo "first: $<"
	touch hey

one:
	touch one

two:
	touch two

clean:
	rm -f hey one two
