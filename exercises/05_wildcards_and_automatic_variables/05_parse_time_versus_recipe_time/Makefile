# makeling exercise: 05_wildcards_and_automatic_variables/05_parse_time_versus_recipe_time
# title: make globs at parse time, the shell globs at recipe time
# objective: Have one rule create a .c file and another report both the parse-time $(wildcard *.c) and the recipe-time shell glob.
# reference: * Wildcard
# hint: make reads the whole file before it runs a single recipe, so $(wildcard) cannot see a file that a prerequisite creates later. The shell, by contrast, expands *.c only when the recipe line runs.

gen:
	@echo "int main(void) { return 0; }" > new.c

report: gen
	@echo "parse-time wildcard: *.c"
	@echo "recipe-time shell:" *.c
