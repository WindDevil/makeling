# makefiling exercise: 10_functions/15_if
# title: Choosing with $(if)
# objective: Produce then! for a condition that expands to something, else! for one that expands to nothing, and use the two-argument form too.
# reference: The if function
# hint: $(if condition,then-part,else-part) tests whether the condition expands to a non-empty string. The else-part is optional, and an empty condition makes the whole $(if) expand to nothing when it is left out.

empty :=
foo := some-text

$(info one=[$(if this-is-not-empty,then!,else!)])
$(info two=[$(if $(empty),then!,else!)])
$(info three=[$(if $(empty),then!)])
$(info four=[$(if $(foo),yes)])
$(info five=[$(if $(empty),yes)])

all:
	@echo done
