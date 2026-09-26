# makeling exercise: 09_conditionals/02_branches_choose_rules
# title: A conditional chooses which rules exist
# objective: Let the conditional decide which rule the Makefile contains, so that make debug builds when MODE is debug and make release builds when MODE is release.
# reference: Conditional if/else
# hint: Conditionals are not recipe text: they decide which lines of the file make reads at all. Put the ifeq around the whole rules, so that the target that is not selected does not exist.

MODE = debug

debug:
ifeq ($(MODE),debug)
	echo "building debug"
else
	echo "building release"
endif
