# makefiling exercise: 11_other_features/08_vpath_variable
# title: VPATH searches for every prerequisite
# objective: Point VPATH at both directories that hold prerequisites, so blah.h and extra.txt are found without a vpath pattern.
# reference: The vpath Directive
# hint: VPATH is a variable listing directories, separated by spaces or colons, and it applies to every prerequisite. Naming only the first directory leaves the second file unfindable.

VPATH = headers libs

some_binary: blah.h extra.txt
	cat $^ > some_binary
