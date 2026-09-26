# makeling exercise: 10_functions/05_patsubst
# title: Rewriting words with $(patsubst)
# objective: Turn a.o b.o l.a c.o into a.c b.c l.a c.c, and turn the two src/ paths into build/ paths, with %.o and %.c patterns.
# reference: String Substitution
# hint: $(patsubst pattern,replacement,text) rewrites every word that matches pattern; the % stands for any characters, and the % in the replacement is filled in with whatever it matched. A word that does not match is left alone.

foo := a.o b.o l.a c.o

obj := $(patsubst %.o,%.c,$(foo))
moved := $(patsubst src/%.c,build/%.o,src/a.c src/b.c)

$(info obj=[$(obj)])
$(info moved=[$(moved)])

all:
	@echo $(obj)
