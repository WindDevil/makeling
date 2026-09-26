# makeling exercise: 04_targets/10_duplicate_prerequisites
# title: The same prerequisite twice
# objective: Make the inspect recipe print the deduplicated list with $^ and every mention of the repeated prerequisite with $+.
# reference: Automatic Variables
# hint: Both variables list the prerequisites; $^ drops duplicates and $+ keeps them. app.conf is named twice on purpose here.

all: app.conf app.conf

app.conf:
	echo "setting=1" > app.conf

inspect: app.conf app.conf
	@echo "unique prerequisites: $+"
	@echo "every prerequisite: $^"
