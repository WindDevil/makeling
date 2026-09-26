# makeling exercise: 11_other_features/03_include_optional
# title: An include that may not exist yet
# objective: Read deps.mk when it is there and carry on when it is not, so a fresh checkout still builds.
# reference: Include Makefiles
# hint: A leading dash on the include line tells make that a missing file is not an error. Without it make tries to build the missing file and stops when no rule can.

-include deps.mk

report: notes.txt
	cat notes.txt > report
