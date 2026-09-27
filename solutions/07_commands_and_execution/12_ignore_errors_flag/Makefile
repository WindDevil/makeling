# makefiling exercise: 07_commands_and_execution/12_ignore_errors_flag
# title: make -i ignores every error
# objective: Compare a plain make, which stops at the failing line, with make -i, which ignores it and carries on.
# reference: Error handling with -k, -i, and -
# hint: make -i is the command line version of a - on every line. The recipe needs a command that really fails: 'false' exits non-zero, while a command that merely prints the word false does not.

all:
	@echo "make flags: [$(MAKEFLAGS)]"
	false
	@echo "make carried on regardless"
