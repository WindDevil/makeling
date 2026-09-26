# makeling exercise: 00_getting_started/06_beyond_compilation
# title: Make is not only for compilers
# objective: Chain two non-compilation targets so that make builds a report file before printing it.
# reference: Why do Makefiles exist?
# hint: Any target can carry any shell command. Let the report target depend on the file it prints, so the file is produced first.

report:
	cat summary.txt

summary.txt: names.txt
	grep -c . names.txt > summary.txt
