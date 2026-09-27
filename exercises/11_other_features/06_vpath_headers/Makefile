# makefiling exercise: 11_other_features/06_vpath_headers
# title: Finding a prerequisite in another directory
# objective: Use vpath so that blah.h, which only exists in headers/, is found as a prerequisite of some_binary.
# reference: The vpath Directive
# hint: vpath takes a pattern and the directories to search: vpath %.h headers. The recipe must still copy the file make found, so use the automatic variable $< rather than the bare file name.

some_binary: blah.h
	cat $< > some_binary
