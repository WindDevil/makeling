# makefiling exercise: 05_wildcards_and_automatic_variables/02_wildcard_empty_versus_shell_glob
# title: $(wildcard) is empty when nothing matches
# objective: Show that $(wildcard *.dat) expands to nothing while a shell that globs *.dat in a recipe leaves the pattern as it is.
# reference: * Wildcard
# hint: make runs the recipe through the shell, and /bin/sh passes an unmatched pattern through unchanged. $(wildcard) has no such rule: it returns the empty string.

present := $(wildcard *.txt)
missing := *.dat

report:
	@echo present: $(present)
	@echo missing: $(missing)
	@echo shell-glob: *.dat
	@echo shell-match: *.txt
