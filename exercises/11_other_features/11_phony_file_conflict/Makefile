# makefiling exercise: 11_other_features/11_phony_file_conflict
# title: A phony target is never up to date
# objective: Declare clean phony so that the file named clean, created by some_file, cannot stop the clean rule from running.
# reference: .phony
# hint: .PHONY: clean tells make to ignore any file with that name. Without the declaration make sees the file clean, decides the target is up to date and skips the recipe.

some_file:
	touch some_file
	touch clean

clean:
	rm -f some_file
	rm -f clean
