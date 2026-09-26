"""Exercises for the tutorial's "Fancy Rules" chapter.

Recipe lines inside the ``makefile`` strings are indented with a ``\\t`` escape.
Python turns that into a real tab, which is what make requires; writing a
literal tab into the source would be invisible and easy to lose.
"""

from spec import ex, mk, step

TOPIC = "06_fancy_rules"

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_implicit_link_rule",
        title="make compiles and links without a recipe",
        objective=(
            "Ask for an executable called blah without writing a single "
            "recipe, and let make's built-in C rules do the compiling and "
            "the linking."
        ),
        reference="Implicit Rules",
        hint=(
            "Naming blah.o as a prerequisite is enough: make links blah from "
            "blah.o with one built-in rule and compiles blah.o from blah.c "
            "with another. Write the dependency, not the commands."
        ),
        makefile="""
# Nothing in this file says how to compile or how to link.  make's
# built-in "implicit" rules supply both recipes because blah.c exists.
blah: blah.o
""",
        steps=[
            mk(
                stdout=r"cc\s+-c -o blah\.o blah\.c\ncc\s+blah\.o\s+-o blah",
                stdout_mode="regex",
                description="the compile rule runs, then the linker rule",
            ),
            step(
                "test",
                "-f",
                "blah.o",
                description="the implicit compile rule produced blah.o",
            ),
            step(
                "test",
                "-x",
                "blah",
                description="the implicit linker rule produced the program",
            ),
            mk(
                stdout="make: 'blah' is up to date.",
                stdout_mode="contains",
                description="a second run has nothing left to do",
            ),
        ],
        breaks=[("blah: blah.o", "blah:")],
        files={"blah.c": "int main(void) { return 0; }\n"},
    ),
    ex(
        topic=TOPIC,
        slug="02_generate_source_with_rule",
        title="A rule that writes the C source",
        objective=(
            "Let make create blah.c with a rule of your own, then watch the "
            "built-in rules compile and link it using CFLAGS."
        ),
        reference="Implicit Rules",
        hint=(
            "blah.c does not exist yet, so it needs a rule that writes it; "
            "make still contributes the compile and link recipes itself.  "
            "CFLAGS is handed straight to the built-in compile rule."
        ),
        makefile="""
CFLAGS = -g

# Implicit rule #1: blah is built from blah.o by the C linker rule.
# Implicit rule #2: blah.o is built from blah.c by the C compile rule,
# because blah.c can be made.
blah: blah.o

blah.c:
\techo "int main() { return 0; }" > blah.c

clean:
\trm -f blah*
""",
        steps=[
            mk(
                stdout=r'blah\.c\ncc -g\s+-c -o blah\.o blah\.c\ncc\s+blah\.o\s+-o blah',
                stdout_mode="regex",
                description="the source is written, compiled and linked",
            ),
            step(
                "cat",
                "blah.c",
                stdout="int main() { return 0; }",
                stdout_mode="contains",
                description="the explicit rule wrote real source code",
            ),
            step("test", "-x", "blah", description="the linked program exists"),
            mk(
                stdout="make: 'blah' is up to date.",
                stdout_mode="contains",
                description="nothing is rebuilt on a second run",
            ),
            mk(
                "clean",
                stdout="rm -f blah*",
                missing=["blah", "blah.o", "blah.c"],
                description="clean removes the program and its source",
            ),
        ],
        breaks=[
            (
                'blah.c:\n\techo "int main() { return 0; }" > blah.c',
                "# TODO: nothing here knows how to create blah.c",
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="03_implicit_rule_variables",
        title="The variables behind the built-in rule",
        objective=(
            "Set CC, CFLAGS and CPPFLAGS so the built-in compile rule builds "
            "blah.o with exactly those flags, and read the command with make -n."
        ),
        reference="Implicit Rules",
        hint=(
            "The built-in rule for n.o expands to $(CC) $(CFLAGS) $(CPPFLAGS) "
            "-c -o $@ $<.  Run make -n blah.o to see that line without "
            "executing it, then run it for real."
        ),
        makefile="""
# The built-in C compile rule is
#   $(CC) $(CFLAGS) $(CPPFLAGS) -c -o $@ $<
CC = cc
CFLAGS = -Wall -g
CPPFLAGS = -DNDEBUG

# No recipe here: make supplies one from the variables above.
blah.o:
""",
        steps=[
            mk(
                "-n",
                "blah.o",
                stdout=r"cc -Wall -g -DNDEBUG\s+-c -o blah\.o blah\.c",
                stdout_mode="regex",
                missing=["blah.o"],
                description="make -n prints the implicit recipe without running it",
            ),
            mk(
                "blah.o",
                stdout=r"cc -Wall -g -DNDEBUG\s+-c -o blah\.o blah\.c",
                stdout_mode="regex",
                description="the real build expands the same three variables",
            ),
            step("test", "-f", "blah.o", description="the object file was produced"),
        ],
        breaks=[("CPPFLAGS = -DNDEBUG", "# TODO: no preprocessor flag is set")],
        files={"blah.c": "int main(void) { return 0; }\n"},
    ),
    ex(
        topic=TOPIC,
        slug="04_cancel_pattern_rule",
        title="Cancelling the built-in compile rule",
        objective=(
            "Cancel make's built-in %.o: %.c rule with an empty pattern rule, "
            "so that only the object files you build by hand can exist."
        ),
        reference="Implicit Rules",
        hint=(
            "An empty pattern rule with the same target and prerequisite "
            "patterns cancels the built-in one.  Afterwards make can only "
            "build an object file that has an explicit rule of its own."
        ),
        makefile="""
# An empty pattern rule cancels the built-in rule of the same shape, so
# make stops compiling .c files behind our back.
%.o: %.c

# The one object we want has to be spelled out now.
blah.o: blah.c
\t$(CC) -c $< -o $@

all: blah.o
""",
        steps=[
            mk(
                stdout="-c blah.c -o blah.o",
                stdout_mode="contains",
                description="the explicit recipe still builds blah.o",
            ),
            step("test", "-f", "blah.o", description="blah.o was produced"),
            mk(
                "other.o",
                exit_code=2,
                stderr="No rule to make target 'other.o'",
                stderr_mode="contains",
                description="no rule is left for any other object file",
            ),
        ],
        breaks=[("%.o: %.c", "# %.o: %.c")],
        files={
            "blah.c": "int main(void) { return 0; }\n",
            "other.c": "int other(void) { return 0; }\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="05_erase_suffixes",
        title="Erasing make's built-in suffix rules",
        objective=(
            "Empty the suffix list so make forgets how to compile and link C "
            "sources, and see that only explicit recipes are left."
        ),
        reference="Implicit Rules",
        hint=(
            "A .SUFFIXES line with no prerequisites erases the suffix list, "
            "and with it the built-in rules that hang off it.  After that "
            "make has no recipe for blah.o or for linking blah."
        ),
        makefile="""
# .SUFFIXES with no prerequisites erases the built-in suffix rules, and
# with them the C compile and link rules.
.SUFFIXES:

# With nothing built in, this object needs a recipe of its own.
blah.o: blah.c
\t$(CC) -c $< -o $@

all: blah.o
""",
        steps=[
            mk(
                stdout="-c blah.c -o blah.o",
                stdout_mode="contains",
                description="the explicit recipe builds blah.o",
            ),
            mk(
                "blah",
                exit_code=2,
                stderr="No rule to make target 'blah'",
                stderr_mode="contains",
                description="the built-in linker rule is gone as well",
            ),
            step("test", "-f", "blah.o", description="blah.o is still there"),
        ],
        breaks=[(".SUFFIXES:", "# .SUFFIXES:")],
        files={"blah.c": "int main(void) { return 0; }\n"},
    ),
    ex(
        topic=TOPIC,
        slug="06_static_pattern_objects",
        title="One static pattern rule for a list of objects",
        objective=(
            "Replace three hand-written object rules with a single static "
            "pattern rule over $(objects), and link them into a program."
        ),
        reference="Static Pattern Rules",
        hint=(
            "The syntax is targets...: target-pattern: prereq-patterns; the "
            "stem matched by %.o is put back where %.c says.  Give all.c real "
            "content, because the %.c pattern rule below only touches an "
            "empty file."
        ),
        makefile="""
objects = foo.o bar.o all.o

all: $(objects)
\t$(CC) $^ -o all

# targets...: target-pattern: prereq-patterns ...
# foo.o is matched by %.o, giving the stem "foo"; %.c then becomes foo.c.
$(objects): %.o: %.c
\t$(CC) -c $^ -o $@

# all.c does not use the %.c rule below: an explicit rule is a more
# specific match than a pattern rule, and make prefers the specific one.
all.c:
\techo "int main() { return 0; }" > all.c

%.c:
\ttouch $@

clean:
\trm -f *.c *.o all
""",
        steps=[
            mk(
                stdout=(
                    "cc -c foo.c -o foo.o\n"
                    "cc -c bar.c -o bar.o\n"
                    "cc -c all.c -o all.o\n"
                    "cc foo.o bar.o all.o -o all"
                ),
                description="one rule compiled all three objects, then the link ran",
            ),
            step(
                "test",
                "-x",
                "all",
                files={"all.c": "int main() { return 0; }"},
                description="all.c holds real code and all is an executable",
            ),
            step(
                "test",
                "!",
                "-s",
                "foo.c",
                description="foo.c came from the %.c rule, so it is empty",
            ),
            step("test", "-f", "bar.o", description="bar.o was compiled"),
            mk(
                "clean",
                stdout="rm -f *.c *.o all",
                missing=["all", "foo.c", "all.c"],
                description="clean removes every generated file",
            ),
        ],
        breaks=[
            (
                "# all.c does not use the %.c rule below: an explicit rule is a more\n"
                "# specific match than a pattern rule, and make prefers the specific one.\n"
                'all.c:\n\techo "int main() { return 0; }" > all.c',
                "# TODO: nothing writes all.c, so the %.c rule below touches it empty",
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="07_static_pattern_stem",
        title="The stem goes into the prerequisite pattern",
        objective=(
            "Turn a list of .txt files into .raw ones with a static pattern "
            "rule, and print the stem that %.txt matched."
        ),
        reference="Static Pattern Rules",
        hint=(
            "$* is the stem: for alpha.txt matched by %.txt it is alpha, and "
            "the same stem replaces the % in the prerequisite pattern %.raw.  "
            "The rule needs both pattern lines to line up."
        ),
        makefile="""
files = alpha.txt beta.txt

all: $(files)
\techo "built: $^"

# alpha.txt matches %.txt, so the stem is "alpha" and the prerequisite
# pattern %.raw turns into alpha.raw.
$(files): %.txt: %.raw
\techo "target $@ from prereq $< (stem $*)"
\tcp $< $@
""",
        steps=[
            mk(
                stdout=(
                    "target alpha.txt from prereq alpha.raw (stem alpha)\n"
                    "target beta.txt from prereq beta.raw (stem beta)"
                ),
                description="the stem is substituted into the prereq pattern",
            ),
            step(
                "cat",
                "alpha.txt",
                stdout="alpha",
                files={"alpha.txt": "alpha", "beta.txt": "beta"},
                description="each target was copied from its own prerequisite",
            ),
        ],
        breaks=[("$(files): %.txt: %.raw", "$(files): %.txt: %.csv")],
        files={"alpha.raw": "alpha\n", "beta.raw": "beta\n"},
    ),
    ex(
        topic=TOPIC,
        slug="08_more_specific_match",
        title="explicit rules win over pattern rules",
        objective=(
            "Keep the explicit rule for all.c so that it is written by hand, "
            "while the %.c pattern rule touches an empty file for the rest."
        ),
        reference="Static Pattern Rules",
        hint=(
            "make prefers the more specific match: a rule that names all.c "
            "exactly beats a pattern rule that could also match it.  Touch $@ "
            "creates an empty file, so all.c needs its own rule."
        ),
        makefile="""
all: all.c foo.c
\techo "built: $^"

# all.c has a rule of its own, so it never uses the %.c rule below.
all.c:
\techo "int main() { return 0; }" > all.c

# A pattern rule with no prerequisites: any other .c file is created empty.
%.c:
\ttouch $@
""",
        steps=[
            mk(
                stdout="built: all.c foo.c",
                stdout_mode="contains",
                description="both prerequisites were dealt with",
            ),
            step(
                "cat",
                "all.c",
                stdout="int main() { return 0; }",
                stdout_mode="contains",
                description="the explicit rule beat the pattern rule for all.c",
            ),
            step(
                "test",
                "!",
                "-s",
                "foo.c",
                description="foo.c fell through to the pattern rule",
            ),
        ],
        breaks=[
            (
                "# all.c has a rule of its own, so it never uses the %.c rule below.\n"
                'all.c:\n\techo "int main() { return 0; }" > all.c',
                "# TODO: all.c needs a rule of its own here",
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="09_static_pattern_filter",
        title="Picking targets with $(filter ...)",
        objective=(
            "Use $(filter) to give .o files and .result files their own "
            "static pattern rules, so that each kind is built from the right "
            "source."
        ),
        reference="Static Pattern Rules and Filter",
        hint=(
            "$(filter %.o,$(obj_files)) keeps only the .o names, so the rule "
            "after the colon only applies to those.  .PHONY matters here: "
            "without it make tries to link the program all from its prereqs."
        ),
        makefile="""
obj_files = foo.result bar.o lose.o
src_files = foo.raw bar.c lose.c

all: $(obj_files)
# PHONY is important here: without it, implicit rules would try to build
# the executable "all", since the prerequisites are .o files.
.PHONY: all

# Ex 1: .o files come from .c files.
$(filter %.o,$(obj_files)): %.o: %.c
\techo "target: $@ prereq: $<"

# Ex 2: .result files come from .raw files.
$(filter %.result,$(obj_files)): %.result: %.raw
\techo "target: $@ prereq: $<"

# A pattern rule that creates a missing source file, empty.
%.c %.raw:
\ttouch $@

clean:
\trm -f $(src_files)
""",
        steps=[
            mk(
                stdout=(
                    "target: foo.result prereq: foo.raw\n"
                    "target: bar.o prereq: bar.c\n"
                    "target: lose.o prereq: lose.c"
                ),
                description="each target was matched by the rule for its kind",
            ),
            mk(
                "clean",
                stdout="rm -f foo.raw bar.c lose.c",
                missing=["foo.raw", "bar.c", "lose.c"],
                description="clean removes the generated sources",
            ),
        ],
        breaks=[(".PHONY: all\n", "")],
    ),
    ex(
        topic=TOPIC,
        slug="10_static_pattern_filter_out",
        title="Dropping targets with $(filter-out ...)",
        objective=(
            "Build only the objects that are not test.o, using $(filter-out) "
            "in front of a static pattern rule."
        ),
        reference="Static Pattern Rules and Filter",
        hint=(
            "$(filter-out test.o,$(objects)) is $(objects) with test.o "
            "removed, so the rule you attach it to never mentions test.o.  "
            "$^ in the link recipe then holds just the production objects."
        ),
        makefile="""
objects = main.o util.o test.o

# filter-out removes the words in front of the comma from the list.
production = $(filter-out test.o,$(objects))

all: $(production)
\techo "link: $^"

# Only the objects left in $(production) get this rule.
$(production): %.o: %.c
\techo "compile: $< -> $@"

clean:
\trm -f *.o
""",
        steps=[
            mk(
                stdout=(
                    "compile: main.c -> main.o\n"
                    "compile: util.c -> util.o\n"
                    "link: main.o util.o"
                ),
                description="the test object is never compiled or linked",
            ),
            mk(
                stdout="test.o",
                stdout_mode="not_contains",
                description="test.o is missing from the whole run",
            ),
        ],
        breaks=[("$(filter-out test.o,$(objects))", "$(filter test.o,$(objects))")],
        files={
            "main.c": "int main(void) { return 0; }\n",
            "util.c": "int util(void) { return 0; }\n",
            "test.c": "int test(void) { return 0; }\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="11_pattern_rule_compile",
        title="A pattern rule of your own",
        objective=(
            "Write a %.o: %.c pattern rule whose recipe uses $< and $@, and "
            "see it applied to every matching target."
        ),
        reference="Pattern Rules",
        hint=(
            "A pattern rule is an implicit rule you define yourself: % in the "
            "target matches any non-empty stem and the same % in the "
            "prerequisite stands for it.  $< is that prerequisite and $@ the "
            "target."
        ),
        makefile="""
# Define a pattern rule that compiles every .c file into a .o file.
%.o: %.c
\techo "compile $< -> $@"
\t$(CC) -c $< -o $@

all: foo.o bar.o
""",
        steps=[
            mk(
                stdout="compile foo.c -> foo.o\ncompile bar.c -> bar.o",
                description="the one rule was used for both objects",
            ),
            step("test", "-f", "foo.o", description="foo.o exists"),
            step("test", "-f", "bar.o", description="bar.o exists"),
            mk(
                stdout="make: Nothing to be done for 'all'.",
                stdout_mode="contains",
                description="both objects are up to date",
            ),
            step("rm", "-f", "foo.o", description="throw foo.o away again"),
            mk(
                stdout="compile foo.c -> foo.o",
                stdout_mode="contains",
                description="only the missing object is rebuilt",
            ),
            mk(
                stdout="bar.c",
                stdout_mode="not_contains",
                description="bar.o is untouched, so bar.c is not needed",
            ),
        ],
        breaks=[
            (
                "# Define a pattern rule that compiles every .c file into a .o file.\n"
                '%.o: %.c\n\techo "compile $< -> $@"\n\t$(CC) -c $< -o $@',
                "# TODO: the %.o: %.c pattern rule belongs here",
            )
        ],
        files={
            "foo.c": "int foo(void) { return 0; }\n",
            "bar.c": "int bar(void) { return 0; }\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="12_pattern_rule_no_prereq",
        title="A pattern rule with no prerequisites",
        objective=(
            "Add a %.c rule that has no prerequisite pattern, so make can "
            "always create a missing .c file -- empty."
        ),
        reference="Pattern Rules",
        hint=(
            "A pattern rule whose target has no counterpart in the "
            "prerequisites can be used for any matching file, and there is "
            "nothing to check first.  touch $@ creates the needed file and "
            "leaves it empty."
        ),
        makefile="""
# A pattern rule that has no pattern in the prerequisites.  This just
# creates empty .c files when they are needed.
%.c:
\ttouch $@

stub: stub.c
\techo "stub.c is ready"
""",
        steps=[
            mk(
                stdout="touch stub.c\nstub.c is ready",
                description="make created the missing source, then ran the rule",
            ),
            step("test", "-f", "stub.c", description="stub.c exists"),
            step("test", "!", "-s", "stub.c", description="and it is empty"),
        ],
        breaks=[
            (
                "# A pattern rule that has no pattern in the prerequisites.  This just\n"
                "# creates empty .c files when they are needed.\n%.c:\n\ttouch $@",
                "# TODO: nothing says how a missing .c file is created",
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="13_pattern_vs_static",
        title="Pattern rules cover targets you never listed",
        objective=(
            "Replace the two hand-listed targets with a pattern rule, so that "
            "extra.out is built as well even though no rule names it."
        ),
        reference="Pattern Rules",
        hint=(
            "A static pattern rule only ever applies to the targets before "
            "the colon; a pattern rule applies to any target that matches it.  "
            "%.out: %.in covers every .out file in the directory."
        ),
        makefile="""
# A pattern rule has no target list: it applies to every .out file whose
# .in file exists, including extra.out, which is named nowhere here.
%.out: %.in
\tcp $< $@

all: a.out b.out extra.out
\techo "done"
""",
        steps=[
            mk(
                stdout=(
                    "cp a.in a.out\ncp b.in b.out\ncp extra.in extra.out"
                ),
                description="all three outputs were built by the one rule",
            ),
            step("rm", "-f", "extra.out", description="remove one output"),
            mk(
                "extra.out",
                stdout="cp extra.in extra.out",
                stdout_mode="contains",
                description="an unlisted target is still buildable",
            ),
            step(
                "cat",
                "extra.out",
                stdout="extra",
                description="the copy used the matching .in file",
            ),
        ],
        breaks=[("%.out: %.in", "a.out b.out: %.out: %.in")],
        files={"a.in": "a\n", "b.in": "b\n", "extra.in": "extra\n"},
    ),
    ex(
        topic=TOPIC,
        slug="14_double_colon_order",
        title="Two double-colon rules, two recipes",
        objective=(
            "Define the same target twice with :: so that both recipes run, "
            "in the order they appear in the file."
        ),
        reference="Double-Colon Rules",
        hint=(
            "With a single colon the second definition would replace the "
            "first.  A double colon says these are separate rules for one "
            "target, and make runs each rule's recipe in turn."
        ),
        makefile="""
all: blah

blah::
\techo "hello"

blah::
\techo "hello again"
""",
        steps=[
            mk(
                stdout="hello\nhello again",
                description="both recipes ran, in file order",
            ),
            mk(
                "blah",
                stdout="hello\nhello again",
                description="naming the target does the same thing",
            ),
        ],
        breaks=[
            ('blah::\n\techo "hello"', 'blah:\n\techo "hello"'),
            ('blah::\n\techo "hello again"', 'blah:\n\techo "hello again"'),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="15_single_colon_warning",
        title="What a single colon does instead",
        objective=(
            "Repeat the target with single colons and confirm what make says: "
            "it warns and keeps only the last recipe."
        ),
        reference="Double-Colon Rules",
        hint=(
            "Written with one colon, the second rule overrides the first and "
            "make prints a warning on stderr.  Compare that with the "
            "double-colon version, where both recipes run."
        ),
        makefile="""
all: blah

blah:
\techo "first"

blah:
\techo "second"
""",
        steps=[
            mk(
                stdout="second",
                stdout_mode="contains",
                description="the last recipe is the one make keeps",
            ),
            mk(
                stdout="first",
                stdout_mode="not_contains",
                description="the overridden recipe never runs",
            ),
            mk(
                stderr="warning: overriding recipe for target 'blah'",
                stderr_mode="contains",
                description="make warns about the override",
            ),
            mk(
                stderr="warning: ignoring old recipe for target 'blah'",
                stderr_mode="contains",
                description="and says which recipe it dropped",
            ),
        ],
        breaks=[
            ('blah:\n\techo "first"', 'blah::\n\techo "first"'),
            ('blah:\n\techo "second"', 'blah::\n\techo "second"'),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="16_double_colon_prereqs",
        title="Each double-colon rule is checked on its own",
        objective=(
            "Give each :: rule its own prerequisite and its own recipe, so "
            "that make rebuilds only the rule whose prerequisite changed."
        ),
        reference="Double-Colon Rules",
        hint=(
            "Every :: rule is a rule in its own right, with its own "
            "prerequisites and its own up-to-date check.  make -W one pretends "
            "one was just modified, which shows you which rule that triggers."
        ),
        makefile="""
# Each rule has its own prerequisite, and make checks them separately.
blah:: one
\techo "rule 1"
\ttouch blah

blah:: two
\techo "rule 2"
\ttouch blah
""",
        steps=[
            mk(
                stdout="rule 1\nrule 2",
                description="with no blah yet, both rules are out of date",
            ),
            mk(
                stdout="make: 'blah' is up to date.",
                stdout_mode="contains",
                description="once blah is newer than both, nothing runs",
            ),
            mk(
                "-W",
                "one",
                stdout="rule 1",
                stdout_mode="contains",
                description="pretending one changed triggers the first rule",
            ),
            mk(
                "-W",
                "one",
                stdout="rule 2",
                stdout_mode="not_contains",
                description="and leaves the second rule alone",
            ),
            mk(
                "-W",
                "two",
                stdout="rule 2",
                stdout_mode="contains",
                description="pretending two changed triggers the second rule",
            ),
            mk(
                "-W",
                "two",
                stdout="rule 1",
                stdout_mode="not_contains",
                description="and leaves the first rule alone",
            ),
        ],
        breaks=[("blah:: two", "blah:: one")],
        files={"one": "one\n", "two": "two\n"},
    ),
]
