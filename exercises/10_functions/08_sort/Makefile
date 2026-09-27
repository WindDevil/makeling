# makefiling exercise: 10_functions/08_sort
# title: $(sort) sorts and removes duplicates
# objective: Merge the two lists of sources into one alphabetical list without repeating a.c, and count the result.
# reference: First Functions
# hint: $(sort list) returns the words sorted, and drops every duplicate. It is the shortest way to merge two lists into a set.

src := b.c a.c
gen := c.c a.c

combined := $(src) $(gen)

$(info combined=[$(combined)])
$(info count=[$(words $(combined))])

all:
	@echo $(combined)
