"""Exercises for the tutorial's "Other Features" chapter.

Recipe lines inside the ``makefile`` strings are indented with a ``\\t`` escape.
Python turns that into a real tab, which is what make requires; writing a
literal tab into the source would be invisible and easy to lose.  A backslash
that must reach the Makefile (a line continuation, for instance) is written
``\\\\``, and ``$$`` stays ``$$``.
"""

from spec import ex, mk, step

TOPIC = "11_other_features"

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_include_variables",
        title="Include another file's variables",
        objective=(
            "Move the project settings out of the Makefile into config.mk and "
            "include that file, so the recipes can still see the variables."
        ),
        reference="Include Makefiles",
        hint=(
            "The directive is a line of its own: include config.mk. make reads "
            "that file while it parses the Makefile, so everything it defines "
            "is available from that point on."
        ),
        makefile="""
include config.mk

all: banner
\techo "build $(NAME)"

banner:
\techo "starting $(NAME)"

settings:
\techo "$(GREETING), $(NAME)"
""",
        steps=[
            mk(
                stdout="starting makeling\nbuild makeling",
                description="the recipes use variables that live in config.mk",
            ),
            mk(
                "settings",
                stdout="hello, makeling",
                description="both included variables are defined",
            ),
        ],
        breaks=[("include config.mk", "# include config.mk")],
        files={"config.mk": "GREETING = hello\nNAME = makeling\n"},
    ),
    ex(
        topic=TOPIC,
        slug="02_include_rules",
        title="Rules from the included file are part of the build",
        objective=(
            "Keep the build rules in tools.mk and include it: the rules must "
            "work and the included file's first target becomes the default goal."
        ),
        reference="Include Makefiles",
        hint=(
            "include is textual: the rules in tools.mk behave as if they were "
            "written in the Makefile, including the rule that decides the "
            "default goal."
        ),
        makefile="""
# The build rules live in tools.mk.
include tools.mk
""",
        steps=[
            mk(
                stdout="building with the included rule\nall done",
                description="a bare make runs the goal found in tools.mk",
            ),
            mk(
                "build",
                stdout="building with the included rule",
                description="the included rule can still be named directly",
            ),
            mk(
                "clean",
                stdout="cleaning up",
                description="the included clean rule is there too",
            ),
        ],
        breaks=[("include tools.mk", "# include tools.mk")],
        files={
            "tools.mk": """
all: build
\techo "all done"

build:
\techo "building with the included rule"

clean:
\techo "cleaning up"
""",
        },
    ),
    ex(
        topic=TOPIC,
        slug="03_include_optional",
        title="An include that may not exist yet",
        objective=(
            "Read deps.mk when it is there and carry on when it is not, so a "
            "fresh checkout still builds."
        ),
        reference="Include Makefiles",
        hint=(
            "A leading dash on the include line tells make that a missing file "
            "is not an error. Without it make tries to build the missing file "
            "and stops when no rule can."
        ),
        makefile="""
-include deps.mk

report: notes.txt
\tcat notes.txt > report
""",
        steps=[
            mk(
                stdout="cat notes.txt > report",
                description="the build runs even though deps.mk does not exist",
            ),
            mk(
                stdout="make: 'report' is up to date.",
                description="the report is built, nothing is left to do",
            ),
            step(
                "test",
                "!",
                "-f",
                "deps.mk",
                description="make did not invent the optional file",
            ),
        ],
        breaks=[("-include deps.mk", "include deps.mk")],
        files={"notes.txt": "the optional include never stops the build\n"},
    ),
    ex(
        topic=TOPIC,
        slug="04_include_generated",
        title="Make rebuilds a makefile it includes",
        objective=(
            "Give make a rule for version.mk and include it, so the version "
            "file is generated on the first run and reread."
        ),
        reference="Include Makefiles",
        hint=(
            "Before giving up on an included file make looks for a rule that "
            "can build it. Add the rule and keep the include optional so the "
            "very first run can still start."
        ),
        makefile="""
-include version.mk

VERSION ?= unknown

all:
\techo "version $(VERSION)"

version.mk:
\techo "VERSION = 1.0" > version.mk
""",
        steps=[
            mk(
                stdout='echo "VERSION = 1.0" > version.mk\nversion 1.0',
                description="make builds the included file, rereads it, then builds all",
            ),
            step(
                "cat",
                "version.mk",
                stdout="VERSION = 1.0",
                description="the rule wrote the file make then included",
            ),
            mk(
                stdout='echo "VERSION = 1.0"',
                stdout_mode="not_contains",
                description="the up to date version.mk is not generated again",
            ),
        ],
        breaks=[("-include version.mk", "# include version.mk")],
    ),
    ex(
        topic=TOPIC,
        slug="05_include_generated_deps",
        title="The generated dependency file",
        objective=(
            "Include report.d, the file a compiler writes with -M, so that "
            "make learns which sources the report is built from."
        ),
        reference="Include Makefiles",
        hint=(
            "report.d holds one rule that adds prerequisites to report. Point "
            "the include at the file that is actually in the directory: the "
            "leading dash hides a misspelled name."
        ),
        makefile="""
# report.d is what cc -M writes on an earlier build.
-include report.d

report:
\tcat notes.txt > report
""",
        steps=[
            mk(
                "report",
                stdout="cat notes.txt > report",
                description="the rule in the Makefile builds the report",
            ),
            mk(
                "report",
                stdout="make: 'report' is up to date.",
                description="the report is now up to date",
            ),
            step(
                "cat",
                "report",
                stdout="line one\nline two",
                description="the report holds both lines of notes.txt",
            ),
            # The report was built a moment ago.  Dating both files explicitly
            # keeps this a real comparison even where the filesystem stamps
            # them a whole second apart at best.
            step(
                "touch",
                "-t",
                "202001010000",
                "report",
                description="age the built report",
            ),
            step(
                "touch",
                "-t",
                "202101010000",
                "notes.txt",
                description="make the source newer than the report",
            ),
            mk(
                "report",
                stdout="cat notes.txt > report",
                description="the prerequisite from report.d triggers a rebuild",
            ),
        ],
        breaks=[("-include report.d", "-include report.mk")],
        files={
            "notes.txt": "line one\nline two\n",
            "report.d": "report: notes.txt\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="06_vpath_headers",
        title="Finding a prerequisite in another directory",
        objective=(
            "Use vpath so that blah.h, which only exists in headers/, is found "
            "as a prerequisite of some_binary."
        ),
        reference="The vpath Directive",
        hint=(
            "vpath takes a pattern and the directories to search: vpath %.h "
            "headers. The recipe must still copy the file make found, so use "
            "the automatic variable $< rather than the bare file name."
        ),
        makefile="""
vpath %.h headers

some_binary: blah.h
\tcat $< > some_binary
""",
        steps=[
            mk(
                "some_binary",
                stdout="cat headers/blah.h > some_binary",
                description="make found the header through the vpath directive",
            ),
            step(
                "cat",
                "some_binary",
                stdout="hello from the header",
                description="the recipe copied the header make handed it",
            ),
            mk(
                "some_binary",
                stdout="make: 'some_binary' is up to date.",
                description="the header was found, so there is nothing left to do",
            ),
        ],
        breaks=[("vpath %.h headers\n\n", "")],
        files={"headers/blah.h": "hello from the header\n"},
    ),
    ex(
        topic=TOPIC,
        slug="07_vpath_clear",
        title="Clearing a stale search path",
        objective=(
            "Forget the old headers directory before adding the new one, so "
            "that blah.h resolves to the file in new/."
        ),
        reference="The vpath Directive",
        hint=(
            "A vpath directive with no pattern clears every search path added "
            "so far. Without it the earlier directory is still searched first "
            "and its stale header wins."
        ),
        makefile="""
vpath %.h old

vpath

vpath %.h new

some_binary: blah.h
\tcat $< > some_binary
""",
        steps=[
            mk(
                "some_binary",
                stdout="cat new/blah.h > some_binary",
                description="the stale directory is no longer searched",
            ),
            step(
                "cat",
                "some_binary",
                stdout="fresh header",
                description="the new header is the one that was copied",
            ),
        ],
        breaks=[("vpath %.h old\n\nvpath\n\n", "vpath %.h old\n\n")],
        files={
            "old/blah.h": "stale header\n",
            "new/blah.h": "fresh header\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="08_vpath_variable",
        title="VPATH searches for every prerequisite",
        objective=(
            "Point VPATH at both directories that hold prerequisites, so "
            "blah.h and extra.txt are found without a vpath pattern."
        ),
        reference="The vpath Directive",
        hint=(
            "VPATH is a variable listing directories, separated by spaces or "
            "colons, and it applies to every prerequisite. Naming only the "
            "first directory leaves the second file unfindable."
        ),
        makefile="""
VPATH = headers libs

some_binary: blah.h extra.txt
\tcat $^ > some_binary
""",
        steps=[
            mk(
                stdout="cat headers/blah.h libs/extra.txt > some_binary",
                description="both prerequisites were found through VPATH",
            ),
            step(
                "cat",
                "some_binary",
                stdout="hello from the header\nplus extra",
                description="the recipe copied each file from its own directory",
            ),
        ],
        breaks=[("VPATH = headers libs", "VPATH = headers")],
        files={
            "headers/blah.h": "hello from the header\n",
            "libs/extra.txt": "plus extra\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="09_multiline_recipe",
        title="A recipe line that continues",
        objective=(
            "Break one long shell command over two lines with a backslash so "
            "that the shell still receives it as a single command."
        ),
        reference="Multiline",
        hint=(
            "End the first line with a backslash: make hands the continuation "
            "to the shell, which removes the backslash and the newline. "
            "Without it the second line becomes a command of its own."
        ),
        makefile="""
greeting.txt:
\techo one two three \\
\t\tfour five six > greeting.txt
""",
        steps=[
            mk(
                stdout="echo one two three \\",
                stdout_mode="contains",
                files={"greeting.txt": "one two three four five six\n"},
                description="one echo wrote one line into the file",
            ),
            mk(
                stdout="make: 'greeting.txt' is up to date.",
                description="the file was written, so make has nothing to do",
            ),
        ],
        breaks=[("echo one two three \\", "echo one two three")],
    ),
    ex(
        topic=TOPIC,
        slug="10_multiline_variable",
        title="A variable that spans lines",
        objective=(
            "Continue the SOURCES variable onto a second line, so the list "
            "works both as prerequisites and as a value."
        ),
        reference="Multiline",
        hint=(
            "A continued assignment also needs the trailing backslash, but "
            "here make joins the lines itself, collapsing the backslash, the "
            "newline and the following spaces into a single space. Indent the "
            "continuation with spaces, never a tab."
        ),
        makefile="""
SOURCES = one.txt \\
          two.txt

combined.txt: $(SOURCES)
\tcat $(SOURCES) > combined.txt

show:
\techo "[$(SOURCES)]"
""",
        steps=[
            mk(
                stdout="cat one.txt two.txt > combined.txt",
                files={"combined.txt": "one\ntwo\n"},
                description="the joined value is a two word prerequisite list",
            ),
            mk(
                "show",
                stdout="[one.txt two.txt]",
                description="the backslash, the newline and the indent became one space",
            ),
            step(
                "touch",
                "-t",
                "202001010000",
                "combined.txt",
                description="age the built file",
            ),
            step(
                "touch",
                "-t",
                "202101010000",
                "one.txt",
                description="make the first source newer",
            ),
            mk(
                stdout="cat one.txt two.txt > combined.txt",
                description="both words really are prerequisites",
            ),
        ],
        breaks=[("SOURCES = one.txt \\", "SOURCES = one.txt")],
        files={
            "one.txt": "one\n",
            "two.txt": "two\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="11_phony_file_conflict",
        title="A phony target is never up to date",
        objective=(
            "Declare clean phony so that the file named clean, created by "
            "some_file, cannot stop the clean rule from running."
        ),
        reference=".phony",
        hint=(
            ".PHONY: clean tells make to ignore any file with that name. "
            "Without the declaration make sees the file clean, decides the "
            "target is up to date and skips the recipe."
        ),
        makefile="""
some_file:
\ttouch some_file
\ttouch clean

.PHONY: clean
clean:
\trm -f some_file
\trm -f clean
""",
        steps=[
            mk(
                "some_file",
                stdout="touch some_file\ntouch clean",
                description="building some_file also creates a file called clean",
            ),
            step(
                "test",
                "-f",
                "clean",
                description="the decoy file is really there",
            ),
            mk(
                "clean",
                stdout="rm -f some_file\nrm -f clean",
                missing=["some_file", "clean"],
                description="clean runs anyway and removes both files",
            ),
        ],
        breaks=[(".PHONY: clean\n", "")],
    ),
    ex(
        topic=TOPIC,
        slug="12_phony_conventional_targets",
        title="all, clean and install are phony",
        objective=(
            "Declare the conventional targets phony so a file named install "
            "and a directory named clean cannot shadow them."
        ),
        reference=".phony",
        hint=(
            "One .PHONY line can list several targets: .PHONY: all clean "
            "install. A phony target is out of date whenever make looks at it, "
            "whatever files share its name."
        ),
        makefile="""
.PHONY: all clean install

all: app.txt

app.txt: notes.txt
\tcp notes.txt app.txt

install:
\tcp app.txt installed.txt

clean:
\trm -f app.txt installed.txt
""",
        steps=[
            mk(
                stdout="cp notes.txt app.txt",
                files={"app.txt": "notes from makeling\n"},
                description="the default goal builds the application file",
            ),
            mk(
                "install",
                files={"installed.txt": "notes from makeling\n"},
                description="install runs even though a file of that name exists",
            ),
            mk(
                "clean",
                stdout="rm -f app.txt installed.txt",
                missing=["app.txt", "installed.txt"],
                description="clean runs even though a directory of that name exists",
            ),
        ],
        breaks=[(".PHONY: all clean install\n\n", "")],
        files={
            "notes.txt": "notes from makeling\n",
            "install": "install notes shipped with the source\n",
            "clean/leftover.txt": "left behind by an earlier build\n",
        },
    ),
    ex(
        topic=TOPIC,
        slug="13_delete_on_error",
        title="Delete the target of a failed rule",
        objective=(
            "Switch on DELETE_ON_ERROR so that a rule which fails halfway "
            "leaves no half written target behind."
        ),
        reference=".delete_on_error",
        hint=(
            "The declaration is a target line with no recipe: "
            ".DELETE_ON_ERROR:, starting in column one. It applies to every "
            "rule in the makefile, not only to the rule beneath it."
        ),
        makefile="""
.DELETE_ON_ERROR:

all: one two

one:
\ttouch one
\tfalse

two:
\ttouch two
\tfalse
""",
        steps=[
            mk(
                exit_code=2,
                missing=["one"],
                stdout="touch one\nfalse",
                stderr="Deleting file 'one'",
                description="the file written by the failing rule is removed",
            ),
            mk(
                "two",
                exit_code=2,
                missing=["two"],
                stdout="touch two\nfalse",
                stderr="Deleting file 'two'",
                description="the declaration is not tied to the target that follows it",
            ),
        ],
        breaks=[(".DELETE_ON_ERROR:\n\n", "")],
    ),
    ex(
        topic=TOPIC,
        slug="14_delete_on_error_default",
        title="Without DELETE_ON_ERROR the target stays",
        objective=(
            "Turn the declaration off to see make's default: a rule that fails "
            "leaves its half written target on disk."
        ),
        reference=".delete_on_error",
        hint=(
            "Historical default: make only reports the error. Remove the "
            ".DELETE_ON_ERROR line and the half written file survives, which "
            "is why the next build may think the target is up to date."
        ),
        makefile="""
halfway.txt:
\techo "half written" > halfway.txt
\tfalse
""",
        steps=[
            mk(
                "halfway.txt",
                exit_code=2,
                stdout='echo "half written" > halfway.txt',
                stderr="Error 1",
                files={"halfway.txt": "half written\n"},
                description="the failing rule leaves its half written file behind",
            ),
            mk(
                "halfway.txt",
                stdout="make: 'halfway.txt' is up to date.",
                files={"halfway.txt": "half written\n"},
                description="the leftover file even looks up to date on the next run",
            ),
        ],
        breaks=[
            (
                "halfway.txt:\n",
                ".DELETE_ON_ERROR:\n\nhalfway.txt:\n",
            )
        ],
    ),
]
