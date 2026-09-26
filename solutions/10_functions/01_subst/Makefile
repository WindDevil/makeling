# makeling exercise: 10_functions/01_subst
# title: Replace text with $(subst)
# objective: Use $(subst from,to,text) to turn the sentence "I am not superman" into '"I am "totally" superman"'.
# reference: First Functions
# hint: $(subst from,to,text) replaces every occurrence of the literal string from with to. The quotes in the example are ordinary characters: they are part of the third argument, not syntax.

# $(subst from,to,text) replaces every occurrence of "from" in "text".
bar := $(subst not,"totally", "I am not superman")
plain := $(subst world,there,hello world)

$(info bar=[$(bar)])
$(info plain=[$(plain)])

all:
	@echo $(plain)
