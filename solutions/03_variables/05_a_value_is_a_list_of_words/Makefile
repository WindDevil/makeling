# makefiling exercise: 03_variables/05_a_value_is_a_list_of_words
# title: A value is a list of words
# objective: Point a target at a variable whose value has irregular spacing and see make turn it into an ordinary word list.
# reference: Variables
# hint: Make splits the value on any run of whitespace. The extra spaces and the variable expansion are both gone by the time $^ prints the prerequisite list.

SRCS := one.c    two.c       three.c

prog: $(SRCS)
	echo "sources: $^"
	touch $@
