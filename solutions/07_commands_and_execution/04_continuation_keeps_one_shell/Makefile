# makefiling exercise: 07_commands_and_execution/04_continuation_keeps_one_shell
# title: Shell state survives across a line continuation
# objective: Show that a shell variable set on one line is gone by the next, and keep it alive by continuing the recipe line with a backslash.
# reference: Command Execution
# hint: A make variable reaches every line, but a shell variable only lives inside the one shell that set it. Ending a line with backslash-newline keeps the next line in that same shell.

MAKE_NOTE = set in the Makefile

all:
	message="set in line one"
	echo "next line sees: [$$message]"
	message="set again"; \
	echo "continuation sees: [$$message]"
	@echo "the make variable survives anyway: [$(MAKE_NOTE)]"
