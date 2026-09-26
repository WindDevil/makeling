# makeling exercise: 01_syntax_and_essence/03_prerequisite_order
# title: Prerequisites are built left to right
# objective: Order the prerequisites of the all target so that make builds one, then two, then three.
# reference: Makefile Syntax
# hint: Every prerequisite has to be finished before the commands of the target run, and make works through the list from left to right.

all: one two three
	cat order.txt

one:
	echo "one" >> order.txt

two:
	echo "two" >> order.txt

three:
	echo "three" >> order.txt
