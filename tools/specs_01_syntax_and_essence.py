"""Exercises for the tutorial's "Makefile Syntax" and "The essence of Make".

Recipe lines inside the ``makefile`` strings are indented with a ``\\t`` escape.
Python turns that into a real tab, which is what make requires; writing a
literal tab into the source would be invisible and easy to lose.
"""

from spec import ex, mk, step

TOPIC = "01_syntax_and_essence"

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_rule_anatomy",
        title="The anatomy of a rule",
        objective=(
            "Write a rule whose target is report.txt, whose prerequisite is "
            "notes.txt, and whose recipe builds the report in two commands."
        ),
        reference="Makefile Syntax",
        hint=(
            "A rule is the line 'targets: prerequisites' followed by the "
            "recipe. Every recipe line must begin with a real TAB character; "
            "four spaces are rejected with 'missing separator'."
        ),
        makefile="""
report.txt: notes.txt
\techo "Report" > report.txt
\tcat notes.txt >> report.txt
""",
        steps=[
            mk(
                stdout=(
                    'echo "Report" > report.txt\n'
                    'cat notes.txt >> report.txt'
                ),
                description="both commands of the recipe run, in order",
            ),
            step(
                "cat",
                "report.txt",
                stdout="Report\nalpha\nbeta",
                description="the first command wrote the header, the second "
                "appended the notes",
            ),
            mk(
                stdout="make: 'report.txt' is up to date.",
                stdout_mode="contains",
                description="the prerequisite is not newer, so nothing is rebuilt",
            ),
            step(
                "touch",
                "-t",
                "199001010000",
                "report.txt",
                description="put the target in the past, so the prerequisite "
                "is the newer file",
            ),
            mk(
                stdout='echo "Report" > report.txt',
                stdout_mode="contains",
                description="a newer prerequisite brings the rule back to life",
            ),
        ],
        breaks=[
            (
                '\techo "Report" > report.txt\n\tcat notes.txt >> report.txt',
                '    echo "Report" > report.txt\n'
                '    cat notes.txt >> report.txt',
            )
        ],
        files={"notes.txt": "alpha\nbeta\n"},
    ),
    ex(
        topic=TOPIC,
        slug="02_several_targets_one_rule",
        title="Several targets on one rule line",
        objective=(
            "Write a single rule that applies to two target names, so that "
            "make can build either one of them."
        ),
        reference="Makefile Syntax",
        hint=(
            "The targets are file names separated by spaces. Two names on the "
            "same rule line mean one recipe serves both targets."
        ),
        makefile="""
one two:
\ttouch one two
""",
        steps=[
            mk(
                "two",
                stdout="touch one two",
                description="the second name on the rule line is a target too",
            ),
            step(
                "test",
                "-f",
                "two",
                description="the recipe created the file two",
            ),
            step(
                "test",
                "-f",
                "one",
                description="the same recipe created the file one as well",
            ),
            mk(
                "one",
                stdout="make: 'one' is up to date.",
                stdout_mode="contains",
                description="the first name refers to the very same rule",
            ),
        ],
        breaks=[("one two:", "one:")],
    ),
    ex(
        topic=TOPIC,
        slug="03_prerequisite_order",
        title="Prerequisites are built left to right",
        objective=(
            "Order the prerequisites of the all target so that make builds "
            "one, then two, then three."
        ),
        reference="Makefile Syntax",
        hint=(
            "Every prerequisite has to be finished before the commands of the "
            "target run, and make works through the list from left to right."
        ),
        makefile="""
all: one two three
\tcat order.txt

one:
\techo "one" >> order.txt

two:
\techo "two" >> order.txt

three:
\techo "three" >> order.txt
""",
        steps=[
            mk(
                stdout=(
                    'echo "one" >> order.txt\n'
                    'echo "two" >> order.txt\n'
                    'echo "three" >> order.txt\n'
                    "cat order.txt\n"
                    "one\n"
                    "two\n"
                    "three"
                ),
                description="the prerequisites run in the order they are listed",
            ),
            step(
                "cat",
                "order.txt",
                stdout="one\ntwo\nthree",
                description="the file records that same order",
            ),
            step(
                "test",
                "-f",
                "order.txt",
                files={"order.txt": "one\ntwo\nthree\n"},
                description="the target's own command ran last",
            ),
        ],
        breaks=[("all: one two three", "all: three two one")],
    ),
    ex(
        topic=TOPIC,
        slug="04_recipe_creates_the_target",
        title="The recipe creates the file the target names",
        objective=(
            "Make the hello target write its two lines into a file called "
            "hello, so that a second make finds nothing to do."
        ),
        reference="The essence of Make",
        hint=(
            "A target and a file with the same name are tied together. "
            "Redirect the first command into hello and append the second one "
            "to the same file."
        ),
        makefile="""
hello:
\techo "Hello, World" > hello
\techo "This line will print if the file hello does not exist." >> hello
""",
        steps=[
            mk(
                stdout=(
                    'echo "Hello, World" > hello\n'
                    'echo "This line will print if the file hello does not '
                    'exist." >> hello'
                ),
                description="both commands of the recipe run on the first make",
            ),
            step(
                "cat",
                "hello",
                stdout=(
                    "Hello, World\n"
                    "This line will print if the file hello does not exist."
                ),
                description="the file holds both lines",
            ),
            mk(
                stdout="make: 'hello' is up to date.",
                stdout_mode="contains",
                description="the target now exists as a file, so make stops",
            ),
        ],
        breaks=[
            (
                'echo "Hello, World" > hello\n'
                '\techo "This line will print if the file hello does not '
                'exist." >> hello',
                'echo "Hello, World"\n'
                '\techo "This line will print if the file hello does not '
                'exist."',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="05_timestamps_decide",
        title="Timestamps decide whether to rebuild",
        objective=(
            "Give blah a prerequisite so that touching blah.c rebuilds it, "
            "while an older blah.c is ignored."
        ),
        reference="The essence of Make",
        hint=(
            "Without a prerequisite make only asks whether blah exists. Add "
            "blah.c after the colon and make starts comparing timestamps."
        ),
        makefile="""
blah: blah.c
\tcp blah.c blah
""",
        steps=[
            mk(
                stdout="cp blah.c blah",
                description="the first run builds blah from blah.c",
            ),
            step(
                "test",
                "-f",
                "blah",
                description="the recipe created the file blah",
            ),
            step(
                "touch",
                "-t",
                "200001010000",
                "blah.c",
                description="give the source a fixed timestamp",
            ),
            step(
                "touch",
                "-t",
                "201001010000",
                "blah",
                description="and the target a newer one",
            ),
            mk(
                stdout="make: 'blah' is up to date.",
                stdout_mode="contains",
                description="an older prerequisite does not force a rebuild",
            ),
            step(
                "touch",
                "-t",
                "199001010000",
                "blah",
                description="now put the target in the past",
            ),
            mk(
                stdout="cp blah.c blah",
                description="a newer prerequisite forces a rebuild",
            ),
        ],
        breaks=[("blah: blah.c", "blah:")],
        files={"blah.c": "int main(void) { return 0; }\n"},
    ),
    ex(
        topic=TOPIC,
        slug="06_every_prerequisite_counts",
        title="Every prerequisite is checked",
        objective=(
            "Declare both parts as prerequisites of combined.txt so that "
            "touching either one rebuilds it."
        ),
        reference="The essence of Make",
        hint=(
            "All the names after the colon are prerequisites. The target is "
            "rebuilt when any one of them is newer than the target itself."
        ),
        makefile="""
combined.txt: a.txt b.txt
\tcat a.txt b.txt > combined.txt
""",
        steps=[
            mk(
                stdout="cat a.txt b.txt > combined.txt",
                description="the first run concatenates both parts",
            ),
            step(
                "touch",
                "-t",
                "199001010000",
                "a.txt",
                "b.txt",
                description="put both parts in the past",
            ),
            step(
                "touch",
                "-t",
                "200001010000",
                "combined.txt",
                description="and the target in between",
            ),
            mk(
                stdout="make: 'combined.txt' is up to date.",
                stdout_mode="contains",
                description="with both parts older there is nothing to do",
            ),
            step(
                "touch",
                "-t",
                "201001010000",
                "b.txt",
                description="now make only the second part newer than "
                "the target",
            ),
            mk(
                stdout="cat a.txt b.txt > combined.txt",
                description="the second prerequisite alone triggers a rebuild",
            ),
            step(
                "touch",
                "-t",
                "200001010000",
                "combined.txt",
                description="put the target back in the past",
            ),
            step(
                "touch",
                "-t",
                "200501010000",
                "a.txt",
                description="now make the first part the newer one",
            ),
            mk(
                stdout="cat a.txt b.txt > combined.txt",
                description="so does the first prerequisite on its own",
            ),
        ],
        breaks=[("combined.txt: a.txt b.txt", "combined.txt: a.txt")],
        files={"a.txt": "head\n", "b.txt": "tail\n"},
    ),
    ex(
        topic=TOPIC,
        slug="07_existing_file_is_skipped",
        title="A target that is already a file",
        objective=(
            "Name the target after the file that is already there, so that "
            "make skips the recipe instead of running it."
        ),
        reference="The essence of Make",
        hint=(
            "make looks for a file whose name is exactly the target's name. "
            "When that file exists the target counts as up to date and no "
            "command runs."
        ),
        makefile="""
existing.txt:
\techo "do not touch" > existing.txt
""",
        steps=[
            mk(
                stdout="make: 'existing.txt' is up to date.",
                stdout_mode="contains",
                description="the file with the target's name already exists",
            ),
            mk(
                stdout='echo "do not touch"',
                stdout_mode="not_contains",
                description="so make never runs the recipe",
            ),
            step(
                "cat",
                "existing.txt",
                stdout="do not touch",
                description="and the file keeps the contents it had",
            ),
        ],
        breaks=[("existing.txt:", "report.txt:")],
        files={"existing.txt": "do not touch\n"},
    ),
    ex(
        topic=TOPIC,
        slug="08_no_prerequisites_always_runs",
        title="A target with no file always runs",
        objective=(
            "Write a target that has no prerequisites and creates no file, "
            "and confirm that make runs it every time."
        ),
        reference="The essence of Make",
        hint=(
            "make skips a recipe only when a file with the target's name "
            "exists. A target such as stamp, whose recipe never creates "
            "stamp, is run again on every invocation."
        ),
        makefile="""
stamp:
\techo "the stamp target ran"

report.txt:
\techo "report built" > report.txt
""",
        steps=[
            mk(
                "stamp",
                stdout="the stamp target ran",
                stdout_mode="contains",
                description="the first run executes the recipe",
            ),
            mk(
                "stamp",
                stdout="the stamp target ran",
                stdout_mode="contains",
                description="there is no file called stamp, so it runs again",
            ),
            mk(
                "report.txt",
                stdout='echo "report built" > report.txt',
                description="a target that does create its file behaves "
                "differently",
            ),
            mk(
                "report.txt",
                stdout="make: 'report.txt' is up to date.",
                stdout_mode="contains",
                description="make has a file to compare against here",
            ),
        ],
        breaks=[
            (
                'echo "the stamp target ran"',
                'echo "the stamp target ran" > stamp',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="09_directory_target",
        title="When the target is a directory",
        objective=(
            "Let make treat the existing directory out as the target's file, "
            "skipping the recipe until out/.keep becomes newer."
        ),
        reference="The essence of Make",
        hint=(
            "A directory is a file as far as make is concerned. If out exists "
            "the recipe is skipped; list out/.keep as a prerequisite so make "
            "has a timestamp to compare against."
        ),
        makefile="""
out: out/.keep
\techo "the directory target was out of date"
""",
        steps=[
            step(
                "touch",
                "-t",
                "201001010000",
                "out/.keep",
                description="put the file inside the directory in the past",
            ),
            step(
                "touch",
                "-t",
                "202001010000",
                "out",
                description="and the directory itself a newer one",
            ),
            mk(
                "out",
                stdout="make: 'out' is up to date.",
                stdout_mode="contains",
                description="the directory counts as an existing file",
            ),
            step(
                "touch",
                "-t",
                "202101010000",
                "out/.keep",
                description="now the prerequisite is newer than the directory",
            ),
            mk(
                "out",
                stdout="the directory target was out of date",
                stdout_mode="contains",
                description="the out of date directory is rebuilt",
            ),
        ],
        breaks=[("out: out/.keep", "out:")],
        files={"out/.keep": "keep\n"},
    ),
    ex(
        topic=TOPIC,
        slug="10_no_rule_to_make_target",
        title="No rule to make target",
        objective=(
            "Give broken a prerequisite that nothing creates, and watch make "
            "refuse to build it."
        ),
        reference="The essence of Make",
        hint=(
            "A prerequisite must either exist as a file or be the target of "
            "another rule. Declare missing.txt as the prerequisite of broken "
            "to see what make says about it."
        ),
        makefile="""
summary: notes.txt
\tcat notes.txt

notes.txt:
\techo "written by the notes target" > notes.txt

broken: missing.txt
\tcat missing.txt
""",
        steps=[
            mk(
                stdout=(
                    'echo "written by the notes target" > notes.txt\n'
                    "cat notes.txt\n"
                    "written by the notes target"
                ),
                description="the default target builds its prerequisite first",
            ),
            mk(
                "broken",
                exit_code=2,
                stdout="cat missing.txt",
                stdout_mode="not_contains",
                stderr="No rule to make target 'missing.txt', needed by 'broken'.",
                description="make stops before running the recipe",
            ),
            mk(
                "nosuch",
                exit_code=2,
                stderr="No rule to make target 'nosuch'.",
                description="a goal that no rule defines is refused the same way",
            ),
        ],
        breaks=[("broken: missing.txt", "broken:")],
    ),
    ex(
        topic=TOPIC,
        slug="11_nothing_to_do_vs_up_to_date",
        title="Nothing to be done versus up to date",
        objective=(
            "Use a target with no recipe so make reports nothing to be done, "
            "and a target whose file exists so make reports it is up to date."
        ),
        reference="The essence of Make",
        hint=(
            "Nothing to be done is what make says about a target that has no "
            "recipe at all. Up to date is what it says about a target whose "
            "recipe was skipped because the file is already there."
        ),
        makefile="""
all:

report.txt:
\techo "building the report" > report.txt
""",
        steps=[
            mk(
                stdout="make: Nothing to be done for 'all'.",
                stdout_mode="contains",
                description="all has no recipe and no prerequisites",
            ),
            mk(
                "all",
                stdout="make: Nothing to be done for 'all'.",
                stdout_mode="contains",
                description="naming the target makes no difference here",
            ),
            mk(
                "report.txt",
                stdout='echo "building the report" > report.txt',
                description="this target does have a recipe to run",
            ),
            mk(
                "report.txt",
                stdout="make: 'report.txt' is up to date.",
                stdout_mode="contains",
                description="now the file exists, so the message changes",
            ),
        ],
        breaks=[("all:", "all:\n\techo \"all ran\"")],
    ),
]
