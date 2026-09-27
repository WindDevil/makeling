# makefiling exercise: 03_variables/07_addprefix_and_addsuffix
# title: Adding a prefix and a suffix to every word
# objective: Use $(addprefix) and $(addsuffix) to build an object list and a backup list out of one source list.
# reference: Makefile Cookbook
# hint: $(addprefix prefix,list) and $(addsuffix suffix,list) touch every word of the list. The prefix or the suffix comes first in the call; the list comes last.

SRCS := main.c util.c
BUILD := build

OBJS := $(addprefix $(BUILD)/,$(SRCS))
BACKUPS := $(addsuffix .bak,$(SRCS))

all:
	echo "objs: $(OBJS)"
	echo "backups: $(BACKUPS)"
