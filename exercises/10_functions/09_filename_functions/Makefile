# makeling exercise: 10_functions/09_filename_functions
# title: Splitting file names apart
# objective: Take src/a.c src/b.h apart into directories, file names, suffixes and stems.
# reference: First Functions
# hint: $(dir) keeps everything up to and including the last slash, $(notdir) drops it, $(suffix) and $(basename) split at the last dot. $(basename) keeps the directory part of the path.

files := src/a.c src/b.h

$(info dirs=[$(dir $(files))])
$(info names=[$(notdir $(files))])
$(info suffixes=[$(suffix $(files))])
$(info stems=[$(basename $(notdir $(files)))])
$(info bare=[$(basename noext)][$(suffix noext)])

all:
	@echo $(notdir $(files))
