# makefiling exercise: 06_fancy_rules/04_cancel_pattern_rule
# title: Cancelling the built-in compile rule
# objective: Cancel make's built-in %.o: %.c rule with an empty pattern rule, so that only the object files you build by hand can exist.
# reference: Implicit Rules
# hint: An empty pattern rule with the same target and prerequisite patterns cancels the built-in one.  Afterwards make can only build an object file that has an explicit rule of its own.

# An empty pattern rule cancels the built-in rule of the same shape, so
# make stops compiling .c files behind our back.
%.o: %.c

# The one object we want has to be spelled out now.
blah.o: blah.c
	$(CC) -c $< -o $@

all: blah.o
