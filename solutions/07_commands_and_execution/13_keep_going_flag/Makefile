# makefiling exercise: 07_commands_and_execution/13_keep_going_flag
# title: make -k keeps going but still fails
# objective: Build three targets where the first one fails, and tell make -k and make -i apart.
# reference: Error handling with -k, -i, and -
# hint: -k continues with the goals that can still be built and then exits non-zero because the build was not completed; -i ignores the errors entirely and exits 0. Make the first target fail for real.

all: first second third

first:
	false

second:
	touch second.made

third:
	touch third.made
