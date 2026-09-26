# makeling exercise: 09_conditionals/13_makeflags_silent
# title: Detect silent mode
# objective: Branch on whether -s was passed: bare make echoes the command, make -s only prints the message.
# reference: $(MAKEFLAGS)
# hint: The letters in MAKEFLAGS carry no dash, so searching for -s never matches. Search for s on its own and compare the result with s.

all:
ifeq ($(findstring s,$(MAKEFLAGS)),s)
	echo "silent mode"
else
	echo "echoing commands"
endif
