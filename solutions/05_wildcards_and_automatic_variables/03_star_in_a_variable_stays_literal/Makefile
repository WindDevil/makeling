# makeling exercise: 05_wildcards_and_automatic_variables/03_star_in_a_variable_stays_literal
# title: A bare * in a variable is not a wildcard
# objective: Contrast thing_wrong := *.o with thing_right := $(wildcard *.o) and observe what make does with each one as a prerequisite.
# reference: * Wildcard
# hint: Assigning *.o to a variable copies the two characters, it does not look at the filesystem. A prerequisite that is literally *.o has to be built, and make does not know how.

# Don't do this! '*' is not expanded in a variable definition.
thing_wrong := *.o
thing_right := $(wildcard *.o)

report:
	@echo wrong: [$(thing_wrong)]
	@echo right: [$(thing_right)]

one: $(thing_wrong)
	@echo one ran

three: $(thing_right)
	@echo three ran
