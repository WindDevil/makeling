# makefiling exercise: 10_functions/02_subst_spaces_and_commas
# title: Replacing spaces and commas
# objective: Turn the list a b c into the single word a,b,c by replacing every space with a comma.
# reference: First Functions
# hint: Neither a comma nor a space is easy to write as an argument, so build them first: comma := , and space := $(empty) $(empty). Adding extra spaces around an argument makes them part of the string that is searched for or inserted.

# A comma and a space are awkward to type literally; build them from variables.
comma := ,
empty :=
space := $(empty)$(empty)

foo := a b c
joined := $(subst $(space),$(comma),$(foo))
# Watch out: the spaces around the arguments below end up in the result.
spaced := $(subst $(space), $(comma) ,$(foo))

$(info joined=[$(joined)])
$(info spaced=[$(spaced)])

all:
	@echo $(joined)
