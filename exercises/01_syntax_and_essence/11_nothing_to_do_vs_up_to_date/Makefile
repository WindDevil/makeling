# makeling exercise: 01_syntax_and_essence/11_nothing_to_do_vs_up_to_date
# title: Nothing to be done versus up to date
# objective: Use a target with no recipe so make reports nothing to be done, and a target whose file exists so make reports it is up to date.
# reference: The essence of Make
# hint: Nothing to be done is what make says about a target that has no recipe at all. Up to date is what it says about a target whose recipe was skipped because the file is already there.

all:
	echo "all ran"

report.txt:
	echo "building the report" > report.txt
