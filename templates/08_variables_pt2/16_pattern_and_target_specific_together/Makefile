# makefiling exercise: 08_variables_pt2/16_pattern_and_target_specific_together
# title: Target-specific beats pattern-specific
# objective: Let a pattern give every .o file a mode, then give one of them its own value, and leave a third target with neither.
# reference: Pattern-specific variables
# hint: Both forms can be in the file at once; the one naming the exact target takes precedence over the one matching the pattern.

%.o: mode = pattern

foo.o: mode = pattern

foo.o:
	echo foo.o uses $(mode)

bar.o:
	echo bar.o uses $(mode)

plain:
	echo plain uses [$(mode)]
