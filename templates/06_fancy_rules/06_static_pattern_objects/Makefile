# makeling exercise: 06_fancy_rules/06_static_pattern_objects
# title: One static pattern rule for a list of objects
# objective: Replace three hand-written object rules with a single static pattern rule over $(objects), and link them into a program.
# reference: Static Pattern Rules
# hint: The syntax is targets...: target-pattern: prereq-patterns; the stem matched by %.o is put back where %.c says.  Give all.c real content, because the %.c pattern rule below only touches an empty file.

objects = foo.o bar.o all.o

all: $(objects)
	$(CC) $^ -o all

# targets...: target-pattern: prereq-patterns ...
# foo.o is matched by %.o, giving the stem "foo"; %.c then becomes foo.c.
$(objects): %.o: %.c
	$(CC) -c $^ -o $@

# TODO: nothing writes all.c, so the %.c rule below touches it empty

%.c:
	touch $@

clean:
	rm -f *.c *.o all
