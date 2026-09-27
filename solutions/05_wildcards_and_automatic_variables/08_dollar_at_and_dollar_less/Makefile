# makefiling exercise: 05_wildcards_and_automatic_variables/08_dollar_at_and_dollar_less
# title: $@ is the target, $< is the first prerequisite
# objective: Copy the first prerequisite onto the target while printing both $@ and $< from the recipe.
# reference: Automatic Variables
# hint: $@ is the name of the target being built and $< is the first prerequisite. $< is the one to use in a rule that has a single source file.

greeting.txt: message.txt
	@echo target = $@
	@echo first prerequisite = $<
	@cp $< $@
