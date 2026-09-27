# makefiling exercise: 04_targets/08_one_recipe_many_files
# title: One recipe that produces several files
# objective: Make a single recipe create both first.part and second.part for the bundle target.
# reference: Multiple targets
# hint: The rule still runs its recipe once per target, but make skips a target whose file already exists and which has no prerequisites.

bundle: first.part second.part

first.part second.part:
	echo "shared payload" > first.part
	cp first.part second.part
