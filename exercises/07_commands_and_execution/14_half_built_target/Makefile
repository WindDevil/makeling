# makeling exercise: 07_commands_and_execution/14_half_built_target
# title: A failed recipe leaves a half-built target
# objective: Fail a recipe after it has written part of its output, and see that make keeps the partial file and treats it as finished.
# reference: Interrupting or killing make
# hint: make never rolls a target back when a recipe fails, so report.txt is left with only the first write - and the next make finds the file and reports it up to date. The recipe has to fail between its two writes. (Interrupting make with ctrl-c is different: then make removes the targets it has just made.)

report.txt:
	@echo "partial line" > report.txt
	@true
	@echo "complete report" > report.txt
