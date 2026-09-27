# makefiling exercise: 03_variables/12_target_directory_and_file
# title: $(@D) and $(@F)
# objective: Build a file inside a directory that does not exist yet, using $(@D) for the directory and $(@F) for the file name.
# reference: Automatic Variables
# hint: $(@D) is the directory part of the target and $(@F) the file part. Create $(@D) first, then write into $@.

out/nested/report.txt:
	mkdir -p $(@D)
	echo $(@F) > $@
