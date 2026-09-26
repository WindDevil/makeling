# makeling exercise: 10_functions/20_filter_out
# title: Removing words with $(filter-out)
# objective: Drop the headers from files, drop everything starting with test from objects, and nest the two ideas to keep only the objects that are left.
# reference: The filter function
# hint: $(filter-out pattern,list) is $(filter) with the sense reversed: it keeps the words that do not match. Filters can be nested, so $(filter %.o,$(filter-out test%,$(objects))) removes the test objects first and then keeps the .o ones.

files := a.c b.h c.c d.h
objects := test_a.o a.o test_b.o b.o notes.txt

kept := $(filter %.o,$(filter-out test%,$(objects)))

$(info without_headers=[$(filter-out %.h,$(files))])
$(info candidates=[$(filter-out test%,$(objects))])
$(info kept=[$(kept)])

all:
	@echo final: $(kept)
