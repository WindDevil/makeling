# makeling exercise: 07_commands_and_execution/02_silencing_a_whole_target
# title: Silencing a target, or the whole run
# objective: Keep one target's commands out of the output with .SILENT, and compare that with make -s, which silences everything.
# reference: Command Echoing/Silencing
# hint: .SILENT: quiet silences just that target. With no prerequisites at all, .SILENT: silences every target; make -s (or --silent) does the same for one run without touching the Makefile.

all: quiet loud

quiet:
	echo "quiet target ran"

loud:
	echo "loud target ran"

.SILENT:
