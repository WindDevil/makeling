# makeling exercise: 01_syntax_and_essence/06_every_prerequisite_counts
# title: Every prerequisite is checked
# objective: Declare both parts as prerequisites of combined.txt so that touching either one rebuilds it.
# reference: The essence of Make
# hint: All the names after the colon are prerequisites. The target is rebuilt when any one of them is newer than the target itself.

combined.txt: a.txt
	cat a.txt b.txt > combined.txt
