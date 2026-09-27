# makefiling exercise: 04_targets/04_all_builds_everything
# title: The all target builds everything
# objective: List one, two and three in the all rule so that a bare make builds all three files.
# reference: The all target
# hint: all is a normal target whose prerequisites are the other targets. Because it comes first it is what a bare make runs.

all: one two

one:
	touch one
two:
	touch two
three:
	touch three

clean:
	rm -f one two three
