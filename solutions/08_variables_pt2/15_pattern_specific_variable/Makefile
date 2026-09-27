# makefiling exercise: 08_variables_pt2/15_pattern_specific_variable
# title: A variable that belongs to a pattern
# objective: Attach a variable to every target ending in .c, so that blah.c sees it and other targets do not.
# reference: Pattern-specific variables
# hint: Write %.c: variable = value. The target has to match the pattern for the variable to apply, so a pattern of %.o would leave blah.c without it.

%.c: compiler = clang

blah.c:
	echo blah.c is built by $(compiler)

other:
	echo other is built by [$(compiler)]
