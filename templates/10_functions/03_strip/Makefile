# makefiling exercise: 10_functions/03_strip
# title: Cleaning up whitespace with $(strip)
# objective: Normalise the messy variable into a b c: no leading, trailing or repeated whitespace left.
# reference: First Functions
# hint: $(strip text) removes leading and trailing whitespace and reduces every run of spaces inside the text to a single space. Whitespace-only text strips down to the empty string.

empty :=
raw := a   b $(empty)  c
clean := $(raw)
blank := $(strip $(empty)   )

$(info clean=[$(clean)])
$(info blank=[$(blank)])
$(info words=[$(words $(clean))])

all:
	@echo $(clean)
