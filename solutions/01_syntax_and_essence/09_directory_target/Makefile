# makefiling exercise: 01_syntax_and_essence/09_directory_target
# title: When the target is a directory
# objective: Let make treat the existing directory out as the target's file, skipping the recipe until out/.keep becomes newer.
# reference: The essence of Make
# hint: A directory is a file as far as make is concerned. If out exists the recipe is skipped; list out/.keep as a prerequisite so make has a timestamp to compare against.

out: out/.keep
	echo "the directory target was out of date"
