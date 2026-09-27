# makefiling exercise: 10_functions/18_shell
# title: $(shell) runs at expansion time
# objective: Make snapshot capture the value of who as it is when the variable is defined, so it stays first even though who becomes second afterwards.
# reference: The shell function
# hint: $(shell command) runs the command while make expands the text and returns its output with every newline turned into a space. A recursive variable (=) re-runs the shell on every expansion; a simply expanded variable (:=) runs it once, at that line.

who = first
snapshot = $(shell echo $(who))
who = second
live = $(shell echo $(who))

$(info snapshot=[$(snapshot)])
$(info live=[$(live)])
$(info two_lines=[$(shell echo alpha; echo beta)])

all:
	@echo in recipe: $(live)
