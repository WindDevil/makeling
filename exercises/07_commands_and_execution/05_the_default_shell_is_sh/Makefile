# makeling exercise: 07_commands_and_execution/05_the_default_shell_is_sh
# title: The shell is the SHELL variable
# objective: Look at which program runs your recipe lines, and change it by giving make a different SHELL.
# reference: Default Shell
# hint: make runs recipes with /bin/sh unless the variable SHELL says otherwise. The shell's own $0 is the name of the program running the line; SHELL can be set in the Makefile or on the command line.

which_shell:
	@echo "SHELL is: $(SHELL)"
	@echo "this line was run by: $${0}"
