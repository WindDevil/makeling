# makeling exercise: 06_fancy_rules/15_single_colon_warning
# title: What a single colon does instead
# objective: Repeat the target with single colons and confirm what make says: it warns and keeps only the last recipe.
# reference: Double-Colon Rules
# hint: Written with one colon, the second rule overrides the first and make prints a warning on stderr.  Compare that with the double-colon version, where both recipes run.

all: blah

blah::
	echo "first"

blah::
	echo "second"
