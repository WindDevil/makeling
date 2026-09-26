"""Exercises for the tutorial's "Conditional part of Makefiles" chapter.

Recipe lines inside the ``makefile`` strings are indented with a ``\\t`` escape.
Python turns that into a real tab, which is what make requires; writing a
literal tab into the source would be invisible and easy to lose.  Directive
lines (``ifeq``, ``else``, ``endif``) always start in column 1.
"""

from spec import ex, mk, step

TOPIC = "09_conditionals"

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_ifeq_else",
        title="Pick a recipe line with ifeq/else",
        objective=(
            "Branch on the value of foo so that make prints the matching "
            "message for both the file's value and an override on the "
            "command line."
        ),
        reference="Conditional if/else",
        hint=(
            "The else directive separates the two branches and endif closes "
            "the conditional. A make with an override needs the recipe that "
            "runs when the comparison fails, and that recipe is missing."
        ),
        makefile="""
foo = ok

all:
ifeq ($(foo), ok)
\techo "foo equals ok"
else
\techo "foo is not ok"
endif
""",
        steps=[
            mk(
                stdout='echo "foo equals ok"\nfoo equals ok',
                description="foo is ok, so the first branch runs",
            ),
            mk(
                "foo=nope",
                stdout='echo "foo is not ok"\nfoo is not ok',
                description="a command line override selects the else branch",
            ),
        ],
        breaks=[
            (
                'else\n\techo "foo is not ok"\nendif',
                'endif',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="02_branches_choose_rules",
        title="A conditional chooses which rules exist",
        objective=(
            "Let the conditional decide which rule the Makefile contains, so "
            "that make debug builds when MODE is debug and make release "
            "builds when MODE is release."
        ),
        reference="Conditional if/else",
        hint=(
            "Conditionals are not recipe text: they decide which lines of the "
            "file make reads at all. Put the ifeq around the whole rules, so "
            "that the target that is not selected does not exist."
        ),
        makefile="""
MODE = debug

ifeq ($(MODE),debug)
debug:
\techo "building debug"
else
release:
\techo "building release"
endif
""",
        steps=[
            mk(
                "debug",
                stdout='echo "building debug"\nbuilding debug',
                description="MODE is debug, so the debug rule exists",
            ),
            mk(
                "release",
                exit_code=2,
                stderr="No rule to make target 'release'",
                description="the release rule was never parsed, so it is unknown",
            ),
            mk(
                "MODE=release",
                "release",
                stdout='echo "building release"\nbuilding release',
                description="a command line MODE selects the other rule",
            ),
        ],
        breaks=[
            (
                "ifeq ($(MODE),debug)\ndebug:\n\techo \"building debug\"\n"
                "else\nrelease:\n\techo \"building release\"\nendif",
                "debug:\nifeq ($(MODE),debug)\n\techo \"building debug\"\n"
                "else\n\techo \"building release\"\nendif",
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="03_parsed_top_to_bottom",
        title="The conditional is decided while the file is read",
        objective=(
            "Assign MODE before the conditional that tests it, so that a bare "
            "make reports the debug build."
        ),
        reference="Conditional if/else",
        hint=(
            "make reads the file from the first line to the last and resolves "
            "each conditional the moment it reaches it. An assignment further "
            "down the file has not happened yet."
        ),
        makefile="""
MODE = debug

all:
ifeq ($(MODE),debug)
\techo "debug build"
else
\techo "release build"
endif
""",
        steps=[
            mk(
                stdout='echo "debug build"\ndebug build',
                description="the assignment is above the conditional",
            ),
            mk(
                "MODE=release",
                stdout='echo "release build"\nrelease build',
                description="a command line value is known before parsing starts",
            ),
        ],
        breaks=[
            (
                'MODE = debug\n\nall:\nifeq ($(MODE),debug)\n\techo "debug build"\n'
                'else\n\techo "release build"\nendif',
                'all:\nifeq ($(MODE),debug)\n\techo "debug build"\n'
                'else\n\techo "release build"\nendif\n\nMODE = debug',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="04_both_sides_expanded",
        title="ifeq expands both arguments",
        objective=(
            "Compare two variables whose values are themselves variable "
            "references, so that the branch is taken."
        ),
        reference="Conditional if/else",
        hint=(
            "ifeq expands its two arguments before comparing them, so a "
            "variable that holds a reference to another one is followed. "
            "Writing the argument without $(...) compares it as literal text."
        ),
        makefile="""
flavour = chocolate
choice = $(flavour)
default = $(choice)

all:
ifeq ($(default),$(flavour))
\techo "left and right are both expanded"
else
\techo "the two sides differ"
endif
""",
        steps=[
            mk(
                stdout=(
                    'echo "left and right are both expanded"\n'
                    "left and right are both expanded"
                ),
                description="both sides expand to chocolate",
            ),
            mk(
                stdout="the two sides differ",
                stdout_mode="not_contains",
                description="the else branch is skipped",
            ),
        ],
        breaks=[("ifeq ($(default),$(flavour))", "ifeq ($(default),flavour)")],
    ),
    ex(
        topic=TOPIC,
        slug="05_quoting",
        title="Quotes in an ifeq comparison",
        objective=(
            "Write the comparisons so that quoting both sides matches and "
            "quoting only one side does not."
        ),
        reference="Conditional if/else",
        hint=(
            "Inside ifeq (...) the two arguments are compared as text, so a "
            "quote is just another character: ('ok',\"ok\") never matches, "
            "because 'ok' and \"ok\" are different strings. Quote both sides "
            "or neither."
        ),
        makefile="""
a = ok
b = ok

all:
ifeq ($(a),$(b))
\techo "plain comparison matches"
endif
ifeq ("$(a)","$(b)")
\techo "quoting both sides matches"
endif
ifeq "$(a)" "$(b)"
\techo "the space separated quoted form works"
endif
ifeq ('$(a)',"$(b)")
\techo "mixed quotes match"
else
\techo "a quote is a literal character"
endif
""",
        steps=[
            mk(
                stdout=(
                    "plain comparison matches\n"
                    "quoting both sides matches\n"
                    "the space separated quoted form works\n"
                    "a quote is a literal character"
                ),
                description="only the balanced comparisons match",
            ),
            mk(
                stdout="mixed quotes match",
                stdout_mode="not_contains",
                description="a single quoted side is not equal to an unquoted one",
            ),
        ],
        breaks=[("ifeq ('$(a)',\"$(b)\")", "ifeq ('$(a)','$(b)')")],
    ),
    ex(
        topic=TOPIC,
        slug="06_spaces_in_the_values",
        title="Commas separate, spaces do not",
        objective=(
            "Compare a value that itself contains a space, and rely on the "
            "space after the comma being ignored."
        ),
        reference="Conditional if/else",
        hint=(
            "The comma is the only separator ifeq knows about, so the space "
            "in the tutorial's 'ifeq ($(foo), ok)' is decoration. A space "
            "that belongs to a value is compared like any other character."
        ),
        makefile="""
name = Grace Hopper
lang = c

all:
ifeq ($(name),Grace Hopper)
\techo "a space inside a value is compared"
endif
ifeq ($(lang), c)
\techo "the space after the comma is ignored"
endif
""",
        steps=[
            mk(
                stdout=(
                    "a space inside a value is compared\n"
                    "the space after the comma is ignored"
                ),
                description="both conditionals are true",
            ),
        ],
        breaks=[("ifeq ($(name),Grace Hopper)", "ifeq ($(name),Grace)")],
    ),
    ex(
        topic=TOPIC,
        slug="07_ifneq",
        title="ifneq runs when the values differ",
        objective=(
            "Use ifneq to choose the architecture message, for both the "
            "file's value of arch and an override on the command line."
        ),
        reference="Conditional if/else",
        hint=(
            "ifneq is the negation of ifeq: its text-if-true is read when the "
            "two arguments are not equal. The else branch covers the equal "
            "case."
        ),
        makefile="""
os = linux
arch = x86

all:
ifneq ($(os),windows)
\techo "using unix paths"
endif
ifneq ($(arch),x86)
\techo "64 bit build"
else
\techo "32 bit build"
endif
""",
        steps=[
            mk(
                stdout="using unix paths\n32 bit build",
                description="linux is not windows, and arch equals x86",
            ),
            mk(
                "arch=arm64",
                stdout="using unix paths\n64 bit build",
                description="the command line value makes ifneq true",
            ),
        ],
        breaks=[("ifneq ($(arch),x86)", "ifeq ($(arch),x86)")],
    ),
    ex(
        topic=TOPIC,
        slug="08_ifdef_and_ifndef",
        title="ifdef and ifndef",
        objective=(
            "Report that foo is defined even though its value is a reference "
            "to the empty variable bar, and that bar itself is not."
        ),
        reference="Check if a variable is defined",
        hint=(
            "ifdef and ifndef take a variable name, not a $(...) reference. "
            "foo was assigned something, so ifdef foo is true; bar was "
            "assigned the empty string, so ifndef bar is true."
        ),
        makefile="""
bar =
foo = $(bar)

all:
ifdef foo
\techo "foo is defined"
endif
ifndef bar
\techo "but bar is not"
endif
""",
        steps=[
            mk(
                stdout='echo "foo is defined"\nfoo is defined\nbut bar is not',
                description="both conditionals are true",
            ),
        ],
        breaks=[("ifndef bar", "ifdef bar")],
    ),
    ex(
        topic=TOPIC,
        slug="09_ifdef_does_not_expand",
        title="ifdef looks at the text, ifeq at the value",
        objective=(
            "Show both sides of the trap: an empty variable and an undefined "
            "one compare equal, while ifdef still calls foo set."
        ),
        reference="Check if a variable is defined",
        hint=(
            "ifeq expands its arguments, so $(foo) turns into nothing and an "
            "unassigned name looks exactly the same to it. ifdef expands "
            "nothing: it asks whether the text make recorded for foo is a "
            "non-empty string, and '$(bar)' is one."
        ),
        makefile="""
bar =
foo = $(bar)
empty =
# never_set is not assigned anywhere in this file

all:
ifeq ($(foo),)
\techo "ifeq expands the value and finds it empty"
else
\techo "ifeq found something"
endif
ifeq ($(empty),$(never_set))
\techo "ifeq cannot tell an empty variable from an undefined one"
endif
ifdef foo
\techo "ifdef reads the unexpanded value and finds it set"
else
\techo "ifdef found nothing"
endif
""",
        steps=[
            mk(
                stdout=(
                    "ifeq expands the value and finds it empty\n"
                    "ifeq cannot tell an empty variable from an undefined one\n"
                    "ifdef reads the unexpanded value and finds it set"
                ),
                description="all three conditionals are true",
            ),
            mk(
                stdout="ifeq found something\nifdef found nothing",
                stdout_mode="not_contains",
                description="neither inactive branch is taken",
            ),
        ],
        breaks=[("ifdef foo", "ifndef foo")],
    ),
    ex(
        topic=TOPIC,
        slug="10_empty_means_stripped",
        title="Check whether a variable is empty",
        objective=(
            "Use the $(strip) idiom to recognise that foo holds only a "
            "space, and still detect a variable that was never given a value."
        ),
        reference="Check if a variable is empty",
        hint=(
            "The space before the # is part of the value, so $(foo) is a "
            "single space and does not equal the empty string. $(strip) "
            "removes the surrounding whitespace before the comparison."
        ),
        makefile="""
nullstring =
foo = $(nullstring) # end of line; there is a space here

all:
ifeq ($(strip $(foo)),)
\techo "foo is empty after being stripped"
else
\techo "foo is not empty"
endif
ifeq ($(foo),)
\techo "foo is empty without stripping"
else
\techo "without strip, foo holds only a space"
endif
ifeq ($(nullstring),)
\techo "nullstring doesn't even have spaces"
endif
""",
        steps=[
            mk(
                stdout=(
                    "foo is empty after being stripped\n"
                    "without strip, foo holds only a space\n"
                    "nullstring doesn't even have spaces"
                ),
                description="strip sees through the space, the blunt test does not",
            ),
            mk(
                stdout="foo is empty without stripping\nfoo is not empty",
                stdout_mode="not_contains",
                description="the naive comparison is not the one that is taken",
            ),
        ],
        breaks=[("ifeq ($(strip $(foo)),)", "ifeq ($(foo),)")],
    ),
    ex(
        topic=TOPIC,
        slug="11_whitespace_is_not_empty",
        title="A value of only whitespace is not empty",
        objective=(
            "Show that ifdef is true for a variable whose value is one space, "
            "while ifeq only sees it as empty once it is stripped."
        ),
        reference="Check if a variable is defined",
        hint=(
            "padded holds one space, and a space is a non-empty value, so "
            "ifdef padded is true and ifeq ($(padded),) is false. Only the "
            "stripped comparison is true."
        ),
        makefile="""
space =
padded = $(space) # the space before this comment is part of the value

all:
ifdef padded
\techo "ifdef sees a non-empty value"
else
\techo "ifdef sees nothing"
endif
ifeq ($(padded),)
\techo "ifeq says padded is empty"
else
\techo "ifeq says padded is not empty"
endif
ifeq ($(strip $(padded)),)
\techo "only strip says it is empty"
endif
""",
        steps=[
            mk(
                stdout=(
                    "ifdef sees a non-empty value\n"
                    "ifeq says padded is not empty\n"
                    "only strip says it is empty"
                ),
                description="all three conditionals are true",
            ),
            mk(
                stdout="ifdef sees nothing\nifeq says padded is empty",
                stdout_mode="not_contains",
                description="the whitespace is never mistaken for emptiness",
            ),
        ],
        breaks=[("ifdef padded", "ifdef space")],
    ),
    ex(
        topic=TOPIC,
        slug="12_makeflags_detecting_i",
        title="Detect the -i flag through $(MAKEFLAGS)",
        objective=(
            "Print the message when the user passed -i, and stay quiet "
            "otherwise, by searching $(MAKEFLAGS) for the letter."
        ),
        reference="$(MAKEFLAGS)",
        hint=(
            "MAKEFLAGS is a string of single letters, one per flag, without "
            "the leading dash. $(findstring i,$(MAKEFLAGS)) returns i when "
            "the flag is present and the empty string when it is not, so "
            "ifneq (,$(findstring ...)) is the test to write."
        ),
        makefile="""
all:
ifneq (,$(findstring i, $(MAKEFLAGS)))
\techo "i was passed to MAKEFLAGS"
else
\techo "no i in MAKEFLAGS"
endif
""",
        steps=[
            mk(
                stdout='echo "no i in MAKEFLAGS"\nno i in MAKEFLAGS',
                description="a bare make finds no i",
            ),
            mk(
                "-i",
                stdout='echo "i was passed to MAKEFLAGS"\ni was passed to MAKEFLAGS',
                description="make -i puts an i into MAKEFLAGS",
            ),
        ],
        breaks=[("ifneq (,$(findstring i, $(MAKEFLAGS)))", "ifeq (,$(findstring i, $(MAKEFLAGS)))")],
    ),
    ex(
        topic=TOPIC,
        slug="13_makeflags_silent",
        title="Detect silent mode",
        objective=(
            "Branch on whether -s was passed: bare make echoes the command, "
            "make -s only prints the message."
        ),
        reference="$(MAKEFLAGS)",
        hint=(
            "The letters in MAKEFLAGS carry no dash, so searching for -s "
            "never matches. Search for s on its own and compare the result "
            "with s."
        ),
        makefile="""
all:
ifeq ($(findstring s,$(MAKEFLAGS)),s)
\techo "silent mode"
else
\techo "echoing commands"
endif
""",
        steps=[
            mk(
                stdout='echo "echoing commands"\nechoing commands',
                description="without -s make echoes the recipe line too",
            ),
            mk(
                "-s",
                stdout="silent mode",
                description="with -s the conditional takes the other branch",
            ),
            mk(
                "-s",
                stdout='echo "silent mode"',
                stdout_mode="not_contains",
                description="-s really suppressed the recipe echo",
            ),
        ],
        breaks=[("$(findstring s,$(MAKEFLAGS))", "$(findstring -s,$(MAKEFLAGS))")],
    ),
    ex(
        topic=TOPIC,
        slug="14_shell_and_command_line",
        title="A conditional fed by $(shell)",
        objective=(
            "Probe the filesystem with $(shell) and pick the value with ifeq, "
            "letting the probed file name come from the command line."
        ),
        reference="Conditional if/else",
        hint=(
            "$(shell ...) runs while make parses the file and its output is "
            "compared as text, so the conditional decides the branch before "
            "any target is built. A variable set on the command line "
            "overrides the file's assignment, so PROBE=absent.mk probes a "
            "different file."
        ),
        makefile="""
PROBE = local.mk

ifeq ($(shell test -f $(PROBE) && echo yes),yes)
RESULT = found
else
RESULT = missing
endif

all:
\t@echo "result: $(RESULT)"
""",
        steps=[
            mk(
                stdout="result: found",
                description="local.mk exists, so the shell prints yes",
            ),
            mk(
                "PROBE=absent.mk",
                stdout="result: missing",
                description="the command line probes a file that is not there",
            ),
        ],
        breaks=[
            (
                "RESULT = found\nelse\nRESULT = missing",
                "RESULT = missing\nelse\nRESULT = found",
            )
        ],
        files={"local.mk": "NAME = local\n"},
    ),
]
