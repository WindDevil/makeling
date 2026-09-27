# makefiling exercise: 06_fancy_rules/11_pattern_rule_compile
# title: A pattern rule of your own
# objective: Write a %.o: %.c pattern rule whose recipe uses $< and $@, and see it applied to every matching target.
# reference: Pattern Rules
# hint: A pattern rule is an implicit rule you define yourself: % in the target matches any non-empty stem and the same % in the prerequisite stands for it.  $< is that prerequisite and $@ the target.

# Define a pattern rule that compiles every .c file into a .o file.
%.o: %.c
	echo "compile $< -> $@"
	$(CC) -c $< -o $@

all: foo.o bar.o
