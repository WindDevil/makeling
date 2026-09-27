# makefiling exercise: 10_functions/10_addprefix_addsuffix_join
# title: Building new names with $(addprefix), $(addsuffix) and $(join)
# objective: Turn the two names main util into object files, then put them under src/, and pair the prefixes src/ and build/ with two files.
# reference: First Functions
# hint: $(addsuffix x,list) appends to every word, $(addprefix x,list) prepends to every word, and you can nest them. $(join list1,list2) glues the words together pairwise.

names := main util

$(info objects=[$(addsuffix .o,$(names))])
$(info paths=[$(addprefix src/,$(addsuffix .o,$(names)))])
$(info joined=[$(join src/ build/,a.c b.c)])
$(info short=[$(join a b c,1 2)])

all:
	@echo $(paths)
