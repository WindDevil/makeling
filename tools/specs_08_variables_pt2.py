"""Exercises for the tutorial's "Variables Pt. 2" chapter.

Recipe lines inside the ``makefile`` strings are indented with a ``\\t`` escape.
Python turns that into a real tab, which is what make requires; writing a
literal tab into the source would be invisible and easy to lose.

Command line overrides cannot be expressed by editing the Makefile, so the
steps that exercise them pass ``VAR=value`` arguments to ``make`` instead.
"""

from spec import ex, mk

TOPIC = "08_variables_pt2"

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_recursive_vs_simply_expanded",
        title="Recursive and simply expanded variables",
        objective=(
            "Assign one variable from another before that other variable "
            "exists, then define it: = picks up the new value, := keeps the "
            "one it saw at assignment time."
        ),
        reference="Flavors and modification",
        hint=(
            "A recursive variable (=) stores the text and expands it every "
            "time it is used. A simply expanded variable (:=) expands its "
            "right-hand side once, immediately, and stores the result."
        ),
        makefile="""
# Recursive: the text $(later_variable) is stored and expanded on use.
one = one $(later_variable)
# Simply expanded: $(later_variable) is empty right now, and stays empty.
two := two $(later_variable)

later_variable = later

all:
\techo $(one)
\techo $(two)
""",
        steps=[
            mk(
                stdout=(
                    "echo one later\n"
                    "one later\n"
                    "echo two\n"
                    "two"
                ),
                description=(
                    "the recursive variable grew with later_variable, the "
                    "simply expanded one did not"
                ),
            ),
        ],
        breaks=[("two := two $(later_variable)", "two = two $(later_variable)")],
    ),
    ex(
        topic=TOPIC,
        slug="02_simply_expanded_appending",
        title="A variable cannot be extended from itself with =",
        objective=(
            "Extend one variable with its own old value plus a suffix, so "
            "that make prints the combined value instead of refusing to run."
        ),
        reference="Flavors and modification",
        hint=(
            ":= expands the right-hand side before assigning, so ${one} is "
            "the old value. With = the reference is stored unevaluated and "
            "the variable ends up referring to itself."
        ),
        makefile="""
one = hello

# := expands ${one} right now, so this reads "hello" + " there".
one := ${one} there

all:
\techo $(one)
""",
        steps=[
            mk(
                stdout="echo hello there\nhello there",
                description="the variable holds the old value plus the suffix",
            ),
            mk(
                stderr="Recursive variable",
                stderr_mode="not_contains",
                description="make did not complain about a self reference",
            ),
        ],
        breaks=[("one := ${one} there", "one = ${one} there")],
    ),
    ex(
        topic=TOPIC,
        slug="03_appending_recursive_vs_simply_expanded",
        title="Appending to a recursive and to a simply expanded variable",
        objective=(
            "Append the same text to both flavours of variable, then change "
            "the variable they both refer to, and show that only the "
            "recursive one follows the change."
        ),
        reference="Flavors and modification",
        hint=(
            "+= on a simply expanded variable appends the already expanded "
            "text; on a recursive variable it appends the raw text, which is "
            "expanded again on every use."
        ),
        makefile="""
source = early

# Recursive: += appends the text $(source), expanded when used.
recursive = $(source)
recursive += $(source)

# Simply expanded: += appends the current value of $(source).
simple := $(source)
simple += $(source)

source = late

all:
\techo recursive: $(recursive)
\techo simple: $(simple)
""",
        steps=[
            mk(
                stdout=(
                    "echo recursive: late late\n"
                    "recursive: late late\n"
                    "echo simple: early early\n"
                    "simple: early early"
                ),
                description="the two flavours appended different things",
            ),
        ],
        breaks=[("simple := $(source)", "simple = $(source)")],
    ),
    ex(
        topic=TOPIC,
        slug="04_default_with_question_mark",
        title="?= sets a default only when the variable is undefined",
        objective=(
            "Give one variable a default without clobbering the value it "
            "already has, and let a brand new variable take the default."
        ),
        reference="Flavors and modification",
        hint=(
            "?= assigns only if the variable has no value yet. A plain = "
            "always assigns, which would overwrite the earlier definition."
        ),
        makefile="""
one = hello
one ?= will not be set
two ?= will be set

all:
\techo one is $(one)
\techo two is $(two)
""",
        steps=[
            mk(
                stdout="echo one is hello\none is hello\necho two is will be set\ntwo is will be set",
                description="the existing value survived and the new one got its default",
            ),
            mk(
                "two=from the command line",
                stdout="two is from the command line",
                description=(
                    "a variable given on the command line counts as defined, "
                    "so ?= leaves it alone"
                ),
            ),
        ],
        breaks=[("one ?= will not be set", "one = will not be set")],
    ),
    ex(
        topic=TOPIC,
        slug="05_spaces_and_the_null_string",
        title="Spaces at the ends of an assignment",
        objective=(
            "Build a value that ends in three spaces and a variable holding "
            "exactly one space, using the empty variable as the trick."
        ),
        reference="Flavors and modification",
        hint=(
            "Spaces before the = are stripped but spaces at the end of the "
            "line are kept, comment or not. Set an empty variable and put a "
            "space before the # when you need one space."
        ),
        makefile="""
# The three spaces before the comment are part of the value.
with_spaces = hello   # three spaces live here
after = $(with_spaces)there

nullstring =
space = $(nullstring) # one space, thanks to the space before the comment

all:
\techo "$(after)"
\techo start"$(space)"end
""",
        steps=[
            mk(
                stdout='echo "hello   there"\nhello   there',
                description="the trailing spaces survived and the leading space did not",
            ),
            mk(
                stdout='echo start" "end\nstart end',
                description="the single space variable puts one space between start and end",
            ),
        ],
        breaks=[("space = $(nullstring) # one space, thanks to the space before the comment", "space = $(nullstring)")],
    ),
    ex(
        topic=TOPIC,
        slug="06_undefined_is_empty",
        title="An undefined variable is an empty string",
        objective=(
            "Append a variable that nothing defines to a flag list, and "
            "confirm it contributes nothing until a value is supplied."
        ),
        reference="Flavors and modification",
        hint=(
            "$(NAME) of a variable nobody set expands to nothing at all, so "
            "appending it is harmless. Writing the name without $() makes it "
            "literal text instead."
        ),
        makefile="""
CFLAGS := -Wall
# EXTRA_CFLAGS is never defined anywhere in this Makefile.
CFLAGS += $(EXTRA_CFLAGS)

all:
\techo "cflags: $(CFLAGS)"
""",
        steps=[
            mk(
                stdout='echo "cflags: -Wall"\ncflags: -Wall',
                description="the undefined variable added nothing",
            ),
            mk(
                "EXTRA_CFLAGS=-Wextra",
                stdout='echo "cflags: -Wall -Wextra"\ncflags: -Wall -Wextra',
                description="supplying the variable on the command line fills the hole",
            ),
        ],
        breaks=[("CFLAGS += $(EXTRA_CFLAGS)", "CFLAGS += EXTRA_CFLAGS")],
    ),
    ex(
        topic=TOPIC,
        slug="07_substitution_references",
        title="Substitution references",
        objective=(
            "Turn a list of object files into the matching source files with "
            "the suffix shorthand and with the explicit pattern form."
        ),
        reference="Flavors and modification",
        hint=(
            "$(objects:.o=.c) swaps the suffix of every word that has it. "
            "$(objects:%.o=%.c) is the same idea written as a pattern, where "
            "the % carries the part of the word in front of .o."
        ),
        makefile="""
objects := a.o b.o l.a c.o

# The suffix shorthand: every word ending in .o loses it and gains .c.
sources := $(objects:.o=.c)
# The same substitution written with an explicit pattern.
via_pattern := $(objects:%.o=%.c)
# The long form of the same thing.
via_patsubst := $(patsubst %.o,%.c,$(objects))

all:
\techo sources: $(sources)
\techo via_pattern: $(via_pattern)
\techo via_patsubst: $(via_patsubst)
""",
        steps=[
            mk(
                stdout=(
                    "echo sources: a.c b.c l.a c.c\n"
                    "sources: a.c b.c l.a c.c\n"
                    "echo via_pattern: a.c b.c l.a c.c\n"
                    "via_pattern: a.c b.c l.a c.c\n"
                    "echo via_patsubst: a.c b.c l.a c.c\n"
                    "via_patsubst: a.c b.c l.a c.c"
                ),
                description="all three spellings produce the same list",
            ),
        ],
        breaks=[("via_pattern := $(objects:%.o=%.c)", "via_pattern := $(objects:%.c=%.o)")],
    ),
    ex(
        topic=TOPIC,
        slug="08_command_line_beats_plain_assignment",
        title="A plain assignment loses to the command line",
        objective=(
            "Make the build mode a default that any value passed on the "
            "command line can replace, while a bare make still uses it."
        ),
        reference="Command line arguments and override",
        hint=(
            "Values given on the command line win over every ordinary "
            "assignment in the Makefile. Drop the override keyword and the "
            "command line takes over again."
        ),
        makefile="""
# A plain assignment is only a default.
mode = debug

all:
\techo mode is $(mode)
""",
        steps=[
            mk(
                stdout="echo mode is debug\nmode is debug",
                description="a bare make uses the Makefile's value",
            ),
            mk(
                "mode=release",
                stdout="echo mode is release\nmode is release",
                description="the command line replaces it",
            ),
            mk(
                "mode=fast",
                stdout="mode is fast",
                description="any command line value wins, not just one particular one",
            ),
        ],
        breaks=[("mode = debug", "override mode = debug")],
    ),
    ex(
        topic=TOPIC,
        slug="09_override_wins",
        title="override beats the command line",
        objective=(
            "Force one variable to keep the Makefile's own value no matter "
            "what the command line says, while the variable next to it is "
            "still replaceable."
        ),
        reference="Command line arguments and override",
        hint=(
            "Put override in front of the assignment. Assignments without it "
            "keep losing to the command line, which is exactly what the "
            "second variable should do."
        ),
        makefile="""
# override wins over a value given on the command line.
override mode = release
# A plain assignment would lose here.
plain = from the Makefile

all:
\techo mode is $(mode)
\techo plain is $(plain)
""",
        steps=[
            mk(
                stdout="echo mode is release\nmode is release\necho plain is from the Makefile\nplain is from the Makefile",
                description="without extra arguments both assignments are in charge",
            ),
            mk(
                "mode=debug",
                "plain=from the command line",
                stdout=(
                    "echo mode is release\n"
                    "mode is release\n"
                    "echo plain is from the command line\n"
                    "plain is from the command line"
                ),
                description="override held its ground, the plain assignment did not",
            ),
        ],
        breaks=[("override mode = release", "mode = release")],
    ),
    ex(
        topic=TOPIC,
        slug="10_environment_wins_with_dash_e",
        title="make -e lets the environment win",
        objective=(
            "Keep the Makefile's value in charge by default, let the "
            "environment take over when make runs with -e, and check that "
            "even then the command line still wins."
        ),
        reference="Command line arguments and override",
        hint=(
            "?= would hand the win to the environment always, because an "
            "exported variable already counts as defined. A plain = plus "
            "-e is the way to make the switch happen only when asked."
        ),
        makefile="""
# Without -e this wins; with -e the environment wins instead.
mode = makefile

all:
\techo mode is $(mode)
""",
        steps=[
            mk(
                stdout="echo mode is makefile\nmode is makefile",
                env={"mode": "environment"},
                description="the Makefile beats the environment by default",
            ),
            mk(
                "-e",
                stdout="echo mode is environment\nmode is environment",
                env={"mode": "environment"},
                description="-e flips the precedence",
            ),
            mk(
                "-e",
                "mode=command line",
                stdout="echo mode is command line\nmode is command line",
                env={"mode": "environment"},
                description="the command line outranks the environment even under -e",
            ),
        ],
        breaks=[("mode = makefile", "mode ?= makefile")],
    ),
    ex(
        topic=TOPIC,
        slug="11_define_holds_several_commands",
        title="define and endef hold a list of commands",
        objective=(
            "Put three commands into a single define variable and run them "
            "all from the recipe with one $(name) reference."
        ),
        reference="List of commands and define",
        hint=(
            "define name and endef wrap as many lines as you like; the "
            "variable is the whole block. Using it as a recipe line runs "
            "each of those lines in turn."
        ),
        makefile="""
name = makeling
version = 1.0
parts = core runner

define report
echo "name: $(name)"
echo "version: $(version)"
echo "parts: $(parts)"
endef

all:
\t$(report)
""",
        steps=[
            mk(
                stdout=(
                    'echo "name: makeling"\n'
                    "name: makeling\n"
                    'echo "version: 1.0"\n'
                    "version: 1.0\n"
                    'echo "parts: core runner"\n'
                    "parts: core runner"
                ),
                description="one $(report) reference ran all three commands",
            ),
        ],
        breaks=[
            (
                'define report\necho "name: $(name)"\necho "version: $(version)"\necho "parts: $(parts)"\nendef',
                'report = echo "name: $(name)"',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="12_define_and_separate_shells",
        title="Each line of a command list is its own shell",
        objective=(
            "Keep a one-line variable that exports and prints in a single "
            "shell, and a define block that exports and prints in two, and "
            "show which one actually prints the value."
        ),
        reference="List of commands and define",
        hint=(
            "A semicolon keeps two commands in one shell, so the export is "
            "still visible. Two lines of a define become two recipe lines, "
            "and each recipe line gets a fresh shell."
        ),
        makefile="""
one = export blah="I was set!"; echo $$blah

define two
export blah="I was set!"
echo $$blah
endef

all:
\t@echo "one is a single line, so its shell keeps the export"
\t@$(one)
\t@echo "two spans two lines, so the export is gone by the second one"
\t@$(two)
""",
        steps=[
            mk(
                stdout=(
                    "one is a single line, so its shell keeps the export\n"
                    "I was set!\n"
                    "two spans two lines, so the export is gone by the second one"
                ),
                description="the single line printed the value, the two-line block did not",
            ),
        ],
        breaks=[('one = export blah="I was set!"; echo $$blah', 'one = export blah="I was set!"')],
    ),
    ex(
        topic=TOPIC,
        slug="13_target_specific_variable",
        title="A variable that belongs to one target",
        objective=(
            "Give the all target its own flavour without letting the other "
            "target see it."
        ),
        reference="Target-specific variables",
        hint=(
            "Write target: variable = value before the rule. Making the "
            "assignment global instead would let every target see it."
        ),
        makefile="""
all: flavor = vanilla

all:
\techo the all target uses $(flavor)

other:
\techo the other target sees [$(flavor)]
""",
        steps=[
            mk(
                stdout="echo the all target uses vanilla\nthe all target uses vanilla",
                description="the all target sees its own variable",
            ),
            mk(
                "other",
                stdout="echo the other target sees []\nthe other target sees []",
                description="the sibling target does not",
            ),
            mk(
                "all",
                "other",
                stdout=(
                    "echo the all target uses vanilla\n"
                    "the all target uses vanilla\n"
                    "echo the other target sees []\n"
                    "the other target sees []"
                ),
                description="asking for both in one run does not blur the two",
            ),
        ],
        breaks=[("all: flavor = vanilla", "flavor = vanilla")],
    ),
    ex(
        topic=TOPIC,
        slug="14_target_specific_reaches_prerequisites",
        title="The variable reaches the prerequisites too",
        objective=(
            "Declare the variable on all so that the target it depends on "
            "inherits it, while the same target built on its own does not."
        ),
        reference="Target-specific variables",
        hint=(
            "A target-specific variable is inherited by everything all "
            "depends on, but only while all is being built. Naming the "
            "prerequisite directly on the command line skips all."
        ),
        makefile="""
all: flavor = vanilla

all: cake

cake:
\techo cake is baked with [$(flavor)]

other:
\techo other is baked with [$(flavor)]
""",
        steps=[
            mk(
                stdout="echo cake is baked with [vanilla]\ncake is baked with [vanilla]",
                description="the prerequisite inherited the value from all",
            ),
            mk(
                "cake",
                stdout="echo cake is baked with []\ncake is baked with []",
                description="built directly, cake has no flavour of its own",
            ),
            mk(
                "other",
                stdout="echo other is baked with []\nother is baked with []",
                description="an unrelated target is untouched",
            ),
        ],
        breaks=[("all: flavor = vanilla", "cake: flavor = vanilla")],
    ),
    ex(
        topic=TOPIC,
        slug="15_pattern_specific_variable",
        title="A variable that belongs to a pattern",
        objective=(
            "Attach a variable to every target ending in .c, so that blah.c "
            "sees it and other targets do not."
        ),
        reference="Pattern-specific variables",
        hint=(
            "Write %.c: variable = value. The target has to match the "
            "pattern for the variable to apply, so a pattern of %.o would "
            "leave blah.c without it."
        ),
        makefile="""
%.c: compiler = clang

blah.c:
\techo blah.c is built by $(compiler)

other:
\techo other is built by [$(compiler)]
""",
        steps=[
            mk(
                "blah.c",
                stdout="echo blah.c is built by clang\nblah.c is built by clang",
                description="blah.c matches the pattern and sees the value",
            ),
            mk(
                "other",
                stdout="echo other is built by []\nother is built by []",
                description="a target that does not match the pattern sees nothing",
            ),
        ],
        breaks=[("%.c: compiler = clang", "%.o: compiler = clang")],
    ),
    ex(
        topic=TOPIC,
        slug="16_pattern_and_target_specific_together",
        title="Target-specific beats pattern-specific",
        objective=(
            "Let a pattern give every .o file a mode, then give one of them "
            "its own value, and leave a third target with neither."
        ),
        reference="Pattern-specific variables",
        hint=(
            "Both forms can be in the file at once; the one naming the exact "
            "target takes precedence over the one matching the pattern."
        ),
        makefile="""
%.o: mode = pattern

foo.o: mode = target

foo.o:
\techo foo.o uses $(mode)

bar.o:
\techo bar.o uses $(mode)

plain:
\techo plain uses [$(mode)]
""",
        steps=[
            mk(
                "foo.o",
                stdout="echo foo.o uses target\nfoo.o uses target",
                description="the exact target wins over the pattern",
            ),
            mk(
                "bar.o",
                stdout="echo bar.o uses pattern\nbar.o uses pattern",
                description="a target that only matches the pattern uses it",
            ),
            mk(
                "plain",
                stdout="echo plain uses []\nplain uses []",
                description="a target that does neither gets nothing",
            ),
        ],
        breaks=[("foo.o: mode = target", "foo.o: mode = pattern")],
    ),
]
