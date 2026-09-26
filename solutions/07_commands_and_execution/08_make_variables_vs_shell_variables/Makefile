# makeling exercise: 07_commands_and_execution/08_make_variables_vs_shell_variables
# title: A make variable is not a shell variable
# objective: Give the shell a variable of its own in a recipe line, and see why $(...) and $$... are not interchangeable.
# reference: Double dollar sign
# hint: make expands $(name) itself before the shell ever sees the line. Write $$name when the shell - not make - is supposed to read the variable; with a single $ make eats the name and the shell gets the leftovers.

make_var = I am a make variable

all:
	sh_var='I am a shell variable'; echo $$sh_var
	echo $(make_var)
