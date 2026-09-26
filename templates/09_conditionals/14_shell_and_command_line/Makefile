# makeling exercise: 09_conditionals/14_shell_and_command_line
# title: A conditional fed by $(shell)
# objective: Probe the filesystem with $(shell) and pick the value with ifeq, letting the probed file name come from the command line.
# reference: Conditional if/else
# hint: $(shell ...) runs while make parses the file and its output is compared as text, so the conditional decides the branch before any target is built. A variable set on the command line overrides the file's assignment, so PROBE=absent.mk probes a different file.

PROBE = local.mk

ifeq ($(shell test -f $(PROBE) && echo yes),yes)
RESULT = missing
else
RESULT = found
endif

all:
	@echo "result: $(RESULT)"
