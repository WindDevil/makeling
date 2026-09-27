# makefiling exercise: 07_commands_and_execution/22_directory_flag
# title: Running make somewhere else: -C
# objective: Run the Makefile in sub/ from the top of the tree with -C, keep the directory chatter down with --no-print-directory, and rebuild an up-to-date target with -B.
# reference: Arguments to make
# hint: make -C sub changes directory before reading the Makefile, so it prints Entering/Leaving directory lines; --no-print-directory removes them. -B throws away make's timestamps and runs the recipe even when out.txt is up to date.

out.txt: source.txt
	@cp source.txt out.txt
	@echo "copied source.txt"
