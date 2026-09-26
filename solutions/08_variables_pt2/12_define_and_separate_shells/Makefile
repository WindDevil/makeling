# makeling exercise: 08_variables_pt2/12_define_and_separate_shells
# title: Each line of a command list is its own shell
# objective: Keep a one-line variable that exports and prints in a single shell, and a define block that exports and prints in two, and show which one actually prints the value.
# reference: List of commands and define
# hint: A semicolon keeps two commands in one shell, so the export is still visible. Two lines of a define become two recipe lines, and each recipe line gets a fresh shell.

one = export blah="I was set!"; echo $$blah

define two
export blah="I was set!"
echo $$blah
endef

all:
	@echo "one is a single line, so its shell keeps the export"
	@$(one)
	@echo "two spans two lines, so the export is gone by the second one"
	@$(two)
