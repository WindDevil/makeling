# makeling exercise: 07_commands_and_execution/20_export_across_recursion
# title: Exporting a variable to a sub-make
# objective: Let the Makefile in sub/ see a variable that only the top-level Makefile defines, by exporting it before the recursive call.
# reference: Export, environments, and recursive make
# hint: A sub-make is a child process: it only inherits what make put in the environment, so the top-level variable has to be exported for sub/Makefile to read it as $(cooly) or $$cooly. Add the export.

cooly = The subdirectory can see me!
export cooly

all:
	$(MAKE) -C sub
