# makeling exercise: 10_functions/12_realpath_and_abspath
# title: $(realpath) needs the file, $(abspath) does not
# objective: Show that realpath resolves a name that exists on disk while abspath gives an absolute path for any name at all.
# reference: First Functions
# hint: $(realpath names) resolves names that exist, following symlinks, and returns nothing for a name that is not there. $(abspath names) turns any name into an absolute path, whether or not the file exists.

# present.txt exists; nosuch.txt does not.
$(info real_missing=[$(if $(abspath nosuch.txt),found,missing)])
$(info abs_missing=[$(if $(abspath nosuch.txt),found,missing)])
$(info real_here=[$(if $(realpath present.txt),found,missing)])
$(info abs_here=[$(if $(abspath present.txt),found,missing)])

all:
	@echo checked
