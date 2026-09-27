# makefiling exercise: 07_commands_and_execution/15_plan_with_dry_run
# title: make -n prints the plan without running it
# objective: Read every command a target would run with make -n, and check that the dry run really does not touch the filesystem.
# reference: Arguments to make
# hint: make -n (or --dry-run) prints the whole recipe, including the lines hidden by @, and runs none of them. Note that the plan only contains the commands make would reach, so a missing prerequisite never shows up in it.

all: report.txt
	@cat report.txt

report.txt:
	@echo "writing report" > report.txt
	@echo "report written"
