# makefiling exercise: 02_quick_examples/02_delete_a_source_reruns_everything
# title: Deleting a source re-runs the whole chain
# objective: Keep the three rules in place, then watch what happens when the generated blah.c is deleted: every recipe runs again.
# reference: More quick examples
# hint: blah.o must list blah.c as a prerequisite, or make never notices that the file is gone. Only a prerequisite makes make look at a file that is missing.

blah: blah.o
	cc blah.o -o blah # Runs third

blah.o:
	cc -c blah.c -o blah.o # Runs second

# Typically blah.c would already exist, but I want to limit any additional required files
blah.c:
	echo "int main() { return 0; }" > blah.c # Runs first
