# makefiling exercise: 03_variables/03_quotes_are_characters
# title: Quotes in a value are just characters
# objective: Assign a quoted string to a variable and see that make keeps the quote characters while the shell uses them.
# reference: Variables
# hint: Make has no quoting rules of its own: the quotes end up inside the value. When the recipe is handed to the shell the shell eats them, which is why $(b) arrives as one word.

a := one two
b := 'one two'

all: args echoes

args:
	printf '[%s]\n' $(a)
	printf '[%s]\n' $(b)

echoes:
	echo $(b)
	echo "$(b)"
