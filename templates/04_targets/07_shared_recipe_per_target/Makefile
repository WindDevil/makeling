# makeling exercise: 04_targets/07_shared_recipe_per_target
# title: One recipe writes each target
# objective: Let a single recipe build both red.txt and blue.txt by writing to $@, so each target gets its own file.
# reference: Multiple targets
# hint: $@ is the target being built right now. A hard-coded file name would be written twice and neither target would exist.

all: red.txt blue.txt

red.txt blue.txt:
	echo "$@ created" > out.txt
