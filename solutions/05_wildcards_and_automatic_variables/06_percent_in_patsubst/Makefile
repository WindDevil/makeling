# makeling exercise: 05_wildcards_and_automatic_variables/06_percent_in_patsubst
# title: % matches a stem, and the stem is substituted back
# objective: Turn a list of .c names into .o names with $(patsubst %.c,%.o,...) and with the $(list:%.c=%.o) shorthand.
# reference: % Wildcard
# hint: The % in the pattern matches any run of characters, and whatever it matched is called the stem. The % in the replacement is replaced by that stem. A word that does not match is copied through untouched.

srcs := a.c b.c l.a c.c

objects := $(patsubst %.c,%.o,$(srcs))
same := $(srcs:%.c=%.o)
objdir := $(patsubst %.c,obj/%.o,$(srcs))

show:
	@echo patsubst: $(objects)
	@echo shorthand: $(same)
	@echo into a directory: $(objdir)
