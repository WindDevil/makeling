# makeling exercise: 07_commands_and_execution/16_recursive_make
# title: Calling the Makefile in a subdirectory
# objective: Have the top-level Makefile build the project in sub/ by asking $(MAKE) to read that directory's Makefile.
# reference: Recursive use of make
# hint: A recipe line that runs $(MAKE) -C sub starts a second make in sub/; it announces itself with make[1]: Entering directory and bumps MAKELEVEL to 1. Add that line to the all recipe.

all:
	@echo "top level, MAKELEVEL=$(MAKELEVEL)"
	$(MAKE) -C sub
