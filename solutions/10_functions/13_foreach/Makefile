# makeling exercise: 10_functions/13_foreach
# title: Looping with $(foreach)
# objective: Append an exclamation mark to each word of who are you, producing who! are! you!
# reference: The foreach function
# hint: $(foreach var,list,text) sets var to each word of list in turn and expands text for each of them. The results are joined with single spaces. Inside text you must use the loop variable, not the whole list.

foo := who are you
# For each "word" in foo, output that same word with an exclamation after it.
bar := $(foreach wrd,$(foo),$(wrd)!)

$(info bar=[$(bar)])

all:
	@echo $(bar)
