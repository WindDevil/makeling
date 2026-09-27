# makefiling exercise: 07_commands_and_execution/10_error_stops_make
# title: make gives up at the first failing command
# objective: Run a command that fails and confirm that make stops right there: the rest of the recipe and the other target must not run.
# reference: Error handling with -k, -i, and -
# hint: A recipe line that exits non-zero ends the whole make run, so the line after it and the goal's second prerequisite never happen. Your first target currently shrugs the failure off.

all: first second

first:
	false
	touch first.made

second:
	touch second.made
