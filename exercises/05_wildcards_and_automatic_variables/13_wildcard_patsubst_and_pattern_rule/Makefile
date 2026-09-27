# makefiling exercise: 05_wildcards_and_automatic_variables/13_wildcard_patsubst_and_pattern_rule
# title: Putting the three pieces together
# objective: Discover the sources with $(wildcard src/*.c), rewrite them into build/ names with $(patsubst), and let a pattern rule build each one into its own directory.
# reference: * Wildcard
# hint: The wildcard decides what exists right now, patsubst rewrites each discovered name into the name you want to build, and the pattern rule knows how to build any name of that shape.

srcs := $(wildcard src/*.c)
objects := $(patsubst %.c,%.pack,$(srcs))

all: $(objects)
	@echo sources: $(srcs)
	@echo objects: $(objects)

build/%.pack: src/%.c
	@echo compile $< into $@ with stem $*
	@mkdir -p $(@D)
	@touch $@

clean:
	@rm -rf build
