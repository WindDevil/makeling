# makefiling exercise: 07_commands_and_execution/18_exported_variables
# title: Only exported variables reach the shell
# objective: Print a make variable and a shell variable side by side, and show that environment variables are make variables from the start.
# reference: Export, environments, and recursive make
# hint: A variable defined in the Makefile lives only inside make until you export it, which is what puts it in the environment of every recipe line. Variables that were already in the environment arrive as make variables automatically.

one = this will only work locally
export two = we can run subcommands with this

all:
	@echo "make variable one: [$(one)]"
	@echo "shell variable one: [$$one]"
	@echo "make variable two: [$(two)]"
	@echo "shell variable two: [$$two]"

from_environment:
	@echo "make variable: [$(SHELL_ENV_VAR)]"
	@echo "shell variable: [$$SHELL_ENV_VAR]"
