# makeling exercise: 03_variables/06_dir_notdir_basename_suffix
# title: Taking a file name apart
# objective: Apply $(dir), $(notdir), $(basename) and $(suffix) to one variable holding a list of paths.
# reference: Variables
# hint: $(dir) keeps everything up to and including the last slash, $(notdir) keeps what follows it, $(basename) drops the suffix and $(suffix) keeps only the suffix.

SRCS := src/foo.c src/bar.c

all:
	echo "dir: $(dir $(SRCS))"
	echo "notdir: $(notdir $(SRCS))"
	echo "basename: $(basename $(SRCS))"
	echo "suffix: $(suffix $(SRCS))"
