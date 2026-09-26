# makeling exercise: 07_commands_and_execution/11_dash_suppresses_the_error
# title: A leading - tolerates one command's failure
# objective: Prefix a failing command with - so make prints the error, carries on with the recipe, and still reports the run as a success.
# reference: Error handling with -k, -i, and -
# hint: A - before the command tells make to ignore this one failure: the line is reported as (ignored), the recipe continues and make exits 0. Add it to both failing lines.

all:
	false
	echo "make carried on to the next line"
	-false
	echo "and the whole run still succeeded"
