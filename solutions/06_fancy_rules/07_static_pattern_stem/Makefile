# makefiling exercise: 06_fancy_rules/07_static_pattern_stem
# title: The stem goes into the prerequisite pattern
# objective: Turn a list of .txt files into .raw ones with a static pattern rule, and print the stem that %.txt matched.
# reference: Static Pattern Rules
# hint: $* is the stem: for alpha.txt matched by %.txt it is alpha, and the same stem replaces the % in the prerequisite pattern %.raw.  The rule needs both pattern lines to line up.

files = alpha.txt beta.txt

all: $(files)
	echo "built: $^"

# alpha.txt matches %.txt, so the stem is "alpha" and the prerequisite
# pattern %.raw turns into alpha.raw.
$(files): %.txt: %.raw
	echo "target $@ from prereq $< (stem $*)"
	cp $< $@
