# makefiling exercise: 02_quick_examples/03_touching_an_intermediate_file
# title: Touching an intermediate file rebuilds part of the chain
# objective: Give blah.o its blah.c prerequisite so that touching either file rebuilds exactly as much as it has to.
# reference: More quick examples
# hint: Touching blah.c makes it newer than blah.o, so the object is recompiled and, being newer than blah, the program is relinked. Touching blah.o alone only relinks.

blah: blah.o
	cc blah.o -o blah

blah.o:
	cc -c blah.c -o blah.o
