# makefiling exercise: 08_variables_pt2/04_default_with_question_mark
# title: ?= sets a default only when the variable is undefined
# objective: Give one variable a default without clobbering the value it already has, and let a brand new variable take the default.
# reference: Flavors and modification
# hint: ?= assigns only if the variable has no value yet. A plain = always assigns, which would overwrite the earlier definition.

one = hello
one ?= will not be set
two ?= will be set

all:
	echo one is $(one)
	echo two is $(two)
