# makefiling exercise: 10_functions/14_foreach_paths
# title: Building a list of paths with $(foreach)
# objective: Map the module names auth cart order to build/auth.o build/cart.o build/order.o using a single foreach.
# reference: The foreach function
# hint: Write the path around the loop variable: $(foreach m,$(modules),build/$(m).o). The text is re-expanded for every word, so $(m) takes a different value each time.

modules := auth cart order
objects := $(foreach m,$(modules),build/$(m).o)

$(info objects=[$(objects)])

all:
	@echo $(objects)
