# makeling exercise: 02_quick_examples/07_shared_prerequisite
# title: A wider graph with a shared prerequisite
# objective: Build a report from two files that are both copied from the same base file, and confirm the order the recipes run in.
# reference: More quick examples
# hint: Prerequisites are worked through from left to right, so base.txt is made first for left.txt, and is already up to date by the time right.txt asks for it.

report: left.txt
	cat left.txt right.txt > report

left.txt: base.txt
	cp base.txt left.txt

right.txt: base.txt
	cp base.txt right.txt

base.txt:
	echo "base" > base.txt
