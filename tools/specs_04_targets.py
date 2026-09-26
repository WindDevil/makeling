"""Exercises for the tutorial's "Targets" chapter.

Covers the ``Targets`` chapter heading, ``The all target`` and ``Multiple
targets``.  Recipe lines inside the ``makefile`` strings are indented with a
``\\t`` escape, exactly as in the other spec files: Python turns it into a real
tab, which is what make requires.
"""

from spec import ex, mk, step

TOPIC = "04_targets"

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_target_is_a_name",
        title="A target is just a name",
        objective=(
            "Give the first rule the target name notes and the second the name "
            "real_file, so that make notes prints the note while real_file "
            "creates a file."
        ),
        reference="Targets",
        hint=(
            "A rule's name is the target it defines: make asks for that exact "
            "name. A target with no file behind it is rebuilt every time."
        ),
        makefile="""
notes:
\techo "a target is only a name"

real_file:
\ttouch real_file
""",
        steps=[
            mk(
                stdout='echo "a target is only a name"\na target is only a name',
                description="the default goal runs the first rule",
            ),
            mk(
                stdout="up to date",
                stdout_mode="not_contains",
                description="no file called notes exists, so the recipe is never skipped",
            ),
            mk(
                "notes",
                stdout="a target is only a name",
                description="naming the target explicitly runs the same rule",
            ),
            mk(
                "real_file",
                stdout="touch real_file",
                description="the second rule really does create its target",
            ),
            mk(
                "real_file",
                stdout="make: 'real_file' is up to date.",
                stdout_mode="contains",
                description="that file now exists, so the recipe is skipped",
            ),
            step("test", "-f", "real_file", description="the file is on disk"),
        ],
        breaks=[("notes:", "note:")],
    ),
    ex(
        topic=TOPIC,
        slug="02_target_need_not_exist",
        title="A target need not exist on disk",
        objective=(
            "Make report depend on data.txt so that the data file is generated "
            "first, even though report itself is never created."
        ),
        reference="Targets",
        hint=(
            "A prerequisite is built before the target's own recipe runs. A "
            "target whose name never appears on disk is out of date every time."
        ),
        makefile="""
report: data.txt
\tcat data.txt

data.txt:
\techo "42" > data.txt
""",
        steps=[
            mk(
                "report",
                stdout='echo "42" > data.txt\ncat data.txt\n42',
                description="the prerequisite is built, then report prints it",
            ),
            mk(
                "report",
                stdout="> data.txt",
                stdout_mode="not_contains",
                description="data.txt is up to date and is not regenerated",
            ),
            mk(
                "report",
                stdout="42",
                description="report is still out of date, so it prints again",
            ),
            step(
                "cat",
                "data.txt",
                stdout="42",
                description="the prerequisite really is on disk",
            ),
        ],
        breaks=[("report: data.txt", "report:")],
    ),
    ex(
        topic=TOPIC,
        slug="03_phony_clean",
        title="A file that shadows clean",
        objective=(
            "Declare clean phony so that the stray file called clean does not "
            "make make skip the recipe."
        ),
        reference="Make clean",
        hint=(
            "make compares the target name with the filesystem. .PHONY: clean "
            "tells make that clean is a name to run, never a file to check."
        ),
        makefile="""
.PHONY: clean

some_file:
\techo "content" > some_file

clean:
\trm -f some_file
""",
        steps=[
            mk(
                "some_file",
                stdout='echo "content" > some_file',
                description="build the file that clean is supposed to remove",
            ),
            mk(
                "-n",
                "clean",
                stdout="rm -f some_file",
                files={"some_file": "content\n"},
                description="the dry run shows the recipe and removes nothing",
            ),
            mk(
                "clean",
                stdout="rm -f some_file",
                missing=["some_file"],
                description="clean really runs, even though a file named clean exists",
            ),
        ],
        breaks=[(".PHONY: clean\n\nsome_file:", "some_file:")],
        files={"clean": "# a stray file that happens to be called clean\n"},
    ),
    ex(
        topic=TOPIC,
        slug="04_all_builds_everything",
        title="The all target builds everything",
        objective=(
            "List one, two and three in the all rule so that a bare make builds "
            "all three files."
        ),
        reference="The all target",
        hint=(
            "all is a normal target whose prerequisites are the other targets. "
            "Because it comes first it is what a bare make runs."
        ),
        makefile="""
all: one two three

one:
\ttouch one
two:
\ttouch two
three:
\ttouch three

clean:
\trm -f one two three
""",
        steps=[
            mk(
                stdout="touch one\ntouch two\ntouch three",
                files={"one": "", "two": "", "three": ""},
                description="a bare make builds every prerequisite of all",
            ),
            mk(
                stdout="make: Nothing to be done for 'all'.",
                stdout_mode="contains",
                description="a second run has nothing left to do",
            ),
            mk(
                "one",
                stdout="make: 'one' is up to date.",
                stdout_mode="contains",
                description="a single target can still be asked for by name",
            ),
            mk(
                "clean",
                stdout="rm -f one two three",
                missing=["one", "two", "three"],
                description="clean is not part of all, so it only runs when named",
            ),
        ],
        breaks=[("all: one two three", "all: one two")],
    ),
    ex(
        topic=TOPIC,
        slug="05_all_from_a_variable",
        title="Build the all rule from a variable",
        objective=(
            "Keep the list of targets in a variable and let all expand it "
            "instead of writing the names out."
        ),
        reference="The all target",
        hint=(
            "A variable is expanded with $(NAME). Writing the bare word NAME "
            "makes make look for a file of that name instead."
        ),
        makefile="""
TARGETS := one two three

all: $(TARGETS)

one:
\t@echo "building one"

two:
\t@echo "building two"

three:
\t@echo "building three"

list:
\t@echo "all depends on: $(TARGETS)"
""",
        steps=[
            mk(
                stdout="building one\nbuilding two\nbuilding three",
                description="all expands the variable and builds each name",
            ),
            mk(
                "list",
                stdout="all depends on: one two three",
                description="the variable really holds the three names",
            ),
            mk(
                "two",
                stdout="building two",
                description="one name from the list can be built on its own",
            ),
            mk(
                "two",
                stdout="building one",
                stdout_mode="not_contains",
                description="naming one goal does not build the others",
            ),
        ],
        breaks=[("all: $(TARGETS)", "all: TARGETS")],
    ),
    ex(
        topic=TOPIC,
        slug="06_multiple_targets_one_rule",
        title="Several targets on one rule line",
        objective=(
            "Put f1.o and f2.o on a single rule line and confirm that the recipe "
            "runs once for each target."
        ),
        reference="Multiple targets",
        hint=(
            "f1.o f2.o: is shorthand for two rules with the same recipe. $@ "
            "expands to whichever target is being built."
        ),
        makefile="""
all: f1.o f2.o

f1.o f2.o:
\techo $@
""",
        steps=[
            mk(
                stdout="echo f1.o\nf1.o\necho f2.o\nf2.o",
                description="the recipe is run twice, once per target",
            ),
            mk(
                "-n",
                stdout='echo f1.o\necho f2.o',
                stdout_mode="exact",
                description="the dry run shows the recipe printed once per target",
            ),
            mk(
                "-f",
                "expanded.mk",
                stdout="echo f1.o\nf1.o\necho f2.o\nf2.o",
                description="writing the two rules out is exactly equivalent",
            ),
        ],
        breaks=[("f1.o f2.o:", "f1.o:")],
        files={
            "expanded.mk": """
all: f1.o f2.o

f1.o:
\techo $@

f2.o:
\techo $@
""",
        },
    ),
    ex(
        topic=TOPIC,
        slug="07_shared_recipe_per_target",
        title="One recipe writes each target",
        objective=(
            "Let a single recipe build both red.txt and blue.txt by writing to "
            "$@, so each target gets its own file."
        ),
        reference="Multiple targets",
        hint=(
            "$@ is the target being built right now. A hard-coded file name "
            "would be written twice and neither target would exist."
        ),
        makefile="""
all: red.txt blue.txt

red.txt blue.txt:
\techo "$@ created" > $@
""",
        steps=[
            mk(
                stdout='echo "red.txt created" > red.txt\necho "blue.txt created" > blue.txt',
                files={"red.txt": "red.txt created\n", "blue.txt": "blue.txt created\n"},
                description="both targets are created, each with its own name",
            ),
            mk(
                stdout="make: Nothing to be done for 'all'.",
                stdout_mode="contains",
                description="both files are up to date on the next run",
            ),
        ],
        breaks=[("> $@", "> out.txt")],
    ),
    ex(
        topic=TOPIC,
        slug="08_one_recipe_many_files",
        title="One recipe that produces several files",
        objective=(
            "Make a single recipe create both first.part and second.part for the "
            "bundle target."
        ),
        reference="Multiple targets",
        hint=(
            "The rule still runs its recipe once per target, but make skips a "
            "target whose file already exists and which has no prerequisites."
        ),
        makefile="""
bundle: first.part second.part

first.part second.part:
\techo "shared payload" > first.part
\tcp first.part second.part
""",
        steps=[
            mk(
                stdout='echo "shared payload" > first.part\ncp first.part second.part',
                files={"first.part": "shared payload\n", "second.part": "shared payload\n"},
                description="the recipe produces both files in one go",
            ),
            mk(
                stdout="make: Nothing to be done for 'bundle'.",
                stdout_mode="contains",
                description="second.part already exists, so the recipe is not repeated",
            ),
            step(
                "cat",
                "second.part",
                stdout="shared payload",
                description="the copied file holds the same payload",
            ),
        ],
        breaks=[("cp first.part second.part", "cp first.part other.part")],
    ),
    ex(
        topic=TOPIC,
        slug="09_all_and_clean",
        title="all first, clean last",
        objective=(
            "Keep all as the first rule and clean at the bottom, so that a bare "
            "make builds and make all clean builds then removes."
        ),
        reference="The all target",
        hint=(
            "The first rule in the file is the default goal. clean is not a "
            "prerequisite of anything, so it only runs when it is named."
        ),
        makefile="""
all: one two

one:
\techo "one" > one

two:
\techo "two" > two

clean:
\trm -f one two
""",
        steps=[
            mk(
                stdout='echo "one" > one\necho "two" > two',
                files={"one": "one\n", "two": "two\n"},
                description="a bare make builds and does not clean",
            ),
            mk(
                "all",
                "clean",
                stdout="make: Nothing to be done for 'all'.\nrm -f one two",
                missing=["one", "two"],
                description="goals run left to right: all, then clean",
            ),
            mk(
                "clean",
                "all",
                stdout='rm -f one two\necho "one" > one\necho "two" > two',
                files={"one": "one\n", "two": "two\n"},
                description="swapping the goals swaps the order of the work",
            ),
        ],
        breaks=[
            ("all: one two\n\none:", "one:"),
            ("\nclean:\n\trm -f one two", "\nall: one two\n\nclean:\n\trm -f one two"),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="10_duplicate_prerequisites",
        title="The same prerequisite twice",
        objective=(
            "Make the inspect recipe print the deduplicated list with $^ and "
            "every mention of the repeated prerequisite with $+."
        ),
        reference="Automatic Variables",
        hint=(
            "Both variables list the prerequisites; $^ drops duplicates and $+ "
            "keeps them. app.conf is named twice on purpose here."
        ),
        makefile="""
all: app.conf app.conf

app.conf:
\techo "setting=1" > app.conf

inspect: app.conf app.conf
\t@echo "unique prerequisites: $^"
\t@echo "every prerequisite: $+"
""",
        steps=[
            mk(
                "inspect",
                stdout="unique prerequisites: app.conf\nevery prerequisite: app.conf app.conf",
                files={"app.conf": "setting=1\n"},
                description="$^ collapses the duplicate, $+ keeps both mentions",
            ),
            mk(
                "inspect",
                stdout="unique prerequisites: app.conf\nevery prerequisite: app.conf app.conf",
                description="the prerequisite was built once and stays up to date",
            ),
            mk(
                "all",
                stdout="make: Nothing to be done for 'all'.",
                stdout_mode="contains",
                description="listing app.conf twice in all still builds it once",
            ),
        ],
        breaks=[
            ('\t@echo "unique prerequisites: $^"', '\t@echo "unique prerequisites: $+"'),
            ('\t@echo "every prerequisite: $+"', '\t@echo "every prerequisite: $^"'),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="11_phony_all",
        title="Stray files that shadow the aggregate",
        objective=(
            "Declare all, one and two phony so that files of those names do not "
            "stop make from running the recipes."
        ),
        reference=".phony",
        hint=(
            "Without .PHONY the file one is newer than nothing and make treats "
            "it as up to date. Declare every name in the aggregate that is not "
            "a real output."
        ),
        makefile="""
.PHONY: all one two

all: one two

one:
\techo "building one"
two:
\techo "building two"
""",
        steps=[
            mk(
                stdout="building one\nbuilding two",
                description="a bare make runs both recipes",
            ),
            mk(
                stdout="building one\nbuilding two",
                description="phony targets are rebuilt every time",
            ),
            mk(
                "one",
                stdout="building one",
                description="one can still be built on its own",
            ),
            mk(
                "one",
                stdout="building two",
                stdout_mode="not_contains",
                description="asking for one does not build two",
            ),
        ],
        breaks=[(".PHONY: all one two\n\nall: one two", "all: one two")],
        files={
            "one": "a stray file that happens to be called one\n",
            "two": "another stray file called two\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="12_shared_prerequisite_order",
        title="all builds a shared prerequisite once",
        objective=(
            "Give one and two the same prerequisite base so that make builds "
            "base first and only once."
        ),
        reference="The all target",
        hint=(
            "make walks all's prerequisites left to right and depth first, and "
            "it never builds the same target twice in one run."
        ),
        makefile="""
all: one two

one: base
\techo "one after base"

two: base
\techo "two after base"

base:
\techo "base first"
""",
        steps=[
            mk(
                "-n",
                stdout='echo "base first"\necho "one after base"\necho "two after base"',
                description="the dry run shows the planned order",
            ),
            mk(
                stdout=(
                    'echo "base first"\n'
                    "base first\n"
                    'echo "one after base"\n'
                    "one after base\n"
                    'echo "two after base"\n'
                    "two after base"
                ),
                stdout_mode="exact",
                description="base is built once, before either dependent",
            ),
            mk(
                "base",
                stdout='echo "base first"\nbase first',
                description="the shared prerequisite can be built on its own",
            ),
        ],
        breaks=[("one: base", "one:")],
    ),
]
