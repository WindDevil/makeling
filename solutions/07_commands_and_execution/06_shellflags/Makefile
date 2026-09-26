# makeling exercise: 07_commands_and_execution/06_shellflags
# title: .SHELLFLAGS decides how the shell is called
# objective: Make a recipe line stop at its first failing command by adding -e to .SHELLFLAGS, and see what the default -c does instead.
# reference: Default Shell
# hint: make calls $(SHELL) with $(.SHELLFLAGS), which is just -c by default. Add -e to it and a line like 'false; touch marker' stops after the failure instead of reaching the touch.

.SHELLFLAGS := -ec

all:
	@echo "shell flags: $(.SHELLFLAGS)"
	false; touch carried_on.marker
