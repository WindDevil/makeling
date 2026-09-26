# makeling exercise: 05_wildcards_and_automatic_variables/09_dollar_caret_and_dollar_question
# title: $^ lists every prerequisite, $? only the newer ones
# objective: Build a target from two prerequisites and show that $^ names both while $? names only the one that has been touched since.
# reference: Automatic Variables
# hint: $^ is the whole prerequisite list, in the order it was written. $? is the subset of those prerequisites whose modification time is newer than the target's.

hey: one two
	@echo all prerequisites = $^
	@echo newer prerequisites = $?
	@touch hey

one:
	@touch one

two:
	@touch two
