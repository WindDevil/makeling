# makeling exercise: 07_commands_and_execution/03_one_shell_per_line
# title: Each recipe line runs in its own shell
# objective: Prove that a cd on one recipe line does not reach the next line, and that joining two commands with a semicolon does.
# reference: Command Execution
# hint: make hands every recipe line to its own shell, so a cd or a shell variable is forgotten as soon as the line ends. Put both commands on one line to keep them in the same shell.

all:
	@mkdir -p deeper
	cd deeper
	@pwd
	cd deeper
	@pwd
