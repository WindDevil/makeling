# makeling exercise: 02_quick_examples/01_three_step_chain
# title: Generate, compile, link
# objective: Build blah in three steps: blah from blah.o, blah.o from blah.c, and a rule that creates blah.c itself.
# reference: More quick examples
# hint: Work backwards from the goal: blah needs blah.o, blah.o needs blah.c, and the rule for blah.c has no prerequisites at all, so its recipe is the first one make runs.

blah.o: blah.c
	cc -c blah.c -o blah.o # Runs second

blah: blah.o
	cc blah.o -o blah # Runs third

# Typically blah.c would already exist, but I want to limit any additional required files
blah.c:
	echo "int main() { return 0; }" > blah.c # Runs first
