# makefiling exercise: 11_other_features/13_delete_on_error
# title: Delete the target of a failed rule
# objective: Switch on DELETE_ON_ERROR so that a rule which fails halfway leaves no half written target behind.
# reference: .delete_on_error
# hint: The declaration is a target line with no recipe: .DELETE_ON_ERROR:, starting in column one. It applies to every rule in the makefile, not only to the rule beneath it.

.DELETE_ON_ERROR:

all: one two

one:
	touch one
	false

two:
	touch two
	false
