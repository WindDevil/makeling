# makefiling exercise: 11_other_features/07_vpath_clear
# title: Clearing a stale search path
# objective: Forget the old headers directory before adding the new one, so that blah.h resolves to the file in new/.
# reference: The vpath Directive
# hint: A vpath directive with no pattern clears every search path added so far. Without it the earlier directory is still searched first and its stale header wins.

vpath %.h old

vpath %.h new

some_binary: blah.h
	cat $< > some_binary
