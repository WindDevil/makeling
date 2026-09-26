"""Exercises for the tutorial's "Variables" and "Automatic Variables" chapters.

Recipe lines inside the ``makefile`` strings are indented with a ``\\t`` escape.
Python turns that into a real tab, which is what make requires; writing a
literal tab into the source would be invisible and easy to lose.  A literal
backslash that has to reach the Makefile (the ``\\n`` in printf's format, for
instance) is written as a doubled backslash in the Python source.
"""

from spec import ex, mk, step

TOPIC = "03_variables"


def lines(*items: str) -> str:
    """Several expected output lines that must appear in this order."""
    return "\n".join(items)


SPECS = [
    ex(
        topic=TOPIC,
        slug="01_a_list_in_a_variable",
        title="A list stored in a variable",
        objective=(
            "Keep the file names in a variable and use the same variable as "
            "the prerequisite list and inside the recipe."
        ),
        reference="Variables",
        hint=(
            "A variable is just a string. Everywhere make meets $(files) it "
            "substitutes that string, in the prerequisite list of the target "
            "line exactly as in the recipe."
        ),
        makefile="""
files := file1 file2

some_file: $(files)
\techo "Look at this variable: " $(files)
\ttouch some_file

file1:
\ttouch file1

file2:
\ttouch file2

clean:
\trm -f file1 file2 some_file
""",
        steps=[
            mk(
                stdout=lines(
                    "touch file1",
                    "touch file2",
                    'echo "Look at this variable: " file1 file2',
                    "Look at this variable:  file1 file2",
                    "touch some_file",
                ),
                description="the variable supplies prerequisites and message",
            ),
            mk(
                stdout="make: 'some_file' is up to date.",
                stdout_mode="contains",
                description="a second run finds the file already built",
            ),
            mk(
                "clean",
                stdout="rm -f file1 file2 some_file",
                missing=["file1", "file2", "some_file"],
                description="clean removes everything the variable named",
            ),
        ],
        breaks=[("some_file: $(files)", "some_file:")],
    ),
    ex(
        topic=TOPIC,
        slug="02_parens_or_braces",
        title="$(x) and ${x} mean the same thing",
        objective=(
            "Expand the same variable three ways: with parentheses, with "
            "braces, and with the bare $x form."
        ),
        reference="Variables",
        hint=(
            "$() and ${} are interchangeable; pick one and stay with it. The "
            "bare form only works for one-character names, which is why it is "
            "called bad practice."
        ),
        makefile="""
x := dude

all:
\techo "paren: $(x)"
\techo "brace: ${x}"

\t# Bad practice, but it works for a one-character name
\techo "bare: $x"
""",
        steps=[
            mk(
                stdout=lines("paren: dude", "brace: dude", "bare: dude"),
                description="all three spellings print the same value",
            ),
            mk(
                "all",
                stdout=lines("paren: dude", "brace: dude", "bare: dude"),
                description="naming the target changes nothing",
            ),
        ],
        breaks=[('echo "brace: ${x}"', 'echo "brace: ${y}"')],
    ),
    ex(
        topic=TOPIC,
        slug="03_quotes_are_characters",
        title="Quotes in a value are just characters",
        objective=(
            "Assign a quoted string to a variable and see that make keeps the "
            "quote characters while the shell uses them."
        ),
        reference="Variables",
        hint=(
            "Make has no quoting rules of its own: the quotes end up inside "
            "the value. When the recipe is handed to the shell the shell eats "
            "them, which is why $(b) arrives as one word."
        ),
        makefile="""
a := one two
b := 'one two'

all: args echoes

args:
\tprintf '[%s]\\n' $(a)
\tprintf '[%s]\\n' $(b)

echoes:
\techo $(b)
\techo "$(b)"
""",
        steps=[
            mk(
                "args",
                stdout=lines(
                    "printf '[%s]\\n' one two",
                    "[one]",
                    "[two]",
                    "printf '[%s]\\n' 'one two'",
                    "[one two]",
                ),
                description="the quotes travel with the value into the shell",
            ),
            mk(
                "echoes",
                stdout=lines("one two", "'one two'"),
                description="quoting the expansion keeps the quotes visible",
            ),
            mk(
                stdout=lines(
                    "[one]",
                    "[two]",
                    "[one two]",
                    "one two",
                    "'one two'",
                ),
                description="the default goal runs both rules",
            ),
        ],
        breaks=[("b := 'one two'", "b := one two")],
    ),
    ex(
        topic=TOPIC,
        slug="04_a_value_passed_to_a_program",
        title="Passing $(files) to a program",
        objective=(
            "Feed the value of a variable to printf and see that make splits "
            "it into words unless the expansion is quoted."
        ),
        reference="Variables",
        hint=(
            'The value of $(files) is the string "file1 file2". Unquoted it '
            "reaches printf as two arguments; put the expansion in double "
            "quotes to pass it as one."
        ),
        makefile="""
files := file1 file2

all:
\techo "list: $(files)"
\tprintf '[%s]\\n' $(files)
\tprintf '[%s]\\n' "$(files)"
""",
        steps=[
            mk(
                stdout=lines(
                    "list: file1 file2",
                    "[file1]",
                    "[file2]",
                    "printf '[%s]\\n' \"file1 file2\"",
                    "[file1 file2]",
                ),
                description="one unquoted expansion, two arguments",
            ),
            mk(
                stdout='printf \'[%s]\\n\' "file1 file2"',
                stdout_mode="contains",
                description="the quoted expansion arrives as a single word",
            ),
        ],
        breaks=[
            ('printf \'[%s]\\n\' "$(files)"', "printf '[%s]\\n' $(files)")
        ],
    ),
    ex(
        topic=TOPIC,
        slug="05_a_value_is_a_list_of_words",
        title="A value is a list of words",
        objective=(
            "Point a target at a variable whose value has irregular spacing "
            "and see make turn it into an ordinary word list."
        ),
        reference="Variables",
        hint=(
            "Make splits the value on any run of whitespace. The extra spaces "
            "and the variable expansion are both gone by the time $^ prints "
            "the prerequisite list."
        ),
        makefile="""
SRCS := one.c    two.c       three.c

prog: $(SRCS)
\techo "sources: $^"
\ttouch $@
""",
        steps=[
            mk(
                stdout=lines(
                    'echo "sources: one.c two.c three.c"',
                    "sources: one.c two.c three.c",
                    "touch prog",
                ),
                description="three words, whatever the spacing was",
            ),
            mk(
                stdout="make: 'prog' is up to date.",
                stdout_mode="contains",
                description="all three prerequisites exist and are older",
            ),
        ],
        breaks=[("prog: $(SRCS)", "prog: SRCS")],
        files={"one.c": "one\n", "two.c": "two\n", "three.c": "three\n"},
    ),
    ex(
        topic=TOPIC,
        slug="06_dir_notdir_basename_suffix",
        title="Taking a file name apart",
        objective=(
            "Apply $(dir), $(notdir), $(basename) and $(suffix) to one "
            "variable holding a list of paths."
        ),
        reference="Variables",
        hint=(
            "$(dir) keeps everything up to and including the last slash, "
            "$(notdir) keeps what follows it, $(basename) drops the suffix and "
            "$(suffix) keeps only the suffix."
        ),
        makefile="""
SRCS := src/foo.c src/bar.c

all:
\techo "dir: $(dir $(SRCS))"
\techo "notdir: $(notdir $(SRCS))"
\techo "basename: $(basename $(SRCS))"
\techo "suffix: $(suffix $(SRCS))"
""",
        steps=[
            mk(
                stdout=lines(
                    "dir: src/ src/",
                    "notdir: foo.c bar.c",
                    "basename: src/foo src/bar",
                    "suffix: .c .c",
                ),
                description="each function works word by word",
            ),
        ],
        breaks=[
            (
                'echo "basename: $(basename $(SRCS))"',
                'echo "basename: $(notdir $(SRCS))"',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="07_addprefix_and_addsuffix",
        title="Adding a prefix and a suffix to every word",
        objective=(
            "Use $(addprefix) and $(addsuffix) to build an object list and a "
            "backup list out of one source list."
        ),
        reference="Makefile Cookbook",
        hint=(
            "$(addprefix prefix,list) and $(addsuffix suffix,list) touch every "
            "word of the list. The prefix or the suffix comes first in the "
            "call; the list comes last."
        ),
        makefile="""
SRCS := main.c util.c
BUILD := build

OBJS := $(addprefix $(BUILD)/,$(SRCS))
BACKUPS := $(addsuffix .bak,$(SRCS))

all:
\techo "objs: $(OBJS)"
\techo "backups: $(BACKUPS)"
""",
        steps=[
            mk(
                stdout=lines(
                    "objs: build/main.c build/util.c",
                    "backups: main.c.bak util.c.bak",
                ),
                description="both functions walk the whole list",
            ),
        ],
        breaks=[
            (
                "OBJS := $(addprefix $(BUILD)/,$(SRCS))",
                "OBJS := $(addprefix $(SRCS),$(BUILD)/)",
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="08_substitution_reference",
        title="Substituting one suffix for another",
        objective=(
            "Turn a list of object files into the matching source list with "
            "the $(var:suffix=replacement) shorthand."
        ),
        reference="String Substitution",
        hint=(
            "$(foo:.o=.c) rewrites the ending .o of every word that has one, "
            "in place and in order. The suffix is a plain ending, not a "
            "pattern, so a word that ends differently is left alone."
        ),
        makefile="""
foo := a.o b.o l.a c.o

sources := $(foo:.o=.c)
elsewhere := $(foo:.a=.c)

all:
\techo "sources: $(sources)"
\techo "elsewhere: $(elsewhere)"
""",
        steps=[
            mk(
                stdout=lines(
                    "sources: a.c b.c l.a c.c",
                    "elsewhere: a.o b.o l.c c.o",
                ),
                description="only words with the named suffix are rewritten",
            ),
        ],
        breaks=[("sources := $(foo:.o=.c)", "sources := $(foo:.c=.o)")],
    ),
    ex(
        topic=TOPIC,
        slug="09_the_four_common_automatic_variables",
        title="$@, $?, $^ and $<",
        objective=(
            "Print the target name, the out-of-date prerequisites, every "
            "prerequisite, and the first prerequisite from one recipe."
        ),
        reference="Automatic Variables",
        hint=(
            "$@ is the target being built, $^ is every prerequisite, $< is "
            "just the first of them, and $? is the ones that are newer than "
            "the target."
        ),
        makefile="""
hey: one two
\techo "target: $@"
\techo "newer: $?"
\techo "all: $^"
\techo "first: $<"
\ttouch hey

one:
\ttouch one

two:
\ttouch two

clean:
\trm -f hey one two
""",
        steps=[
            mk(
                stdout=lines(
                    "touch one",
                    "touch two",
                    "target: hey",
                    "newer: one two",
                    "all: one two",
                    "first: one",
                    "touch hey",
                ),
                description="hey does not exist yet, so nothing is up to date",
            ),
            mk(
                stdout="make: 'hey' is up to date.",
                stdout_mode="contains",
                description="the recipe is skipped on the second run",
            ),
            mk(
                "clean",
                stdout="rm -f hey one two",
                missing=["hey", "one", "two"],
                description="clean removes the target and its prerequisites",
            ),
        ],
        breaks=[('echo "first: $<"', 'echo "first: $^"')],
    ),
    ex(
        topic=TOPIC,
        slug="10_only_the_newer_prerequisites",
        title="$? lists only what is out of date",
        objective=(
            "Make one of two prerequisites newer than the target and watch "
            "$? shrink while $^ stays the same."
        ),
        reference="Automatic Variables",
        hint=(
            "$^ and $< never change; $? reports only the prerequisites whose "
            "timestamp is newer than the target's, which is the list you would "
            "hand to a compiler."
        ),
        makefile="""
hey: one two
\techo "newer: $?"
\techo "all: $^"
\techo "first: $<"
\ttouch hey

one:
\ttouch one

two:
\ttouch two
""",
        steps=[
            mk(
                stdout=lines(
                    "touch one",
                    "touch two",
                    "newer: one two",
                    "all: one two",
                    "first: one",
                    "touch hey",
                ),
                description="with no target file every prerequisite counts",
            ),
            step(
                "touch",
                "one",
                description="make one of the two prerequisites newer",
            ),
            mk(
                stdout=lines(
                    "newer: one",
                    "all: one two",
                    "first: one",
                    "touch hey",
                ),
                description="$? now names just the newer prerequisite",
            ),
        ],
        breaks=[('echo "newer: $?"', 'echo "newer: $^"')],
    ),
    ex(
        topic=TOPIC,
        slug="11_one_rule_two_targets",
        title="One rule, several targets",
        objective=(
            "Write a single rule for f1.o and f2.o and let $@ name the output "
            "of each run."
        ),
        reference="Automatic Variables",
        hint=(
            "When a rule lists several targets, make runs the recipe once per "
            "target with $@ set to that target. That is what lets the same "
            "recipe build both files."
        ),
        makefile="""
all: f1.o f2.o

f1.o f2.o:
\techo "building $@"
\ttouch $@
""",
        steps=[
            mk(
                stdout=lines(
                    'echo "building f1.o"',
                    "building f1.o",
                    "touch f1.o",
                    'echo "building f2.o"',
                    "building f2.o",
                    "touch f2.o",
                ),
                description="the recipe runs once per target",
            ),
            step(
                "test",
                "-f",
                "f1.o",
                description="the first target was written to disk",
            ),
            step(
                "test",
                "-f",
                "f2.o",
                description="so was the second",
            ),
            mk(
                stdout="make: Nothing to be done for 'all'.",
                stdout_mode="contains",
                description="both files exist, so there is nothing left to do",
            ),
        ],
        breaks=[('echo "building $@"', 'echo "building $<"')],
    ),
    ex(
        topic=TOPIC,
        slug="12_target_directory_and_file",
        title="$(@D) and $(@F)",
        objective=(
            "Build a file inside a directory that does not exist yet, using "
            "$(@D) for the directory and $(@F) for the file name."
        ),
        reference="Automatic Variables",
        hint=(
            "$(@D) is the directory part of the target and $(@F) the file "
            "part. Create $(@D) first, then write into $@."
        ),
        makefile="""
out/nested/report.txt:
\tmkdir -p $(@D)
\techo $(@F) > $@
""",
        steps=[
            mk(
                stdout=lines(
                    "mkdir -p out/nested",
                    "echo report.txt > out/nested/report.txt",
                ),
                files={"out/nested/report.txt": "report.txt\n"},
                description="the directory is made before the file is written",
            ),
            mk(
                stdout="make: 'out/nested/report.txt' is up to date.",
                stdout_mode="contains",
                description="the second run has nothing to do",
            ),
        ],
        breaks=[("echo $(@F) > $@", "echo $(@D) > $@")],
    ),
    ex(
        topic=TOPIC,
        slug="13_the_stem_variable",
        title="$* is the stem",
        objective=(
            "Print $* for a target that ends in a known suffix and for one "
            "that does not."
        ),
        reference="Automatic Variables",
        hint=(
            "$* is the target name with a known suffix removed, so foo.o gives "
            "foo. A target without a recognised suffix, like prog, gives an "
            "empty $*."
        ),
        makefile="""
all: foo.o prog

foo.o: foo.c
\techo "stem of foo.o: [$*]"
\ttouch $@

prog: prog.c
\techo "stem of prog: [$*]"
\ttouch $@
""",
        steps=[
            mk(
                stdout=lines(
                    "stem of foo.o: [foo]",
                    "touch foo.o",
                    "stem of prog: []",
                    "touch prog",
                ),
                description="one target has a stem, the other does not",
            ),
            mk(
                stdout="make: Nothing to be done for 'all'.",
                stdout_mode="contains",
                description="both outputs exist on the second run",
            ),
        ],
        breaks=[('echo "stem of foo.o: [$*]"', 'echo "stem of foo.o: [$<]"')],
        files={"foo.c": "/* foo */\n", "prog.c": "/* prog */\n"},
    ),
    ex(
        topic=TOPIC,
        slug="14_first_prerequisite_only",
        title="$< is the first prerequisite",
        objective=(
            "Copy the first of two prerequisites into the target while still "
            "reporting all of them."
        ),
        reference="Automatic Variables",
        hint=(
            "With several prerequisites $< is the first one on the target "
            "line, not all of them; $^ is the whole list. Two arguments to cp "
            "would be a mistake."
        ),
        makefile="""
out.txt: a.txt b.txt
\tcp $< $@
\techo "inputs: $^" >> $@
\tcat $@
""",
        steps=[
            mk(
                stdout=lines(
                    "cp a.txt out.txt",
                    'echo "inputs: a.txt b.txt" >> out.txt',
                    "from a",
                    "inputs: a.txt b.txt",
                ),
                files={"out.txt": "from a\ninputs: a.txt b.txt\n"},
                description="the copy came from a.txt, the report lists both",
            ),
            mk(
                stdout="make: 'out.txt' is up to date.",
                stdout_mode="contains",
                description="nothing changed, so nothing is rebuilt",
            ),
            step(
                "touch",
                "b.txt",
                description="make the second prerequisite newer",
            ),
            mk(
                stdout="cp a.txt out.txt",
                description="the recipe runs again, still copying the first",
            ),
        ],
        breaks=[("cp $< $@", "cp $^ $@")],
        files={"a.txt": "from a\n", "b.txt": "from b\n"},
    ),
]
