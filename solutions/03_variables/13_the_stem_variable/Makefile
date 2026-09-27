# makefiling exercise: 03_variables/13_the_stem_variable
# title: $* is the stem
# objective: Print $* for a target that ends in a known suffix and for one that does not.
# reference: Automatic Variables
# hint: $* is the target name with a known suffix removed, so foo.o gives foo. A target without a recognised suffix, like prog, gives an empty $*.

all: foo.o prog

foo.o: foo.c
	echo "stem of foo.o: [$*]"
	touch $@

prog: prog.c
	echo "stem of prog: [$*]"
	touch $@
