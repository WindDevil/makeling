# makefiling exercise: 08_variables_pt2/07_substitution_references
# title: Substitution references
# objective: Turn a list of object files into the matching source files with the suffix shorthand and with the explicit pattern form.
# reference: Flavors and modification
# hint: $(objects:.o=.c) swaps the suffix of every word that has it. $(objects:%.o=%.c) is the same idea written as a pattern, where the % carries the part of the word in front of .o.

objects := a.o b.o l.a c.o

# The suffix shorthand: every word ending in .o loses it and gains .c.
sources := $(objects:.o=.c)
# The same substitution written with an explicit pattern.
via_pattern := $(objects:%.o=%.c)
# The long form of the same thing.
via_patsubst := $(patsubst %.o,%.c,$(objects))

all:
	echo sources: $(sources)
	echo via_pattern: $(via_pattern)
	echo via_patsubst: $(via_patsubst)
