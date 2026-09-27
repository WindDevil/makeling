# makefiling exercise: 03_variables/08_substitution_reference
# title: Substituting one suffix for another
# objective: Turn a list of object files into the matching source list with the $(var:suffix=replacement) shorthand.
# reference: String Substitution
# hint: $(foo:.o=.c) rewrites the ending .o of every word that has one, in place and in order. The suffix is a plain ending, not a pattern, so a word that ends differently is left alone.

foo := a.o b.o l.a c.o

sources := $(foo:.c=.o)
elsewhere := $(foo:.a=.c)

all:
	echo "sources: $(sources)"
	echo "elsewhere: $(elsewhere)"
