# makeling exercise: 08_variables_pt2/01_recursive_vs_simply_expanded
# title: Recursive and simply expanded variables
# objective: Assign one variable from another before that other variable exists, then define it: = picks up the new value, := keeps the one it saw at assignment time.
# reference: Flavors and modification
# hint: A recursive variable (=) stores the text and expands it every time it is used. A simply expanded variable (:=) expands its right-hand side once, immediately, and stores the result.

# Recursive: the text $(later_variable) is stored and expanded on use.
one = one $(later_variable)
# Simply expanded: $(later_variable) is empty right now, and stays empty.
two = two $(later_variable)

later_variable = later

all:
	echo $(one)
	echo $(two)
