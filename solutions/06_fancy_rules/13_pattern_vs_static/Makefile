# makefiling exercise: 06_fancy_rules/13_pattern_vs_static
# title: Pattern rules cover targets you never listed
# objective: Replace the two hand-listed targets with a pattern rule, so that extra.out is built as well even though no rule names it.
# reference: Pattern Rules
# hint: A static pattern rule only ever applies to the targets before the colon; a pattern rule applies to any target that matches it.  %.out: %.in covers every .out file in the directory.

# A pattern rule has no target list: it applies to every .out file whose
# .in file exists, including extra.out, which is named nowhere here.
%.out: %.in
	cp $< $@

all: a.out b.out extra.out
	echo "done"
