"""Exercises for the tutorial's "More quick examples" and "Make clean" chapters.

Recipe lines inside the ``makefile`` strings are indented with a ``\\t`` escape.
Python turns that into a real tab, which is what make requires; writing a
literal tab into the source would be invisible and easy to lose.
"""

from spec import ex, mk, step

TOPIC = "02_quick_examples"

# The three-rule build from "More quick examples": blah is linked from blah.o,
# blah.o is compiled from blah.c, and a third rule writes blah.c itself.  Only
# the target that is asked for is built last; make starts at the deepest
# prerequisite and works back up.
CHAIN = """
blah: blah.o
\tcc blah.o -o blah # Runs third

blah.o: blah.c
\tcc -c blah.c -o blah.o # Runs second

# Typically blah.c would already exist, but I want to limit any additional required files
blah.c:
\techo "int main() { return 0; }" > blah.c # Runs first
"""

# The same three recipes, in the order make runs them on a first build.  make
# echoes each recipe line as it is written, comments and all.
CHAIN_OUTPUT = (
    'echo "int main() { return 0; }" > blah.c # Runs first\n'
    "cc -c blah.c -o blah.o # Runs second\n"
    "cc blah.o -o blah # Runs third"
)

# The same chain, plus a clean target that undoes every file it produces.
CHAIN_WITH_CLEAN = CHAIN + """
# Every file above is produced by this Makefile, so clean removes all of them.
clean:
\trm -f blah blah.o blah.c
"""

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_three_step_chain",
        title="Generate, compile, link",
        objective=(
            "Build blah in three steps: blah from blah.o, blah.o from blah.c, "
            "and a rule that creates blah.c itself."
        ),
        reference="More quick examples",
        hint=(
            "Work backwards from the goal: blah needs blah.o, blah.o needs "
            "blah.c, and the rule for blah.c has no prerequisites at all, so "
            "its recipe is the first one make runs."
        ),
        makefile=CHAIN,
        steps=[
            mk(
                stdout=CHAIN_OUTPUT,
                description="make starts at the deepest prerequisite and links last",
            ),
            step("test", "-x", "blah", description="the build produced an executable"),
            mk(
                stdout="make: 'blah' is up to date.",
                stdout_mode="contains",
                description="with every file in place there is nothing left to do",
            ),
        ],
        breaks=[
            (
                "blah: blah.o\n\tcc blah.o -o blah # Runs third\n\n"
                "blah.o: blah.c\n\tcc -c blah.c -o blah.o # Runs second",
                "blah.o: blah.c\n\tcc -c blah.c -o blah.o # Runs second\n\n"
                "blah: blah.o\n\tcc blah.o -o blah # Runs third",
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="02_delete_a_source_reruns_everything",
        title="Deleting a source re-runs the whole chain",
        objective=(
            "Keep the three rules in place, then watch what happens when the "
            "generated blah.c is deleted: every recipe runs again."
        ),
        reference="More quick examples",
        hint=(
            "blah.o must list blah.c as a prerequisite, or make never notices "
            "that the file is gone. Only a prerequisite makes make look at a "
            "file that is missing."
        ),
        makefile=CHAIN,
        steps=[
            mk(
                stdout=CHAIN_OUTPUT,
                description="the first build runs all three recipes",
            ),
            step("rm", "-f", "blah.c", description="throw the generated source away"),
            mk(
                stdout=CHAIN_OUTPUT,
                description="make regenerates blah.c, recompiles and relinks",
            ),
            mk(
                stdout="make: 'blah' is up to date.",
                stdout_mode="contains",
                description="the rebuild is complete, so a third run is quiet",
            ),
        ],
        breaks=[
            (
                "blah.o: blah.c\n\tcc -c blah.c -o blah.o # Runs second",
                "blah.o:\n\tcc -c blah.c -o blah.o # Runs second",
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="03_touching_an_intermediate_file",
        title="Touching an intermediate file rebuilds part of the chain",
        objective=(
            "Give blah.o its blah.c prerequisite so that touching either file "
            "rebuilds exactly as much as it has to."
        ),
        reference="More quick examples",
        hint=(
            "Touching blah.c makes it newer than blah.o, so the object is "
            "recompiled and, being newer than blah, the program is relinked. "
            "Touching blah.o alone only relinks."
        ),
        makefile="""
blah: blah.o
\tcc blah.o -o blah

blah.o: blah.c
\tcc -c blah.c -o blah.o
""",
        steps=[
            mk(
                stdout="cc -c blah.c -o blah.o\ncc blah.o -o blah",
                description="the object is compiled before the program is linked",
            ),
            step("touch", "blah.c", description="pretend the source was edited"),
            mk(
                stdout="cc -c blah.c -o blah.o\ncc blah.o -o blah",
                description="a newer source recompiles and the fresh object relinks",
            ),
            step("touch", "blah.o", description="pretend only the object was touched"),
            mk(
                stdout="cc blah.o -o blah",
                stdout_mode="exact",
                description="a newer object relinks the program and runs nothing else",
            ),
        ],
        breaks=[
            (
                "blah.o: blah.c\n\tcc -c blah.c -o blah.o",
                "blah.o:\n\tcc -c blah.c -o blah.o",
            )
        ],
        files={"blah.c": "int main(void) { return 0; }\n"},
    ),
    ex(
        topic=TOPIC,
        slug="04_prerequisite_that_is_never_created",
        title="A prerequisite that is never created",
        objective=(
            "Make some_file depend on other_file, a target whose recipe never "
            "creates a file, so that both recipes run every single time."
        ),
        reference="More quick examples",
        hint=(
            "make decides a target is out of date when a prerequisite is "
            "missing or newer than it. other_file stays missing forever, so "
            "some_file can never be up to date."
        ),
        makefile="""
some_file: other_file
\techo "This will always run, and runs second"
\ttouch some_file

other_file:
\techo "This will always run, and runs first"
""",
        steps=[
            mk(
                stdout=(
                    'echo "This will always run, and runs first"\n'
                    "This will always run, and runs first\n"
                    'echo "This will always run, and runs second"\n'
                    "This will always run, and runs second\n"
                    "touch some_file"
                ),
                description="other_file is built before the target that needs it",
            ),
            step("test", "-f", "some_file", description="the recipe created some_file"),
            mk(
                stdout=(
                    'echo "This will always run, and runs first"\n'
                    'echo "This will always run, and runs second"'
                ),
                description="both recipes run again even though some_file exists",
            ),
        ],
        breaks=[("some_file: other_file", "some_file:")],
    ),
    ex(
        topic=TOPIC,
        slug="05_several_goals_on_one_line",
        title="Several goals on one command line",
        objective=(
            "Ask make for two targets at once and see that it builds them "
            "left to right, while a bare make still builds only the first."
        ),
        reference="More quick examples",
        hint=(
            "Goals on the command line are handled in the order you type them. "
            "Each one is finished before the next begins, unless one target is "
            "a prerequisite of the other."
        ),
        makefile="""
one.txt:
\techo "one" > one.txt

two.txt:
\techo "two" > two.txt
""",
        steps=[
            mk(
                "two.txt",
                "one.txt",
                stdout='echo "two" > two.txt\necho "one" > one.txt',
                description="the goals run in the order they were named",
            ),
            step(
                "rm",
                "-f",
                "one.txt",
                "two.txt",
                description="start again with no files in the directory",
            ),
            mk(
                "one.txt",
                "two.txt",
                stdout='echo "one" > one.txt\necho "two" > two.txt',
                description="reversing the goals reverses the order",
            ),
            mk(
                stdout="make: 'one.txt' is up to date.",
                stdout_mode="contains",
                description="a bare make only considers the first target",
            ),
        ],
        breaks=[
            (
                'two.txt:\n\techo "two" > two.txt',
                'two.txt: one.txt\n\techo "two" > two.txt',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="06_four_step_chain",
        title="A four-step chain",
        objective=(
            "Extend the build with a fourth rule, so that blah.c is copied from "
            "source.txt, which is itself written by a recipe."
        ),
        reference="More quick examples",
        hint=(
            "Every step needs a rule and a prerequisite that points at the step "
            "before it. source.txt comes first, then blah.c, blah.o and blah."
        ),
        makefile="""
blah: blah.o
\tcc blah.o -o blah

blah.o: blah.c
\tcc -c blah.c -o blah.o

blah.c: source.txt
\tcp source.txt blah.c

source.txt:
\techo "int main() { return 0; }" > source.txt
""",
        steps=[
            mk(
                stdout=(
                    'echo "int main() { return 0; }" > source.txt\n'
                    "cp source.txt blah.c\n"
                    "cc -c blah.c -o blah.o\n"
                    "cc blah.o -o blah"
                ),
                description="all four recipes run, deepest first",
            ),
            mk(
                stdout="make: 'blah' is up to date.",
                stdout_mode="contains",
                description="a second run has nothing to do",
            ),
            step("rm", "-f", "blah.c", description="delete a middle file of the chain"),
            mk(
                stdout="cp source.txt blah.c\ncc -c blah.c -o blah.o\ncc blah.o -o blah",
                description="only the three steps below the deleted file run again",
            ),
        ],
        breaks=[("blah.c: source.txt", "blah.c:")],
    ),
    ex(
        topic=TOPIC,
        slug="07_shared_prerequisite",
        title="A wider graph with a shared prerequisite",
        objective=(
            "Build a report from two files that are both copied from the same "
            "base file, and confirm the order the recipes run in."
        ),
        reference="More quick examples",
        hint=(
            "Prerequisites are worked through from left to right, so base.txt "
            "is made first for left.txt, and is already up to date by the time "
            "right.txt asks for it."
        ),
        makefile="""
report: left.txt right.txt
\tcat left.txt right.txt > report

left.txt: base.txt
\tcp base.txt left.txt

right.txt: base.txt
\tcp base.txt right.txt

base.txt:
\techo "base" > base.txt
""",
        steps=[
            mk(
                stdout=(
                    'echo "base" > base.txt\n'
                    "cp base.txt left.txt\n"
                    "cp base.txt right.txt\n"
                    "cat left.txt right.txt > report"
                ),
                description="the shared file is built once, before either copy",
            ),
            step(
                "cat",
                "report",
                stdout="base\nbase",
                description="the report holds both copies of the shared file",
            ),
            mk(
                stdout="make: 'report' is up to date.",
                stdout_mode="contains",
                description="nothing is out of date on a second run",
            ),
        ],
        breaks=[("report: left.txt right.txt", "report: left.txt")],
    ),
    ex(
        topic=TOPIC,
        slug="08_clean_can_run_twice",
        title="clean removes what make built",
        objective=(
            "Add a clean target that deletes some_file and can be run again "
            "when there is nothing left to delete."
        ),
        reference="Make clean",
        hint=(
            "clean is an ordinary target: it is not first, and nothing depends "
            "on it, so it only runs when you ask for it. Give rm the -f flag so "
            "that a second clean is not an error."
        ),
        makefile="""
some_file:
\ttouch some_file

clean:
\trm -f some_file
""",
        steps=[
            mk(stdout="touch some_file", description="make creates the file"),
            step("test", "-f", "some_file", description="the file is there to delete"),
            mk(
                "clean",
                stdout="rm -f some_file",
                missing=["some_file"],
                description="make clean deletes it",
            ),
            mk(
                "clean",
                stdout="rm -f some_file",
                missing=["some_file"],
                description="a second clean is harmless",
            ),
        ],
        breaks=[("\trm -f some_file", "\trm some_file")],
    ),
    ex(
        topic=TOPIC,
        slug="09_a_file_named_clean",
        title="A file called clean stops the recipe",
        objective=(
            "Make clean run even though the directory contains a stray file "
            "with the same name as the target."
        ),
        reference="Make clean",
        hint=(
            "clean is not a special word in make: the target is matched against "
            "the filesystem like any other. Declare it .PHONY so make always "
            "runs the recipe."
        ),
        makefile="""
.PHONY: clean

some_file:
\ttouch some_file

clean:
\trm -f some_file
""",
        steps=[
            mk(stdout="touch some_file", description="make creates the file"),
            step("test", "-f", "some_file", description="the file is there to delete"),
            mk(
                "clean",
                stdout="rm -f some_file",
                missing=["some_file"],
                description="the recipe runs even though a file called clean exists",
            ),
        ],
        breaks=[(".PHONY: clean\n\nsome_file:", "some_file:")],
        files={
            "clean": (
                "# A stray file that happens to be called clean.\n"
                "# Nothing in the build uses it; it is here so that the clean\n"
                "# target has to fight the filesystem.\n"
            )
        },
    ),
    ex(
        topic=TOPIC,
        slug="10_build_clean_build",
        title="Build, clean, build again",
        objective=(
            "Complete the Makefile with a clean target that removes everything "
            "make created, so the same three recipes can run from scratch again."
        ),
        reference="Make clean",
        hint=(
            "clean should delete every file the other rules produce, including "
            "the generated blah.c. After it runs, make must be able to rebuild "
            "the program from nothing."
        ),
        makefile=CHAIN_WITH_CLEAN,
        steps=[
            mk(stdout=CHAIN_OUTPUT, description="the first build runs all three recipes"),
            mk(
                "clean",
                stdout="rm -f blah blah.o blah.c",
                missing=["blah", "blah.o", "blah.c"],
                description="clean leaves the directory as it found it",
            ),
            mk(
                stdout=CHAIN_OUTPUT,
                description="the same three recipes run again from a clean tree",
            ),
            step("test", "-x", "blah", description="the rebuilt program is executable"),
        ],
        breaks=[("rm -f blah blah.o blah.c", "rm -f blah blah.o")],
    ),
]
