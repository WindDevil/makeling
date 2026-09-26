# makeling exercise: 08_variables_pt2/09_override_wins
# title: override beats the command line
# objective: Force one variable to keep the Makefile's own value no matter what the command line says, while the variable next to it is still replaceable.
# reference: Command line arguments and override
# hint: Put override in front of the assignment. Assignments without it keep losing to the command line, which is exactly what the second variable should do.

# override wins over a value given on the command line.
mode = release
# A plain assignment would lose here.
plain = from the Makefile

all:
	echo mode is $(mode)
	echo plain is $(plain)
