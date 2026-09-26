"""Exercises for the tutorial's "Getting Started" chapter.

Recipe lines inside the ``makefile`` strings are indented with a ``\\t`` escape.
Python turns that into a real tab, which is what make requires; writing a
literal tab into the source would be invisible and easy to lose.
"""

from spec import ex, mk, step

TOPIC = "00_getting_started"

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_first_rule",
        title="The simplest Makefile",
        objective="Write a rule that prints Hello, World when make runs.",
        reference="Running the Examples",
        hint=(
            "A rule is a target line followed by its recipe. Every recipe line "
            "must begin with a real TAB character; four spaces will be rejected "
            'with "missing separator".'
        ),
        makefile="""
hello:
\techo "Hello, World"
""",
        steps=[
            mk(
                stdout='echo "Hello, World"\nHello, World',
                description="make runs the only target",
            ),
            mk(
                "hello",
                stdout='echo "Hello, World"\nHello, World',
                description="naming the target explicitly does the same thing",
            ),
        ],
        breaks=[('\techo "Hello, World"', '    echo "Hello, World"')],
    ),
    ex(
        topic=TOPIC,
        slug="02_default_goal",
        title="The first target is the default goal",
        objective=(
            "Order the rules so that a bare make runs the greeting, while "
            "make goodbye still runs the farewell."
        ),
        reference="Running the Examples",
        hint=(
            "With no goal on the command line, make runs the first target it "
            "sees in the file."
        ),
        makefile="""
hello:
\techo "Hello, World"

goodbye:
\techo "Goodbye, World"
""",
        steps=[
            mk(stdout="Hello, World", description="bare make runs hello"),
            mk(
                "goodbye",
                stdout="Goodbye, World",
                description="make goodbye runs the second rule",
            ),
            mk(
                stdout="not_contains:Goodbye",
                stdout_mode="not_contains",
                description="the default goal does not run the farewell too",
            ),
        ],
        breaks=[
            (
                'hello:\n\techo "Hello, World"\n\ngoodbye:\n\techo "Goodbye, World"',
                'goodbye:\n\techo "Goodbye, World"\n\nhello:\n\techo "Hello, World"',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="03_essence_target_file",
        title="A target and a file with the same name",
        objective=(
            "Make the hello target create a file called hello, so that a second "
            "make reports it is already up to date."
        ),
        reference="The essence of Make",
        hint=(
            "make compares the target's name with the filesystem. If a file "
            "called hello exists, the recipe is skipped; redirect the echo into "
            "that file."
        ),
        makefile="""
hello:
\techo "Hello, World" > hello
""",
        steps=[
            mk(
                stdout='echo "Hello, World" > hello',
                description="the first run executes the recipe",
            ),
            step(
                "cat",
                "hello",
                description="the recipe created the file",
            ),
            mk(
                stdout="make: 'hello' is up to date.",
                stdout_mode="contains",
                description="the second run has nothing to do",
            ),
        ],
        breaks=[('\techo "Hello, World" > hello', '\techo "Hello, World"')],
    ),
    ex(
        topic=TOPIC,
        slug="04_essence_prerequisites",
        title="Prerequisites decide whether to rebuild",
        objective=(
            "Declare blah.c as a prerequisite of blah so that touching the "
            "source recompiles the program."
        ),
        reference="The essence of Make",
        hint=(
            "Without a prerequisite make only checks whether the target exists. "
            "A prerequisite makes it compare timestamps instead."
        ),
        makefile="""
blah: blah.c
\tcc blah.c -o blah
""",
        steps=[
            mk(stdout="cc blah.c -o blah", description="the first build compiles"),
            step("test", "-x", "blah", description="an executable named blah exists"),
            mk(
                stdout="make: 'blah' is up to date.",
                stdout_mode="contains",
                description="nothing changed, so nothing is rebuilt",
            ),
            # The two timestamps are set explicitly rather than left to the
            # wall clock: the target was written moments ago, and on a
            # filesystem whose timestamps are quantised to a whole second a
            # plain `touch` can land in the same tick and leave make convinced
            # there is nothing to do.
            step(
                "touch",
                "-t",
                "202001010000",
                "blah",
                description="age the compiled program",
            ),
            step(
                "touch",
                "-t",
                "202101010000",
                "blah.c",
                description="make the source newer than the program",
            ),
            mk(
                stdout="cc blah.c -o blah",
                description="the newer source triggers a rebuild",
            ),
        ],
        breaks=[("blah: blah.c", "blah:")],
        files={"blah.c": "int main(void) { return 0; }\n"},
    ),
    ex(
        topic=TOPIC,
        slug="05_which_makefile",
        title="Which file does make read?",
        objective=(
            "Give GNUmakefile and Makefile different default goals and confirm "
            "which one a bare make picks up."
        ),
        reference="Running the Examples",
        hint=(
            "make looks for GNUmakefile first, then makefile, then Makefile. "
            "Use make -f <name> to read a specific one."
        ),
        makefile="""
# Read with: make -f Makefile
explicit:
\techo "from Makefile"
""",
        steps=[
            mk(
                stdout="from GNUmakefile",
                stdout_mode="contains",
                description="a bare make prefers GNUmakefile",
            ),
            mk(
                "-f",
                "Makefile",
                stdout="from Makefile",
                stdout_mode="contains",
                description="make -f reads the named file",
            ),
            mk(
                "-f",
                "GNUmakefile",
                stdout="from GNUmakefile",
                stdout_mode="contains",
                description="the GNUmakefile can still be named explicitly",
            ),
        ],
        breaks=[],
        files={
            "GNUmakefile": """
# This file wins when you just run "make"
default:
\techo "from GNUmakefile"
""",
        },
        file_breaks=[
            (
                "GNUmakefile",
                'echo "from GNUmakefile"',
                'echo "from Makefile"',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="06_beyond_compilation",
        title="Make is not only for compilers",
        objective=(
            "Chain two non-compilation targets so that make builds a report "
            "file before printing it."
        ),
        reference="Why do Makefiles exist?",
        hint=(
            "Any target can carry any shell command. Let the report target "
            "depend on the file it prints, so the file is produced first."
        ),
        makefile="""
report: summary.txt
\tcat summary.txt

summary.txt: names.txt
\tgrep -c . names.txt > summary.txt
""",
        steps=[
            mk(
                "report",
                stdout="3",
                stdout_mode="contains",
                description="the count is printed after the report is built",
            ),
            step(
                "cat",
                "summary.txt",
                stdout="3",
                description="the intermediate file holds the line count",
            ),
            mk(
                "report",
                stdout="3",
                stdout_mode="contains",
                description="re-running still prints the report",
            ),
            mk(
                "report",
                stdout="grep -c",
                stdout_mode="not_contains",
                description="summary.txt is up to date, so it is not regenerated",
            ),
        ],
        breaks=[("report: summary.txt", "report:")],
        files={"names.txt": "ada\ngrace\nedsger\n"},
    ),
]
