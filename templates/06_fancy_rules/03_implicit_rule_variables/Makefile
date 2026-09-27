# makefiling exercise: 06_fancy_rules/03_implicit_rule_variables
# title: The variables behind the built-in rule
# objective: Set CC, CFLAGS and CPPFLAGS so the built-in compile rule builds blah.o with exactly those flags, and read the command with make -n.
# reference: Implicit Rules
# hint: The built-in rule for n.o expands to $(CC) $(CFLAGS) $(CPPFLAGS) -c -o $@ $<.  Run make -n blah.o to see that line without executing it, then run it for real.

# The built-in C compile rule is
#   $(CC) $(CFLAGS) $(CPPFLAGS) -c -o $@ $<
CC = cc
CFLAGS = -Wall -g
# TODO: no preprocessor flag is set

# No recipe here: make supplies one from the variables above.
blah.o:
