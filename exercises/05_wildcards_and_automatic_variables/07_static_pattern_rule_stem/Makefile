# makeling exercise: 05_wildcards_and_automatic_variables/07_static_pattern_rule_stem
# title: The stem in a static pattern rule
# objective: Use $(targets): %.out: %.raw so that each target is matched by the target pattern and the stem is substituted into the prerequisite pattern.
# reference: % Wildcard
# hint: In a static pattern rule the target pattern matches the target name and the matched stem replaces the % in the prerequisite pattern. foo.out is matched by %.out with the stem foo, so its prerequisite is foo.raw.

targets := foo.out bar.out

all: $(targets)
	@echo all: $^

$(targets): %.out: %.raw
	@echo target=[$@] stem=[$*] prereq=[$*]
	@touch $@
