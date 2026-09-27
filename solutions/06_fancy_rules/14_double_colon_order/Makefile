# makefiling exercise: 06_fancy_rules/14_double_colon_order
# title: Two double-colon rules, two recipes
# objective: Define the same target twice with :: so that both recipes run, in the order they appear in the file.
# reference: Double-Colon Rules
# hint: With a single colon the second definition would replace the first.  A double colon says these are separate rules for one target, and make runs each rule's recipe in turn.

all: blah

blah::
	echo "hello"

blah::
	echo "hello again"
