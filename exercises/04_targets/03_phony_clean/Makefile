# makefiling exercise: 04_targets/03_phony_clean
# title: A file that shadows clean
# objective: Declare clean phony so that the stray file called clean does not make make skip the recipe.
# reference: Make clean
# hint: make compares the target name with the filesystem. .PHONY: clean tells make that clean is a name to run, never a file to check.

some_file:
	echo "content" > some_file

clean:
	rm -f some_file
