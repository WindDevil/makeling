# makeling exercise: 05_wildcards_and_automatic_variables/11_dollar_star_in_a_pattern_rule
# title: $* in a pattern rule is the stem
# objective: Write a pattern rule that copies %.txt to %.backup and prints the stem it matched.
# reference: Automatic Variables
# hint: A pattern rule has a % in its target. That % matches a piece of the target name, and the matched piece is the stem, available as $*. The % in the prerequisite stands for the same stem.

%.backup: %.txt
	@echo target = $@
	@echo stem = $*
	@cp $< $@

all: a.backup b.backup
	@echo all: $^
