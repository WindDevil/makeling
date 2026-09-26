# makeling exercise: 06_fancy_rules/08_more_specific_match
# title: explicit rules win over pattern rules
# objective: Keep the explicit rule for all.c so that it is written by hand, while the %.c pattern rule touches an empty file for the rest.
# reference: Static Pattern Rules
# hint: make prefers the more specific match: a rule that names all.c exactly beats a pattern rule that could also match it.  Touch $@ creates an empty file, so all.c needs its own rule.

all: all.c foo.c
	echo "built: $^"

# TODO: all.c needs a rule of its own here

# A pattern rule with no prerequisites: any other .c file is created empty.
%.c:
	touch $@
