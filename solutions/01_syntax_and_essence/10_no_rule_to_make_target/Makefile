# makefiling exercise: 01_syntax_and_essence/10_no_rule_to_make_target
# title: No rule to make target
# objective: Give broken a prerequisite that nothing creates, and watch make refuse to build it.
# reference: The essence of Make
# hint: A prerequisite must either exist as a file or be the target of another rule. Declare missing.txt as the prerequisite of broken to see what make says about it.

summary: notes.txt
	cat notes.txt

notes.txt:
	echo "written by the notes target" > notes.txt

broken: missing.txt
	cat missing.txt
