# makeling exercise: 10_functions/17_call_template
# title: A template that builds a list
# objective: Use $(call) to turn the names main util into the object files src/main.o src/util.o, and let a pattern rule build them.
# reference: The call function
# hint: Define the template with = first, then expand it with $(call objects_for,src,$(names)): $(1) becomes src and $(2) the list. Inside the template a $(foreach) visits every word of $(2).

# A template: $(1) is the directory, $(2) the list of names.
objects_for = $(foreach name,$(2),$(1)/$(name).o)

names := main util
objects := $(call objects_for,src,$(names))

$(info objects=[$(objects)])

app: $(objects)
	@echo linking $^

src/%.o: src/%.c
	@echo compile $< -o $@
