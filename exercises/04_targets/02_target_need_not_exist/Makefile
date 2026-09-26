# makeling exercise: 04_targets/02_target_need_not_exist
# title: A target need not exist on disk
# objective: Make report depend on data.txt so that the data file is generated first, even though report itself is never created.
# reference: Targets
# hint: A prerequisite is built before the target's own recipe runs. A target whose name never appears on disk is out of date every time.

report:
	cat data.txt

data.txt:
	echo "42" > data.txt
