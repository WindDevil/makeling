# makefiling exercise: 01_syntax_and_essence/08_no_prerequisites_always_runs
# title: A target with no file always runs
# objective: Write a target that has no prerequisites and creates no file, and confirm that make runs it every time.
# reference: The essence of Make
# hint: make skips a recipe only when a file with the target's name exists. A target such as stamp, whose recipe never creates stamp, is run again on every invocation.

stamp:
	echo "the stamp target ran"

report.txt:
	echo "report built" > report.txt
