# makeling exercise: 04_targets/09_all_and_clean
# title: all first, clean last
# objective: Keep all as the first rule and clean at the bottom, so that a bare make builds and make all clean builds then removes.
# reference: The all target
# hint: The first rule in the file is the default goal. clean is not a prerequisite of anything, so it only runs when it is named.

all: one two

one:
	echo "one" > one

two:
	echo "two" > two

clean:
	rm -f one two
