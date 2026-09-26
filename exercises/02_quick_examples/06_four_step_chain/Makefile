# makeling exercise: 02_quick_examples/06_four_step_chain
# title: A four-step chain
# objective: Extend the build with a fourth rule, so that blah.c is copied from source.txt, which is itself written by a recipe.
# reference: More quick examples
# hint: Every step needs a rule and a prerequisite that points at the step before it. source.txt comes first, then blah.c, blah.o and blah.

blah: blah.o
	cc blah.o -o blah

blah.o: blah.c
	cc -c blah.c -o blah.o

blah.c:
	cp source.txt blah.c

source.txt:
	echo "int main() { return 0; }" > source.txt
