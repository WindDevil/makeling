# makefiling exercise: 10_functions/06_substitution_reference
# title: The $(text:pattern=replacement) shorthand
# objective: Express the same rewrite twice: once with the % shorthand and once with the suffix-only shorthand.
# reference: String Substitution
# hint: $(foo:%.o=%.c) is shorthand for $(patsubst %.o,%.c,$(foo)), and $(foo:.o=.c) is the suffix-only form of the same thing. Do not pad the shorthand with spaces; they would become part of the search or the replacement.

foo := a.o b.o l.a c.o

# $(foo:pattern=replacement) is a shorthand for $(patsubst pattern,replacement,$(foo)).
one := $(foo:%.o=%.c)
# Dropping the % makes it a plain suffix substitution.
two := $(foo:.c=.o)

$(info one=[$(one)])
$(info two=[$(two)])

all:
	@echo $(one)
