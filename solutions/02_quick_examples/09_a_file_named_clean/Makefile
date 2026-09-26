# makeling exercise: 02_quick_examples/09_a_file_named_clean
# title: A file called clean stops the recipe
# objective: Make clean run even though the directory contains a stray file with the same name as the target.
# reference: Make clean
# hint: clean is not a special word in make: the target is matched against the filesystem like any other. Declare it .PHONY so make always runs the recipe.

.PHONY: clean

some_file:
	touch some_file

clean:
	rm -f some_file
