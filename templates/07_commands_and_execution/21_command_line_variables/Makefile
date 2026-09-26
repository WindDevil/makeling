# makeling exercise: 07_commands_and_execution/21_command_line_variables
# title: Variables on the command line, and several goals
# objective: Give MODE a default in the Makefile, override it with make MODE=..., and ask for several goals in one run.
# reference: Arguments to make
# hint: A value written on the command line wins over the Makefile's own assignment and is passed into the environment of every recipe. Several goals on one command line are run left to right.

all:
	@echo "mode: $(MODE)"
	@echo "mode in the shell: [$$MODE]"

clean:
	@echo "cleaning"

run:
	@echo "running"

test:
	@echo "testing"
