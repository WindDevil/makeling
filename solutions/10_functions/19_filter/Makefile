# makefiling exercise: 10_functions/19_filter
# title: Selecting words with $(filter)
# objective: Keep only the .o files from obj_files, then keep the .o and .result files, then keep every C source and header.
# reference: The filter function
# hint: $(filter pattern,list) returns the words of list that match the pattern, in their original order, and drops the rest. Write as many patterns as you like, separated by spaces, and remember the % in front of the suffix.

sources := a.c b.h c.c d.h
obj_files := foo.result bar.o lose.o

filtered := $(filter %.o,$(obj_files))

$(info filtered=[$(filtered)])
$(info both=[$(filter %.o %.result,$(obj_files))])
$(info keep=[$(filter %.c %.h,$(sources))])

all:
	@echo $(filtered)
