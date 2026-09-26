# makeling exercise: 06_fancy_rules/02_generate_source_with_rule
# title: A rule that writes the C source
# objective: Let make create blah.c with a rule of your own, then watch the built-in rules compile and link it using CFLAGS.
# reference: Implicit Rules
# hint: blah.c does not exist yet, so it needs a rule that writes it; make still contributes the compile and link recipes itself.  CFLAGS is handed straight to the built-in compile rule.

CFLAGS = -g

# Implicit rule #1: blah is built from blah.o by the C linker rule.
# Implicit rule #2: blah.o is built from blah.c by the C compile rule,
# because blah.c can be made.
blah: blah.o

# TODO: nothing here knows how to create blah.c

clean:
	rm -f blah*
