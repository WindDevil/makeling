# makefiling exercise: 06_fancy_rules/16_double_colon_prereqs
# title: Each double-colon rule is checked on its own
# objective: Give each :: rule its own prerequisite and its own recipe, so that make rebuilds only the rule whose prerequisite changed.
# reference: Double-Colon Rules
# hint: Every :: rule is a rule in its own right, with its own prerequisites and its own up-to-date check.  make -W one pretends one was just modified, which shows you which rule that triggers.

# Each rule has its own prerequisite, and make checks them separately.
blah:: one
	echo "rule 1"
	touch blah

blah:: one
	echo "rule 2"
	touch blah
