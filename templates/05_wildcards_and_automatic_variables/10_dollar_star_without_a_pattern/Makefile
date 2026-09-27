# makefiling exercise: 05_wildcards_and_automatic_variables/10_dollar_star_without_a_pattern
# title: $* in an explicit rule is the target minus a known suffix
# objective: Print $* for a target ending in .o, for a target ending in .txt and for a target with no suffix at all.
# reference: Automatic Variables
# hint: In an explicit rule $* is only the stem if the target ends in one of make's known suffixes, such as .o or .c. For any other name there is no stem to report and $* is empty.

program.o: input.c
	@echo object target: stem=[$@] target=[$@]

notes.txt: input.c
	@echo text target: stem=[$*] target=[$@]

release: input.c
	@echo suffixless target: stem=[$*] target=[$@]
