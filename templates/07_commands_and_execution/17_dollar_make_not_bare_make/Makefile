# makeling exercise: 07_commands_and_execution/17_dollar_make_not_bare_make
# title: Use $(MAKE), never a bare make
# objective: Show what breaks when a recipe calls make instead of $(MAKE): the second make loses the flags and make -n no longer descends.
# reference: Recursive use of make
# hint: make only runs a recipe line itself (rather than merely printing it) under -n when the line mentions $(MAKE), and it hands its flags to the sub-make through MAKEFLAGS. Replace the bare make with $(MAKE).

all:
	@echo "top level, MAKELEVEL=$(MAKELEVEL)"
	@echo "top level flags: [$(MAKEFLAGS)]"
	make -C sub
