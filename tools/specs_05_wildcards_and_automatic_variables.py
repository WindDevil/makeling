"""Exercises for the tutorial's "Automatic Variables and Wildcards" chapter.

The chapter covers three sections: ``* Wildcard`` (make's filesystem glob),
``% Wildcard`` (make's own stem-matching wildcard) and ``Automatic Variables``
(``$@``, ``$<``, ``$^``, ``$?``, ``$*`` and the ``D``/``F`` variants).

Recipe lines inside the ``makefile`` strings are indented with a ``\\t``
escape.  Python turns that into a real tab, which is what make requires;
writing a literal tab into the source would be invisible and easy to lose.
"""

from spec import ex, mk, step

TOPIC = "05_wildcards_and_automatic_variables"

SPECS = [
    # ---------------------------------------------------------------- * --
    ex(
        topic=TOPIC,
        slug="01_wildcard_function_in_a_variable",
        title="$(wildcard) expands at parse time",
        objective=(
            "Collect every .c file with $(wildcard *.c) and use the resulting "
            "list as the prerequisites of a target."
        ),
        reference="* Wildcard",
        hint=(
            "The wildcard function is the safe way to use *: it runs while "
            "make reads the file and returns the matching names, separated by "
            "spaces."
        ),
        makefile="""
sources := $(wildcard *.c)

show: $(sources)
\t@echo target: $@
\t@echo sources: $(sources)
\t@echo prereqs: $^
""",
        steps=[
            mk(
                "show",
                stdout="target: show\nsources: alpha.c beta.c\nprereqs: alpha.c beta.c",
                description="$(wildcard *.c) lists both source files, sorted",
            ),
            mk(
                "show",
                stdout="target: show",
                description="the target is named on its own line",
            ),
        ],
        breaks=[
            ("sources := $(wildcard *.c)", "sources := $(wildcard *.h)"),
        ],
        files={
            "alpha.c": "int alpha(void) { return 1; }\n",
            "beta.c": "int beta(void) { return 2; }\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="02_wildcard_empty_versus_shell_glob",
        title="$(wildcard) is empty when nothing matches",
        objective=(
            "Show that $(wildcard *.dat) expands to nothing while a shell that "
            "globs *.dat in a recipe leaves the pattern as it is."
        ),
        reference="* Wildcard",
        hint=(
            "make runs the recipe through the shell, and /bin/sh passes an "
            "unmatched pattern through unchanged. $(wildcard) has no such "
            "rule: it returns the empty string."
        ),
        makefile="""
present := $(wildcard *.txt)
missing := $(wildcard *.dat)

report:
\t@echo present: $(present)
\t@echo missing: $(missing)
\t@echo shell-glob: *.dat
\t@echo shell-match: *.txt
""",
        steps=[
            mk(
                stdout=(
                    "present: a.txt b.txt\n"
                    "missing:\n"
                    "shell-glob: *.dat\n"
                    "shell-match: a.txt b.txt"
                ),
                description="wildcard returns nothing, the shell keeps the pattern",
            ),
        ],
        breaks=[
            ("missing := $(wildcard *.dat)", "missing := *.dat"),
        ],
        files={
            "a.txt": "alpha\n",
            "b.txt": "beta\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="03_star_in_a_variable_stays_literal",
        title="A bare * in a variable is not a wildcard",
        objective=(
            "Contrast thing_wrong := *.o with thing_right := $(wildcard *.o) "
            "and observe what make does with each one as a prerequisite."
        ),
        reference="* Wildcard",
        hint=(
            "Assigning *.o to a variable copies the two characters, it does "
            "not look at the filesystem. A prerequisite that is literally "
            "*.o has to be built, and make does not know how."
        ),
        makefile="""
# Don't do this! '*' is not expanded in a variable definition.
thing_wrong := *.o
thing_right := $(wildcard *.o)

report:
\t@echo wrong: [$(thing_wrong)]
\t@echo right: [$(thing_right)]

one: $(thing_wrong)
\t@echo one ran

three: $(thing_right)
\t@echo three ran
""",
        steps=[
            mk(
                "report",
                stdout="wrong: [*.o]\nright: []",
                description="the variable holds the literal text, the function is empty",
            ),
            mk(
                "one",
                exit_code=2,
                stderr="No rule to make target '*.o', needed by 'one'.",
                description="the literal *.o prerequisite cannot be satisfied",
            ),
            mk(
                "three",
                stdout="three ran",
                description="the empty wildcard leaves three with no prerequisites",
            ),
        ],
        breaks=[
            ("three: $(thing_right)", "three: $(thing_wrong)"),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="04_wildcard_in_a_target_list",
        title="An empty wildcard leaves a rule with no prerequisites",
        objective=(
            "Write all: $(wildcard *.o) so that it still works when no object "
            "file exists, and see why a bare *.o in the same place does not."
        ),
        reference="* Wildcard",
        hint=(
            "When $(wildcard) matches nothing the prerequisite list is simply "
            "empty and the rule is still valid. The string *.o written "
            "directly into the rule is not: make tries to build a file with "
            "that name."
        ),
        makefile="""
# No .o files exist, so this list is empty.
objects := $(wildcard *.o)

all: $(objects)
\t@echo objects: [$(objects)]
\t@echo prerequisites of all: [$^]

bare: *.o
\t@echo bare ran
""",
        steps=[
            mk(
                "all",
                stdout="objects: []\nprerequisites of all: []",
                description="an empty wildcard is not an error",
            ),
            mk(
                "bare",
                exit_code=2,
                stderr="No rule to make target '*.o', needed by 'bare'.",
                description="the literal *.o in the rule is treated as a file name",
            ),
        ],
        breaks=[
            ("objects := $(wildcard *.o)", "objects := *.o"),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="05_parse_time_versus_recipe_time",
        title="make globs at parse time, the shell globs at recipe time",
        objective=(
            "Have one rule create a .c file and another report both the "
            "parse-time $(wildcard *.c) and the recipe-time shell glob."
        ),
        reference="* Wildcard",
        hint=(
            "make reads the whole file before it runs a single recipe, so "
            "$(wildcard) cannot see a file that a prerequisite creates later. "
            "The shell, by contrast, expands *.c only when the recipe line "
            "runs."
        ),
        makefile="""
gen:
\t@echo "int main(void) { return 0; }" > new.c

report: gen
\t@echo "parse-time wildcard: $(wildcard *.c)"
\t@echo "recipe-time shell:" *.c
""",
        steps=[
            mk(
                "report",
                stdout="parse-time wildcard:\nrecipe-time shell: new.c",
                description="only the shell sees the file gen just created",
            ),
            mk(
                "report",
                stdout="parse-time wildcard: new.c\nrecipe-time shell: new.c",
                description="on the next run make finds new.c while reading the file",
            ),
        ],
        breaks=[
            ('"parse-time wildcard: $(wildcard *.c)"', '"parse-time wildcard: *.c"'),
        ],
    ),
    # ---------------------------------------------------------------- % --
    ex(
        topic=TOPIC,
        slug="06_percent_in_patsubst",
        title="% matches a stem, and the stem is substituted back",
        objective=(
            "Turn a list of .c names into .o names with $(patsubst %.c,%.o,...) "
            "and with the $(list:%.c=%.o) shorthand."
        ),
        reference="% Wildcard",
        hint=(
            "The % in the pattern matches any run of characters, and whatever "
            "it matched is called the stem. The % in the replacement is "
            "replaced by that stem. A word that does not match is copied "
            "through untouched."
        ),
        makefile="""
srcs := a.c b.c l.a c.c

objects := $(patsubst %.c,%.o,$(srcs))
same := $(srcs:%.c=%.o)
objdir := $(patsubst %.c,obj/%.o,$(srcs))

show:
\t@echo patsubst: $(objects)
\t@echo shorthand: $(same)
\t@echo into a directory: $(objdir)
""",
        steps=[
            mk(
                stdout=(
                    "patsubst: a.o b.o l.a c.o\n"
                    "shorthand: a.o b.o l.a c.o\n"
                    "into a directory: obj/a.o obj/b.o l.a obj/c.o"
                ),
                description="the stem replaces % in the replacement text",
            ),
        ],
        breaks=[
            ("$(patsubst %.c,%.o,$(srcs))", "$(patsubst %.o,%.c,$(srcs))"),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="07_static_pattern_rule_stem",
        title="The stem in a static pattern rule",
        objective=(
            "Use $(targets): %.out: %.raw so that each target is matched by "
            "the target pattern and the stem is substituted into the "
            "prerequisite pattern."
        ),
        reference="% Wildcard",
        hint=(
            "In a static pattern rule the target pattern matches the target "
            "name and the matched stem replaces the % in the prerequisite "
            "pattern. foo.out is matched by %.out with the stem foo, so its "
            "prerequisite is foo.raw."
        ),
        makefile="""
targets := foo.out bar.out

all: $(targets)
\t@echo all: $^

$(targets): %.out: %.raw
\t@echo target=[$@] stem=[$*] prereq=[$<]
\t@touch $@
""",
        steps=[
            mk(
                "all",
                stdout=(
                    "target=[foo.out] stem=[foo] prereq=[foo.raw]\n"
                    "target=[bar.out] stem=[bar] prereq=[bar.raw]\n"
                    "all: foo.out bar.out"
                ),
                description="each stem produces that target's own prerequisite",
            ),
            mk(
                "all",
                stdout="stem=[",
                stdout_mode="not_contains",
                description="both outputs already exist, so nothing is rebuilt",
            ),
            mk(
                "all",
                stdout="all: foo.out bar.out",
                description="all still runs its own recipe on the second run",
            ),
        ],
        breaks=[
            ("prereq=[$<]", "prereq=[$*]"),
        ],
        files={
            "foo.raw": "foo contents\n",
            "bar.raw": "bar contents\n",
        },
    ),
    # ------------------------------------------------- automatic vars --
    ex(
        topic=TOPIC,
        slug="08_dollar_at_and_dollar_less",
        title="$@ is the target, $< is the first prerequisite",
        objective=(
            "Copy the first prerequisite onto the target while printing both "
            "$@ and $< from the recipe."
        ),
        reference="Automatic Variables",
        hint=(
            "$@ is the name of the target being built and $< is the first "
            "prerequisite. $< is the one to use in a rule that has a single "
            "source file."
        ),
        makefile="""
greeting.txt: message.txt
\t@echo target = $@
\t@echo first prerequisite = $<
\t@cp $< $@
""",
        steps=[
            mk(
                "greeting.txt",
                stdout="target = greeting.txt\nfirst prerequisite = message.txt",
                description="the recipe names the file it is building",
            ),
            step(
                "cat",
                "greeting.txt",
                stdout="hello from message.txt",
                description="the copy really happened",
            ),
            mk(
                "greeting.txt",
                stdout="make: 'greeting.txt' is up to date.",
                description="once the target exists there is nothing to do",
            ),
        ],
        breaks=[
            (
                '\t@echo target = $@\n\t@echo first prerequisite = $<',
                '\t@echo target = $<\n\t@echo first prerequisite = $@',
            ),
        ],
        files={"message.txt": "hello from message.txt\n"},
    ),
    ex(
        topic=TOPIC,
        slug="09_dollar_caret_and_dollar_question",
        title="$^ lists every prerequisite, $? only the newer ones",
        objective=(
            "Build a target from two prerequisites and show that $^ names "
            "both while $? names only the one that has been touched since."
        ),
        reference="Automatic Variables",
        hint=(
            "$^ is the whole prerequisite list, in the order it was written. "
            "$? is the subset of those prerequisites whose modification time "
            "is newer than the target's."
        ),
        makefile="""
hey: one two
\t@echo all prerequisites = $^
\t@echo newer prerequisites = $?
\t@touch hey

one:
\t@touch one

two:
\t@touch two
""",
        steps=[
            mk(
                stdout="all prerequisites = one two\nnewer prerequisites = one two",
                description="hey does not exist yet, so everything is newer",
            ),
            step("touch", "one", description="make one newer than hey"),
            mk(
                stdout="all prerequisites = one two\nnewer prerequisites = one",
                description="only the touched prerequisite is out of date",
            ),
        ],
        breaks=[
            ("\t@echo newer prerequisites = $?", "\t@echo newer prerequisites = $^"),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="10_dollar_star_without_a_pattern",
        title="$* in an explicit rule is the target minus a known suffix",
        objective=(
            "Print $* for a target ending in .o, for a target ending in .txt "
            "and for a target with no suffix at all."
        ),
        reference="Automatic Variables",
        hint=(
            "In an explicit rule $* is only the stem if the target ends in "
            "one of make's known suffixes, such as .o or .c. For any other "
            "name there is no stem to report and $* is empty."
        ),
        makefile="""
program.o: input.c
\t@echo object target: stem=[$*] target=[$@]

notes.txt: input.c
\t@echo text target: stem=[$*] target=[$@]

release: input.c
\t@echo suffixless target: stem=[$*] target=[$@]
""",
        steps=[
            mk(
                "program.o",
                stdout="object target: stem=[program] target=[program.o]",
                description=".o is a known suffix, so the stem is program",
            ),
            mk(
                "notes.txt",
                stdout="text target: stem=[] target=[notes.txt]",
                description=".txt is not a known suffix, so there is no stem",
            ),
            mk(
                "release",
                stdout="suffixless target: stem=[] target=[release]",
                description="a name without a suffix has no stem either",
            ),
        ],
        breaks=[
            ("object target: stem=[$*]", "object target: stem=[$@]"),
        ],
        files={"input.c": "int main(void) { return 0; }\n"},
    ),
    ex(
        topic=TOPIC,
        slug="11_dollar_star_in_a_pattern_rule",
        title="$* in a pattern rule is the stem",
        objective=(
            "Write a pattern rule that copies %.txt to %.backup and prints "
            "the stem it matched."
        ),
        reference="Automatic Variables",
        hint=(
            "A pattern rule has a % in its target. That % matches a piece of "
            "the target name, and the matched piece is the stem, available as "
            "$*. The % in the prerequisite stands for the same stem."
        ),
        makefile="""
%.backup: %.txt
\t@echo target = $@
\t@echo stem = $*
\t@cp $< $@

all: a.backup b.backup
\t@echo all: $^
""",
        steps=[
            mk(
                "all",
                stdout=(
                    "target = a.backup\n"
                    "stem = a\n"
                    "target = b.backup\n"
                    "stem = b\n"
                    "all: a.backup b.backup"
                ),
                description="the stem is the part of the target % matched",
            ),
        ],
        breaks=[
            ("\t@echo stem = $*", "\t@echo stem = $@"),
        ],
        files={
            "a.txt": "first\n",
            "b.txt": "second\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="12_directory_and_file_variants",
        title="The D and F variants of the automatic variables",
        objective=(
            "Print $(@D), $(@F), $(<D), $(<F), $(^D) and $(^F) for a target "
            "that lives in a subdirectory."
        ),
        reference="Automatic Variables",
        hint=(
            "Every automatic variable that holds file names has a D variant "
            "for the directory part and an F variant for the file part. "
            "A name with no directory gives . as its D part, which is exactly "
            "what mkdir -p $(@D) needs."
        ),
        makefile="""
out/report.txt: src/one.txt src/two.txt
\t@echo at: D=[$(@D)] F=[$(@F)]
\t@echo lt: D=[$(<D)] F=[$(<F)]
\t@echo all: D=[$(^D)] F=[$(^F)]
\t@mkdir -p $(@D)
\t@touch $@

orphan.txt: src/one.txt
\t@echo orphan D=[$(@D)] F=[$(@F)]
\t@touch $@
""",
        steps=[
            mk(
                "out/report.txt",
                stdout=(
                    "at: D=[out] F=[report.txt]\n"
                    "lt: D=[src] F=[one.txt]\n"
                    "all: D=[src src] F=[one.txt two.txt]"
                ),
                description="D strips the file part, F strips the directory part",
            ),
            step(
                "test",
                "-f",
                "out/report.txt",
                description="mkdir -p $(@D) created out/ and the recipe wrote into it",
            ),
            mk(
                "orphan.txt",
                stdout="orphan D=[.] F=[orphan.txt]",
                description="a target in the current directory has . as its D part",
            ),
        ],
        breaks=[
            ("D=[$(^D)] F=[$(^F)]", "D=[$(^F)] F=[$(^D)]"),
        ],
        files={
            "src/one.txt": "one\n",
            "src/two.txt": "two\n",
        },
    ),
    # ------------------------------------------------------------ recap --
    ex(
        topic=TOPIC,
        slug="13_wildcard_patsubst_and_pattern_rule",
        title="Putting the three pieces together",
        objective=(
            "Discover the sources with $(wildcard src/*.c), rewrite them into "
            "build/ names with $(patsubst), and let a pattern rule build each "
            "one into its own directory."
        ),
        reference="* Wildcard",
        hint=(
            "The wildcard decides what exists right now, patsubst rewrites "
            "each discovered name into the name you want to build, and the "
            "pattern rule knows how to build any name of that shape."
        ),
        makefile="""
srcs := $(wildcard src/*.c)
objects := $(patsubst src/%.c,build/%.pack,$(srcs))

all: $(objects)
\t@echo sources: $(srcs)
\t@echo objects: $(objects)

build/%.pack: src/%.c
\t@echo compile $< into $@ with stem $*
\t@mkdir -p $(@D)
\t@touch $@

clean:
\t@rm -rf build
""",
        steps=[
            mk(
                "all",
                stdout=(
                    "compile src/alpha.c into build/alpha.pack with stem alpha\n"
                    "compile src/beta.c into build/beta.pack with stem beta\n"
                    "sources: src/alpha.c src/beta.c\n"
                    "objects: build/alpha.pack build/beta.pack"
                ),
                description="each object comes from the source with the same stem",
            ),
            mk(
                "all",
                stdout="compile",
                stdout_mode="not_contains",
                description="the second run has nothing to rebuild",
            ),
            step(
                "test",
                "-f",
                "build/alpha.pack",
                description="both objects were written into build/",
            ),
            mk(
                "clean",
                missing=["build/alpha.pack"],
                description="clean removes the whole build directory",
            ),
        ],
        breaks=[
            ("$(patsubst src/%.c,build/%.pack,$(srcs))", "$(patsubst %.c,%.pack,$(srcs))"),
        ],
        files={
            "src/alpha.c": "int alpha(void) { return 1; }\n",
            "src/beta.c": "int beta(void) { return 2; }\n",
        },
    ),
]
