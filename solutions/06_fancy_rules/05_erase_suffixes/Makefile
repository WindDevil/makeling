# makefiling exercise: 06_fancy_rules/05_erase_suffixes
# title: Erasing make's built-in suffix rules
# objective: Empty the suffix list so make forgets how to compile and link C sources, and see that only explicit recipes are left.
# reference: Implicit Rules
# hint: A .SUFFIXES line with no prerequisites erases the suffix list, and with it the built-in rules that hang off it.  After that make has no recipe for blah.o or for linking blah.

# .SUFFIXES with no prerequisites erases the built-in suffix rules, and
# with them the C compile and link rules.
.SUFFIXES:

# With nothing built in, this object needs a recipe of its own.
blah.o: blah.c
	$(CC) -c $< -o $@

all: blah.o
