# makefiling exercise: 03_variables/14_first_prerequisite_only
# title: $< is the first prerequisite
# objective: Copy the first of two prerequisites into the target while still reporting all of them.
# reference: Automatic Variables
# hint: With several prerequisites $< is the first one on the target line, not all of them; $^ is the whole list. Two arguments to cp would be a mistake.

out.txt: a.txt b.txt
	cp $< $@
	echo "inputs: $^" >> $@
	cat $@
