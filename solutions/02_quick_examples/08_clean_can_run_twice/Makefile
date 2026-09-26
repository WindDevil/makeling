# makeling exercise: 02_quick_examples/08_clean_can_run_twice
# title: clean removes what make built
# objective: Add a clean target that deletes some_file and can be run again when there is nothing left to delete.
# reference: Make clean
# hint: clean is an ordinary target: it is not first, and nothing depends on it, so it only runs when you ask for it. Give rm the -f flag so that a second clean is not an error.

some_file:
	touch some_file

clean:
	rm -f some_file
