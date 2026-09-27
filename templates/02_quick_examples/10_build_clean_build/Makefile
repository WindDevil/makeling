# makefiling exercise: 02_quick_examples/10_build_clean_build
# title: Build, clean, build again
# objective: Complete the Makefile with a clean target that removes everything make created, so the same three recipes can run from scratch again.
# reference: Make clean
# hint: clean should delete every file the other rules produce, including the generated blah.c. After it runs, make must be able to rebuild the program from nothing.

blah: blah.o
	cc blah.o -o blah # Runs third

blah.o: blah.c
	cc -c blah.c -o blah.o # Runs second

# Typically blah.c would already exist, but I want to limit any additional required files
blah.c:
	echo "int main() { return 0; }" > blah.c # Runs first

# Every file above is produced by this Makefile, so clean removes all of them.
clean:
	rm -f blah blah.o
