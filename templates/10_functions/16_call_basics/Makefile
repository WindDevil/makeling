# makefiling exercise: 10_functions/16_call_basics
# title: Writing a function with $(call)
# objective: Report the name of the called variable and its parameters with $(0), $(1) and $(2), and make a template that repeats its first parameter three times.
# reference: The call function
# hint: A variable holding $(1), $(2), ... is a function you invoke with $(call variable,param1,param2). $(0) is the name of the variable being called, and parameters you do not pass are empty.

sweet_new_fn = Variable Name: $(0) First: $(1) Second: $(2) Empty Variable: $(3)
triple = $(0) $(0) $(0)

$(info call=[$(call sweet_new_fn, go, tigers)])
$(info triple=[$(call triple,ha)])

all:
	@echo $(call triple,ha)
