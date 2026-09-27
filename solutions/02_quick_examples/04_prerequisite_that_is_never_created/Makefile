# makefiling exercise: 02_quick_examples/04_prerequisite_that_is_never_created
# title: A prerequisite that is never created
# objective: Make some_file depend on other_file, a target whose recipe never creates a file, so that both recipes run every single time.
# reference: More quick examples
# hint: make decides a target is out of date when a prerequisite is missing or newer than it. other_file stays missing forever, so some_file can never be up to date.

some_file: other_file
	echo "This will always run, and runs second"
	touch some_file

other_file:
	echo "This will always run, and runs first"
