# makefiling exercise: 06_fancy_rules/10_static_pattern_filter_out
# title: Dropping targets with $(filter-out ...)
# objective: Build only the objects that are not test.o, using $(filter-out) in front of a static pattern rule.
# reference: Static Pattern Rules and Filter
# hint: $(filter-out test.o,$(objects)) is $(objects) with test.o removed, so the rule you attach it to never mentions test.o.  $^ in the link recipe then holds just the production objects.

objects = main.o util.o test.o

# filter-out removes the words in front of the comma from the list.
production = $(filter test.o,$(objects))

all: $(production)
	echo "link: $^"

# Only the objects left in $(production) get this rule.
$(production): %.o: %.c
	echo "compile: $< -> $@"

clean:
	rm -f *.o
