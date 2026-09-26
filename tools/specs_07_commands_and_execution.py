"""Exercises for the tutorial's "Commands and execution" chapter.

Recipe lines inside the ``makefile`` strings are indented with a ``\\t``
escape: Python turns that into a real tab, which is what make requires.  A
backslash that must survive into the Makefile (a line continuation) is written
``\\\\``, and a shell dollar is written ``$$`` exactly as make wants it.

Every expectation below was copied from a real run of the command in a scratch
directory; make prints the commands it runs, the ``make[1]:`` directory lines
and its diagnostics in exactly these shapes.
"""

from spec import ex, mk, step

TOPIC = "07_commands_and_execution"

SPECS = [
    ex(
        topic=TOPIC,
        slug="01_silencing_one_line",
        title="Make echoes each command before running it",
        objective=(
            "Watch make print a recipe line before running it, and keep one "
            "line out of that echo with @."
        ),
        reference="Command Echoing/Silencing",
        hint=(
            "make writes every recipe line to stdout and then runs it, so you "
            "see the command and its output. An @ at the start of a line stops "
            "the printing for that line only; the command still runs."
        ),
        makefile="""
all:
\t@echo "this line runs, but make does not print it"
\techo "make prints this line before running it"
""",
        steps=[
            mk(
                stdout="""this line runs, but make does not print it
echo "make prints this line before running it"
make prints this line before running it""",
                description="the silent line's output appears without its command",
            ),
            mk(
                stdout='echo "this line runs, but make does not print it"',
                stdout_mode="not_contains",
                description="the @ line is never echoed",
            ),
        ],
        breaks=[
            (
                '\t@echo "this line runs, but make does not print it"',
                '\techo "this line runs, but make does not print it"',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="02_silencing_a_whole_target",
        title="Silencing a target, or the whole run",
        objective=(
            "Keep one target's commands out of the output with .SILENT, and "
            "compare that with make -s, which silences everything."
        ),
        reference="Command Echoing/Silencing",
        hint=(
            ".SILENT: quiet silences just that target. With no prerequisites "
            "at all, .SILENT: silences every target; make -s (or --silent) "
            "does the same for one run without touching the Makefile."
        ),
        makefile="""
all: quiet loud

quiet:
\techo "quiet target ran"

loud:
\techo "loud target ran"

.SILENT: quiet
""",
        steps=[
            mk(
                stdout="""quiet target ran
echo "loud target ran"
loud target ran""",
                description="only the quiet target hides its command",
            ),
            mk(
                "-s",
                stdout="""quiet target ran
loud target ran""",
                description="make -s runs both targets silently",
            ),
            mk(
                "--silent",
                stdout="echo",
                stdout_mode="not_contains",
                description="--silent prints no command at all",
            ),
        ],
        breaks=[(".SILENT: quiet", ".SILENT:")],
    ),
    ex(
        topic=TOPIC,
        slug="03_one_shell_per_line",
        title="Each recipe line runs in its own shell",
        objective=(
            "Prove that a cd on one recipe line does not reach the next line, "
            "and that joining two commands with a semicolon does."
        ),
        reference="Command Execution",
        hint=(
            "make hands every recipe line to its own shell, so a cd or a shell "
            "variable is forgotten as soon as the line ends. Put both commands "
            "on one line to keep them in the same shell."
        ),
        makefile="""
all:
\t@mkdir -p deeper
\tcd deeper
\t@pwd
\tcd deeper; pwd
""",
        steps=[
            mk(
                stdout="""cd deeper
<stage>
cd deeper; pwd
<stage>/deeper""",
                description="the lone cd has no effect, the joined one does",
            ),
        ],
        breaks=[("\tcd deeper; pwd", "\tcd deeper\n\t@pwd")],
    ),
    ex(
        topic=TOPIC,
        slug="04_continuation_keeps_one_shell",
        title="Shell state survives across a line continuation",
        objective=(
            "Show that a shell variable set on one line is gone by the next, "
            "and keep it alive by continuing the recipe line with a backslash."
        ),
        reference="Command Execution",
        hint=(
            "A make variable reaches every line, but a shell variable only "
            "lives inside the one shell that set it. Ending a line with "
            "backslash-newline keeps the next line in that same shell."
        ),
        makefile="""
MAKE_NOTE = set in the Makefile

all:
\tmessage="set in line one"
\techo "next line sees: [$$message]"
\tmessage="set again"; \\
\techo "continuation sees: [$$message]"
\t@echo "the make variable survives anyway: [$(MAKE_NOTE)]"
""",
        steps=[
            mk(
                stdout="""message="set in line one"
echo "next line sees: [$message]"
next line sees: []
message="set again"; \\
echo "continuation sees: [$message]"
continuation sees: [set again]
the make variable survives anyway: [set in the Makefile]""",
                description="the shell variable only survives inside one shell",
            ),
        ],
        breaks=[
            (
                'message="set again"; \\\n\techo "continuation sees: [$$message]"',
                'message="set again";\n\techo "continuation sees: [$$message]"',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="05_the_default_shell_is_sh",
        title="The shell is the SHELL variable",
        objective=(
            "Look at which program runs your recipe lines, and change it by "
            "giving make a different SHELL."
        ),
        reference="Default Shell",
        hint=(
            "make runs recipes with /bin/sh unless the variable SHELL says "
            "otherwise. The shell's own $0 is the name of the program running "
            "the line; SHELL can be set in the Makefile or on the command line."
        ),
        makefile="""
which_shell:
\t@echo "SHELL is: $(SHELL)"
\t@echo "this line was run by: $${0}"
""",
        steps=[
            mk(
                stdout="""SHELL is: /bin/sh
this line was run by: /bin/sh""",
                description="the default shell is /bin/sh",
            ),
            mk(
                "SHELL=/bin/bash",
                stdout="""SHELL is: /bin/bash
this line was run by: /bin/bash""",
                description="SHELL on the command line switches the shell",
            ),
            mk(
                "-f",
                "bash.mk",
                stdout="""SHELL is: /bin/bash
this line was run by: /bin/bash""",
                description="SHELL := /bin/bash in the Makefile does the same",
            ),
        ],
        breaks=[],
        files={
            "bash.mk": """
SHELL := /bin/bash

which_shell:
\t@echo "SHELL is: $(SHELL)"
\t@echo "this line was run by: $${0}"
""",
        },
        file_breaks=[
            ("bash.mk", "SHELL := /bin/bash", "SHELL := /bin/sh"),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="06_shellflags",
        title=".SHELLFLAGS decides how the shell is called",
        objective=(
            "Make a recipe line stop at its first failing command by adding -e "
            "to .SHELLFLAGS, and see what the default -c does instead."
        ),
        reference="Default Shell",
        hint=(
            "make calls $(SHELL) with $(.SHELLFLAGS), which is just -c by "
            "default. Add -e to it and a line like 'false; touch marker' stops "
            "after the failure instead of reaching the touch."
        ),
        makefile="""
.SHELLFLAGS := -ec

all:
\t@echo "shell flags: $(.SHELLFLAGS)"
\tfalse; touch carried_on.marker
""",
        steps=[
            mk(
                exit_code=2,
                stdout="shell flags: -ec",
                stderr="make: *** [Makefile:11: all] Error 1",
                missing=["carried_on.marker"],
                description="with -e the shell gives up at the failing command",
            ),
            mk(
                "-f",
                "default.mk",
                stdout="shell flags: -c",
                files={"default_carried_on.marker": ""},
                description="without -e the same line carries on to the touch",
            ),
        ],
        breaks=[(".SHELLFLAGS := -ec\n\n", "")],
        files={
            "default.mk": """
loose:
\t@echo "shell flags: $(.SHELLFLAGS)"
\tfalse; touch default_carried_on.marker
""",
        },
    ),
    ex(
        topic=TOPIC,
        slug="07_parallel_jobs",
        title="make -j runs the goals as parallel jobs",
        objective=(
            "Ask make for two jobs at once with -j2 and read the flags it "
            "hands to the recipe: the -j2 and the jobserver behind it."
        ),
        reference="Arguments to make",
        hint=(
            "make -j2 runs the goal's prerequisites as separate jobs, so their "
            "output may arrive in any order. $(MAKEFLAGS) inside a recipe shows "
            "the -j2 and the jobserver make shares with nested makes."
        ),
        makefile="""
all: one two
\t@echo "jobs make handed the recipe: [$(MAKEFLAGS)]"

one:
\t@echo "job one finished"

two:
\t@echo "job two finished"
""",
        steps=[
            mk(
                "-j2",
                stdout="""job one finished
job two finished""",
                stdout_mode="contains_lines",
                description="both jobs run, in whichever order they finish",
            ),
            mk(
                "-j2",
                stdout=r"jobs make handed the recipe: \[ -j2 --jobserver-auth=[0-9]+,[0-9]+\]",
                stdout_mode="regex",
                description="the recipe sees -j2 and the jobserver",
            ),
            mk(
                "-j1",
                stdout="jobs make handed the recipe: [ -j1]",
                description="one job at a time needs no jobserver",
            ),
            mk(
                stdout="jobs make handed the recipe: []",
                description="without -j there is nothing to hand over",
            ),
        ],
        breaks=[("all: one two", "all: one")],
    ),
    ex(
        topic=TOPIC,
        slug="08_make_variables_vs_shell_variables",
        title="A make variable is not a shell variable",
        objective=(
            "Give the shell a variable of its own in a recipe line, and see "
            "why $(...) and $$... are not interchangeable."
        ),
        reference="Double dollar sign",
        hint=(
            "make expands $(name) itself before the shell ever sees the line. "
            "Write $$name when the shell - not make - is supposed to read the "
            "variable; with a single $ make eats the name and the shell gets "
            "the leftovers."
        ),
        makefile="""
make_var = I am a make variable

all:
\tsh_var='I am a shell variable'; echo $$sh_var
\techo $(make_var)
""",
        steps=[
            mk(
                stdout="""sh_var='I am a shell variable'; echo $sh_var
I am a shell variable
echo I am a make variable
I am a make variable""",
                description="$$ reaches the shell, $( ) is expanded by make",
            ),
            mk(
                stdout="echo h_var",
                stdout_mode="not_contains",
                description="a single $ leaves the shell with the wrong text",
            ),
        ],
        breaks=[("echo $$sh_var", "echo $sh_var")],
    ),
    ex(
        topic=TOPIC,
        slug="09_literal_dollars",
        title="Dollars that must survive into the shell",
        objective=(
            "Print a literal dollar sign, a command substitution and a loop "
            "variable by doubling the dollars make would otherwise eat."
        ),
        reference="Double dollar sign",
        hint=(
            "Every $$ becomes one $ once make has expanded the line, so $$$$ "
            "hands the shell two dollars and $$(cmd) hands it a command "
            "substitution. Quoting decides what the shell then does with them."
        ),
        makefile="""
report:
\t@echo 'a literal dollar: $$$$'
\t@echo "a command substitution: $$(echo hi)"
\t@echo "make expanded the target name: [$@]"
\t@echo "the shell's positional list is empty: [$$@]"
\t@for i in 1 2 3; do echo "item $$i"; done
""",
        steps=[
            mk(
                stdout="""a literal dollar: $$
a command substitution: hi
make expanded the target name: [report]
the shell's positional list is empty: []
item 1
item 2
item 3""",
                description="each escaped dollar does its own job",
            ),
        ],
        breaks=[
            ("a literal dollar: $$$$'", "a literal dollar: $$'"),
            ("positional list is empty: [$$@]", "positional list is empty: [$@]"),
        ],
    ),
    ex(
        topic=TOPIC,
        slug="10_error_stops_make",
        title="make gives up at the first failing command",
        objective=(
            "Run a command that fails and confirm that make stops right there: "
            "the rest of the recipe and the other target must not run."
        ),
        reference="Error handling with -k, -i, and -",
        hint=(
            "A recipe line that exits non-zero ends the whole make run, so the "
            "line after it and the goal's second prerequisite never happen. "
            "Your first target currently shrugs the failure off."
        ),
        makefile="""
all: first second

first:
\tfalse
\ttouch first.made

second:
\ttouch second.made
""",
        steps=[
            mk(
                exit_code=2,
                stdout="false",
                stderr="make: *** [Makefile:10: first] Error 1",
                missing=["first.made", "second.made"],
                description="the failure stops make before anything is written",
            ),
            mk(
                "second",
                files={"second.made": ""},
                description="the other target is still buildable on its own",
            ),
        ],
        breaks=[("\tfalse", "\t-false")],
    ),
    ex(
        topic=TOPIC,
        slug="11_dash_suppresses_the_error",
        title="A leading - tolerates one command's failure",
        objective=(
            "Prefix a failing command with - so make prints the error, carries "
            "on with the recipe, and still reports the run as a success."
        ),
        reference="Error handling with -k, -i, and -",
        hint=(
            "A - before the command tells make to ignore this one failure: the "
            "line is reported as (ignored), the recipe continues and make exits "
            "0. Add it to both failing lines."
        ),
        makefile="""
all:
\t-false
\techo "make carried on to the next line"
\t-false
\techo "and the whole run still succeeded"
""",
        steps=[
            mk(
                stdout="""false
make carried on to the next line
false
and the whole run still succeeded""",
                stderr="""make: [Makefile:8: all] Error 1 (ignored)
make: [Makefile:10: all] Error 1 (ignored)""",
                stderr_mode="ordered_lines",
                description="both failures are ignored and the run succeeds",
            ),
        ],
        breaks=[
            (
                '\t-false\n\techo "make carried on to the next line"',
                '\tfalse\n\techo "make carried on to the next line"',
            )
        ],
    ),
    ex(
        topic=TOPIC,
        slug="12_ignore_errors_flag",
        title="make -i ignores every error",
        objective=(
            "Compare a plain make, which stops at the failing line, with make "
            "-i, which ignores it and carries on."
        ),
        reference="Error handling with -k, -i, and -",
        hint=(
            "make -i is the command line version of a - on every line. The "
            "recipe needs a command that really fails: 'false' exits non-zero, "
            "while a command that merely prints the word false does not."
        ),
        makefile="""
all:
\t@echo "make flags: [$(MAKEFLAGS)]"
\tfalse
\t@echo "make carried on regardless"
""",
        steps=[
            mk(
                exit_code=2,
                stdout="make flags: []",
                stderr="make: *** [Makefile:9: all] Error 1",
                description="without -i the run dies at the failing line",
            ),
            mk(
                exit_code=2,
                stdout="make carried on regardless",
                stdout_mode="not_contains",
                description="so the last line of the recipe never runs",
            ),
            mk(
                "-i",
                stdout="""make flags: [i]
make carried on regardless""",
                stderr="make: [Makefile:9: all] Error 1 (ignored)",
                description="-i records the failure and keeps going",
            ),
        ],
        breaks=[("\tfalse", "\ttrue")],
    ),
    ex(
        topic=TOPIC,
        slug="13_keep_going_flag",
        title="make -k keeps going but still fails",
        objective=(
            "Build three targets where the first one fails, and tell make -k "
            "and make -i apart."
        ),
        reference="Error handling with -k, -i, and -",
        hint=(
            "-k continues with the goals that can still be built and then "
            "exits non-zero because the build was not completed; -i ignores the "
            "errors entirely and exits 0. Make the first target fail for real."
        ),
        makefile="""
all: first second third

first:
\tfalse

second:
\ttouch second.made

third:
\ttouch third.made
""",
        steps=[
            mk(
                exit_code=2,
                stderr="make: *** [Makefile:10: first] Error 1",
                missing=["second.made", "third.made"],
                description="a plain make never reaches the other two targets",
            ),
            mk(
                "-k",
                exit_code=2,
                stdout="""touch second.made
touch third.made""",
                stdout_mode="contains_lines",
                stderr="make: Target 'all' not remade because of errors.",
                files={"second.made": "", "third.made": ""},
                description="-k builds what it can, then reports the failure",
            ),
            mk(
                "-i",
                exit_code=0,
                stderr="make: [Makefile:10: first] Error 1 (ignored)",
                files={"second.made": "", "third.made": ""},
                description="-i ignores the failure and exits 0",
            ),
        ],
        breaks=[("\tfalse", "\techo false")],
    ),
    ex(
        topic=TOPIC,
        slug="14_half_built_target",
        title="A failed recipe leaves a half-built target",
        objective=(
            "Fail a recipe after it has written part of its output, and see "
            "that make keeps the partial file and treats it as finished."
        ),
        reference="Interrupting or killing make",
        hint=(
            "make never rolls a target back when a recipe fails, so report.txt "
            "is left with only the first write - and the next make finds the "
            "file and reports it up to date. The recipe has to fail between its "
            "two writes. (Interrupting make with ctrl-c is different: then make "
            "removes the targets it has just made.)"
        ),
        makefile="""
report.txt:
\t@echo "partial line" > report.txt
\t@false
\t@echo "complete report" > report.txt
""",
        steps=[
            mk(
                exit_code=2,
                stderr="make: *** [Makefile:9: report.txt] Error 1",
                files={"report.txt": "partial line"},
                description="the failed run leaves only the first write",
            ),
            mk(
                stdout="make: 'report.txt' is up to date.",
                description="the next make trusts the half-built file",
            ),
            step(
                "cat",
                "report.txt",
                stdout="partial line",
                description="and the truncated file is still what is on disk",
            ),
        ],
        breaks=[("\t@false", "\t@true")],
    ),
    ex(
        topic=TOPIC,
        slug="15_plan_with_dry_run",
        title="make -n prints the plan without running it",
        objective=(
            "Read every command a target would run with make -n, and check that "
            "the dry run really does not touch the filesystem."
        ),
        reference="Arguments to make",
        hint=(
            "make -n (or --dry-run) prints the whole recipe, including the "
            "lines hidden by @, and runs none of them. Note that the plan only "
            "contains the commands make would reach, so a missing prerequisite "
            "never shows up in it."
        ),
        makefile="""
all: report.txt
\t@cat report.txt

report.txt:
\t@echo "writing report" > report.txt
\t@echo "report written"
""",
        steps=[
            mk(
                "-n",
                stdout="""echo "writing report" > report.txt
echo "report written"
cat report.txt""",
                missing=["report.txt"],
                description="the plan lists every command, and creates nothing",
            ),
            mk(
                "-n",
                "report.txt",
                stdout=(
                    'echo "writing report" > report.txt\n'
                    'echo "report written"'
                ),
                missing=["report.txt"],
                description="a single target can be dry run on its own",
            ),
            mk(
                files={"report.txt": "writing report"},
                stdout="writing report",
                description="the real run finally writes the file",
            ),
        ],
        breaks=[("all: report.txt", "all:")],
    ),
    ex(
        topic=TOPIC,
        slug="16_recursive_make",
        title="Calling the Makefile in a subdirectory",
        objective=(
            "Have the top-level Makefile build the project in sub/ by asking "
            "$(MAKE) to read that directory's Makefile."
        ),
        reference="Recursive use of make",
        hint=(
            "A recipe line that runs $(MAKE) -C sub starts a second make in "
            "sub/; it announces itself with make[1]: Entering directory and "
            "bumps MAKELEVEL to 1. Add that line to the all recipe."
        ),
        makefile="""
all:
\t@echo "top level, MAKELEVEL=$(MAKELEVEL)"
\t$(MAKE) -C sub
""",
        steps=[
            mk(
                stdout="""top level, MAKELEVEL=0
make -C sub
make[1]: Entering directory '<stage>/sub'
sub make, MAKELEVEL=1
make[1]: Leaving directory '<stage>/sub'""",
                files={"sub/built.txt": ""},
                description="the second make runs in sub/ and does its work",
            ),
        ],
        breaks=[
            (
                '\t@echo "top level, MAKELEVEL=$(MAKELEVEL)"\n\t$(MAKE) -C sub',
                '\t@echo "top level, MAKELEVEL=$(MAKELEVEL)"',
            )
        ],
        files={
            "sub/Makefile": """
all:
\t@echo "sub make, MAKELEVEL=$(MAKELEVEL)"
\t@touch built.txt
""",
        },
    ),
    ex(
        topic=TOPIC,
        slug="17_dollar_make_not_bare_make",
        title="Use $(MAKE), never a bare make",
        objective=(
            "Show what breaks when a recipe calls make instead of $(MAKE): the "
            "second make loses the flags and make -n no longer descends."
        ),
        reference="Recursive use of make",
        hint=(
            "make only runs a recipe line itself (rather than merely printing "
            "it) under -n when the line mentions $(MAKE), and it hands its flags "
            "to the sub-make through MAKEFLAGS. Replace the bare make with "
            "$(MAKE)."
        ),
        makefile="""
all:
\t@echo "top level, MAKELEVEL=$(MAKELEVEL)"
\t@echo "top level flags: [$(MAKEFLAGS)]"
\t$(MAKE) -C sub
""",
        steps=[
            mk(
                "-n",
                stdout="""echo "top level, MAKELEVEL=0"
echo "top level flags: [n]"
make -C sub
make[1]: Entering directory '<stage>/sub'
echo "sub make, MAKELEVEL=1"
touch built.txt
make[1]: Leaving directory '<stage>/sub'""",
                missing=["sub/built.txt"],
                description="-n descends into the sub-make but builds nothing",
            ),
            mk(
                "-s",
                stdout="""top level, MAKELEVEL=0
sub make, MAKELEVEL=1""",
                description="-s reaches the sub-make too, so it stays quiet",
            ),
            mk(
                "-s",
                stdout="Entering directory",
                stdout_mode="not_contains",
                description="a silenced sub-make prints no directory lines",
            ),
            mk(
                stdout="sub make, MAKELEVEL=1",
                description="a normal run recurses as well",
            ),
        ],
        breaks=[("$(MAKE) -C sub", "make -C sub")],
        files={
            "sub/Makefile": """
all:
\t@echo "sub make, MAKELEVEL=$(MAKELEVEL)"
\t@touch built.txt
""",
        },
    ),
    ex(
        topic=TOPIC,
        slug="18_exported_variables",
        title="Only exported variables reach the shell",
        objective=(
            "Print a make variable and a shell variable side by side, and show "
            "that environment variables are make variables from the start."
        ),
        reference="Export, environments, and recursive make",
        hint=(
            "A variable defined in the Makefile lives only inside make until "
            "you export it, which is what puts it in the environment of every "
            "recipe line. Variables that were already in the environment arrive "
            "as make variables automatically."
        ),
        makefile="""
one = this will only work locally
export two = we can run subcommands with this

all:
\t@echo "make variable one: [$(one)]"
\t@echo "shell variable one: [$$one]"
\t@echo "make variable two: [$(two)]"
\t@echo "shell variable two: [$$two]"

from_environment:
\t@echo "make variable: [$(SHELL_ENV_VAR)]"
\t@echo "shell variable: [$$SHELL_ENV_VAR]"
""",
        steps=[
            mk(
                "all",
                stdout="""make variable one: [this will only work locally]
shell variable one: []
make variable two: [we can run subcommands with this]
shell variable two: [we can run subcommands with this]""",
                description="export decides which variable the shell can see",
            ),
            mk(
                "from_environment",
                env={"SHELL_ENV_VAR": "I am an environment variable"},
                stdout="""make variable: [I am an environment variable]
shell variable: [I am an environment variable]""",
                description="the environment is imported before the Makefile runs",
            ),
        ],
        breaks=[("export two = we can run subcommands with this", "two = we can run subcommands with this")],
    ),
    ex(
        topic=TOPIC,
        slug="19_unexport_and_export_all",
        title="A bare export, and unexport to undo it",
        objective=(
            "Export every variable at once with an argumentless export, then "
            "keep one of them out of the environment with unexport."
        ),
        reference="Export, environments, and recursive make",
        hint=(
            "'export' on its own line exports every variable, including the "
            "ones defined after it. A later 'unexport name' takes that variable "
            "back out of the environment, which is how you keep a secret out of "
            "your recipes."
        ),
        makefile="""
greeting = hello from the Makefile
loud = exported on purpose
hidden = keep me out of the environment

export loud
unexport loud

# a bare export turns on exporting for every variable
export
unexport hidden

all:
\t@echo "greeting make: [$(greeting)]"
\t@echo "greeting shell: [$$greeting]"
\t@echo "loud shell: [$$loud]"
\t@echo "hidden shell: [$$hidden]"
""",
        steps=[
            mk(
                stdout="""greeting make: [hello from the Makefile]
greeting shell: [hello from the Makefile]
loud shell: []
hidden shell: []""",
                description="the bare export reaches every variable, the "
                "unexport takes one back",
            ),
        ],
        breaks=[("export\nunexport hidden\n", "export\n")],
    ),
    ex(
        topic=TOPIC,
        slug="20_export_across_recursion",
        title="Exporting a variable to a sub-make",
        objective=(
            "Let the Makefile in sub/ see a variable that only the top-level "
            "Makefile defines, by exporting it before the recursive call."
        ),
        reference="Export, environments, and recursive make",
        hint=(
            "A sub-make is a child process: it only inherits what make put in "
            "the environment, so the top-level variable has to be exported for "
            "sub/Makefile to read it as $(cooly) or $$cooly. Add the export."
        ),
        makefile="""
cooly = The subdirectory can see me!
export cooly

all:
\t$(MAKE) -C sub
""",
        steps=[
            mk(
                stdout="""make -C sub
make[1]: Entering directory '<stage>/sub'
sub make variable: [The subdirectory can see me!]
sub shell variable: [The subdirectory can see me!]
make[1]: Leaving directory '<stage>/sub'""",
                description="the sub-make reads the exported variable",
            ),
            mk(
                "-C",
                "sub",
                stdout="""sub make variable: []
sub shell variable: []""",
                description="reading sub/Makefile directly has no such variable",
            ),
        ],
        breaks=[("export cooly\n", "")],
        files={
            "sub/Makefile": """
all:
\t@echo "sub make variable: [$(cooly)]"
\t@echo "sub shell variable: [$$cooly]"
""",
        },
    ),
    ex(
        topic=TOPIC,
        slug="21_command_line_variables",
        title="Variables on the command line, and several goals",
        objective=(
            "Give MODE a default in the Makefile, override it with make "
            "MODE=..., and ask for several goals in one run."
        ),
        reference="Arguments to make",
        hint=(
            "A value written on the command line wins over the Makefile's own "
            "assignment and is passed into the environment of every recipe. "
            "Several goals on one command line are run left to right."
        ),
        makefile="""
MODE = debug

all:
\t@echo "mode: $(MODE)"
\t@echo "mode in the shell: [$$MODE]"

clean:
\t@echo "cleaning"

run:
\t@echo "running"

test:
\t@echo "testing"
""",
        steps=[
            mk(
                stdout="""mode: debug
mode in the shell: []""",
                description="the Makefile's own value is used by default",
            ),
            mk(
                "MODE=release",
                stdout="""mode: release
mode in the shell: [release]""",
                description="the command line wins, and the shell sees it too",
            ),
            mk(
                "clean",
                "run",
                "test",
                stdout="""cleaning
running
testing""",
                description="several goals run in the order they were given",
            ),
            mk(
                "MODE=release",
                "run",
                stdout="running",
                description="a goal and a variable can be mixed freely",
            ),
        ],
        breaks=[("MODE = debug\n\n", "")],
    ),
    ex(
        topic=TOPIC,
        slug="22_directory_flag",
        title="Running make somewhere else: -C",
        objective=(
            "Run the Makefile in sub/ from the top of the tree with -C, keep "
            "the directory chatter down with --no-print-directory, and rebuild "
            "an up-to-date target with -B."
        ),
        reference="Arguments to make",
        hint=(
            "make -C sub changes directory before reading the Makefile, so it "
            "prints Entering/Leaving directory lines; --no-print-directory "
            "removes them. -B throws away make's timestamps and runs the recipe "
            "even when out.txt is up to date."
        ),
        makefile="""
out.txt: source.txt
\t@cp source.txt out.txt
\t@echo "copied source.txt"
""",
        steps=[
            mk(
                files={"out.txt": "hello"},
                stdout="copied source.txt",
                description="the first run copies the source",
            ),
            mk(
                stdout="make: 'out.txt' is up to date.",
                description="the second run has nothing to do",
            ),
            mk(
                "-B",
                stdout="copied source.txt",
                description="-B rebuilds it anyway",
            ),
            mk(
                "-C",
                "sub",
                "all",
                stdout="""make: Entering directory '<stage>/sub'
inside sub
make: Leaving directory '<stage>/sub'""",
                description="make -C names the directory it is entering",
            ),
            mk(
                "-C",
                "sub",
                "all",
                "--no-print-directory",
                stdout="inside sub",
                description="--no-print-directory drops those lines",
            ),
            mk(
                "-C",
                "sub",
                "all",
                "--no-print-directory",
                stdout="Entering directory",
                stdout_mode="not_contains",
                description="and nothing is printed about the directory",
            ),
        ],
        breaks=[],
        files={
            "source.txt": "hello\n",
            "sub/Makefile": """
all:
\t@echo "inside sub"
""",
        },
        file_breaks=[("sub/Makefile", "all:", "build:")],
    ),
]
