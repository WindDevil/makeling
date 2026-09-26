#!/usr/bin/env python3
"""Generate makeling exercises, solutions, templates, and documentation.

The generated files are checked into the repository.  Keeping the generator
around makes it easy to add an exercise consistently:

    python3 tools/generate_exercises.py

Every exercise spec carries the correct Makefile.  The learner's copy is made
by applying the spec's ``breaks`` replacements, which guarantees that the
exercise and the solution can never drift apart.  ``./makeling selftest``
enforces the matching invariant: an exercise must fail before it is solved and
its solution must pass.

Generated paths:

    exercises/<topic>/<slug>/Makefile + files + checks.json
    templates/<topic>/<slug>/...        (identical to exercises/)
    solutions/<topic>/<slug>/...        (the correct files)
    exercises/<topic>/README.md
    docs/curriculum.md
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from pathlib import Path

from spec import MATCH_MODES, ExerciseSpec, checks_document

ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = ROOT / "tools"
EXERCISES_DIR = ROOT / "exercises"
SOLUTIONS_DIR = ROOT / "solutions"
TEMPLATES_DIR = ROOT / "templates"

SITE = "https://makefiletutorial.com/"

# One entry per topic, in curriculum order.  ``sections`` lists the tutorial
# headings the topic covers, with the anchor used on makefiletutorial.com.
TOPICS: list[dict[str, object]] = [
    {
        "topic": "00_getting_started",
        "title": "Getting Started",
        "intro": (
            "Why Makefiles exist, what people use instead, which flavour of "
            "make you are running, and how an example is actually executed."
        ),
        "sections": [
            ("Why do Makefiles exist?", "why-do-makefiles-exist"),
            ("What alternatives are there to Make?", "what-alternatives-are-there-to-make"),
            ("The versions and types of Make", "the-versions-and-types-of-make"),
            ("Running the Examples", "running-the-examples"),
        ],
    },
    {
        "topic": "01_syntax_and_essence",
        "title": "Makefile Syntax and the Essence of Make",
        "intro": (
            "The shape of a rule, the role of targets, prerequisites and "
            "recipes, and the file-existence rule that decides whether a "
            "recipe runs at all."
        ),
        "sections": [
            ("Makefile Syntax", "makefile-syntax"),
            ("The essence of Make", "the-essence-of-make"),
        ],
    },
    {
        "topic": "02_quick_examples",
        "title": "More Quick Examples",
        "intro": (
            "A first end-to-end build: several targets, real prerequisites "
            "between them, and a ``clean`` target to undo the work."
        ),
        "sections": [
            ("More quick examples", "more-quick-examples"),
            ("Make clean", "make-clean"),
        ],
    },
    {
        "topic": "03_variables",
        "title": "Variables",
        "intro": (
            "Assigning to variables, expanding them in targets and recipes, "
            "the quoting rules that surprise everyone, and the automatic "
            "variables every Makefile ends up using."
        ),
        "sections": [
            ("Variables", "variables"),
            ("Automatic Variables", "automatic-variables"),
        ],
    },
    {
        "topic": "04_targets",
        "title": "Targets",
        "intro": (
            "Targets as file names, the conventional ``all`` target, and "
            "rules that build more than one file at a time."
        ),
        "sections": [
            ("Targets", "targets"),
            ("The all target", "the-all-target"),
            ("Multiple targets", "multiple-targets"),
        ],
    },
    {
        "topic": "05_wildcards_and_automatic_variables",
        "title": "Automatic Variables and Wildcards",
        "intro": (
            "The ``*`` and ``%`` wildcards, when each one is expanded, and "
            "the full set of automatic variables available inside a recipe."
        ),
        "sections": [
            ("* Wildcard", "-wildcard"),
            ("% Wildcard", "-wildcard-1"),
            ("Automatic Variables", "automatic-variables"),
        ],
    },
    {
        "topic": "06_fancy_rules",
        "title": "Fancy Rules",
        "intro": (
            "Implicit rules, static pattern rules, pattern rules, and "
            "double-colon rules: the four ways to say ``build things that "
            "look like this''."
        ),
        "sections": [
            ("Implicit Rules", "implicit-rules"),
            ("Static Pattern Rules", "static-pattern-rules"),
            ("Static Pattern Rules and Filter", "static-pattern-rules-and-filter"),
            ("Pattern Rules", "pattern-rules"),
            ("Double-Colon Rules", "double-colon-rules"),
        ],
    },
    {
        "topic": "07_commands_and_execution",
        "title": "Commands and Execution",
        "intro": (
            "How make prints and runs recipes: echoing and silencing, the "
            "shell it uses, ``$$``, error handling, interrupts, recursive "
            "make, exported environments, and the command line."
        ),
        "sections": [
            ("Command Echoing/Silencing", "command-echoingsilencing"),
            ("Command Execution", "command-execution"),
            ("Default Shell", "default-shell"),
            ("Double dollar sign", "double-dollar-sign"),
            ("Error handling with -k, -i, and -", "error-handling-with--k--i-and--"),
            ("Interrupting or killing make", "interrupting-or-killing-make"),
            ("Recursive use of make", "recursive-use-of-make"),
            ("Export, environments, and recursive make", "export-environments-and-recursive-make"),
            ("Arguments to make", "arguments-to-make"),
        ],
    },
    {
        "topic": "08_variables_pt2",
        "title": "Variables Pt. 2",
        "intro": (
            "Recursive versus simply expanded variables, overriding from the "
            "command line, ``define``, and variables scoped to a target or a "
            "pattern."
        ),
        "sections": [
            ("Flavors and modification", "flavors-and-modification"),
            ("Command line arguments and override", "command-line-arguments-and-override"),
            ("List of commands and define", "list-of-commands-and-define"),
            ("Target-specific variables", "target-specific-variables"),
            ("Pattern-specific variables", "pattern-specific-variables"),
        ],
    },
    {
        "topic": "09_conditionals",
        "title": "Conditional Part of Makefiles",
        "intro": (
            "Choosing what a Makefile contains at parse time: ``ifeq`` and "
            "friends, testing for empty and undefined variables, and reading "
            "``$(MAKEFLAGS)``."
        ),
        "sections": [
            ("Conditional if/else", "conditional-ifelse"),
            ("Check if a variable is empty", "check-if-a-variable-is-empty"),
            ("Check if a variable is defined", "check-if-a-variable-is-defined"),
            ("$(MAKEFLAGS)", "makeflags"),
        ],
    },
    {
        "topic": "10_functions",
        "title": "Functions",
        "intro": (
            "Text functions: substitution references, ``$(subst)``, "
            "``$(foreach)``, ``$(if)``, ``$(call)``, ``$(shell)``, "
            "``$(filter)`` and the rest of the family."
        ),
        "sections": [
            ("First Functions", "first-functions"),
            ("String Substitution", "string-substitution"),
            ("The foreach function", "the-foreach-function"),
            ("The if function", "the-if-function"),
            ("The call function", "the-call-function"),
            ("The shell function", "the-shell-function"),
            ("The filter function", "the-filter-function"),
        ],
    },
    {
        "topic": "11_other_features",
        "title": "Other Features",
        "intro": (
            "The directives and special targets that finish a real Makefile: "
            "``include``, ``vpath``, multiline definitions, ``.PHONY`` and "
            "``.DELETE_ON_ERROR``."
        ),
        "sections": [
            ("Include Makefiles", "include-makefiles"),
            ("The vpath Directive", "the-vpath-directive"),
            ("Multiline", "multiline"),
            (".phony", "phony"),
            (".delete_on_error", "delete_on_error"),
        ],
    },
    {
        "topic": "12_cookbook",
        "title": "Makefile Cookbook",
        "intro": (
            "The full project Makefile from the end of the tutorial: source "
            "discovery, out-of-tree objects, generated header dependencies, "
            "and both C and C++ compilation."
        ),
        "sections": [
            ("Makefile Cookbook", "makefile-cookbook"),
        ],
    },
]

TOPIC_BY_NAME = {entry["topic"]: entry for entry in TOPICS}


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


def header(spec: ExerciseSpec, comment: str = "#") -> str:
    lines = [
        f"{comment} makeling exercise: {spec.ident}",
        f"{comment} title: {spec.title}",
        f"{comment} objective: {spec.objective}",
        f"{comment} reference: {spec.reference}",
        f"{comment} hint: {spec.hint}",
    ]
    return "\n".join(lines) + "\n"


def broken_text(spec: ExerciseSpec) -> str:
    text = spec.makefile
    for correct, learner in spec.breaks:
        if correct not in text:
            raise SystemExit(
                f"{spec.ident}: break pattern not found in the Makefile:\n{correct}"
            )
        text = text.replace(correct, learner, 1)
    return text


def broken_file(spec: ExerciseSpec, name: str, content: str) -> str:
    for target, correct, learner in spec.file_breaks:
        if target != name:
            continue
        if correct not in content:
            raise SystemExit(
                f"{spec.ident}/{name}: break pattern not found:\n{correct}"
            )
        content = content.replace(correct, learner, 1)
    return content


def topic_readme(specs: list[ExerciseSpec], entry: dict[str, object]) -> str:
    topic = entry["topic"]
    lines = [
        f"# {entry['title']}",
        "",
        f"[makefiletutorial.com]({SITE}#{entry['sections'][0][1]})",
        "",
        str(entry["intro"]),
        "",
        "Run an exercise with:",
        "",
        "```sh",
        f"./makeling run {topic}/{specs[0].slug}",
        "```",
        "",
        "| Exercise | Objective | Tutorial section |",
        "| --- | --- | --- |",
    ]
    for spec in specs:
        lines.append(f"| `{spec.slug}` | {spec.objective} | {spec.reference} |")
    lines.extend(["", "Tutorial sections covered:", ""])
    for name, anchor in entry["sections"]:
        lines.append(f"- [{name}]({SITE}#{anchor})")
    lines.append("")
    return "\n".join(lines)


def curriculum(specs: list[ExerciseSpec]) -> str:
    by_topic: dict[str, list[ExerciseSpec]] = {}
    for spec in specs:
        by_topic.setdefault(spec.topic, []).append(spec)

    lines = [
        "# Curriculum: makefiletutorial.com, section by section",
        "",
        "This map turns every section of "
        "[makefiletutorial.com](https://makefiletutorial.com/) into runnable",
        "exercises.  Each exercise names the tutorial section it drills in its",
        "`reference` field, so the two can be read side by side.",
        "",
        f"Total exercises: **{len(specs)}** across **{len(by_topic)}** topics.",
        "",
    ]
    for entry in TOPICS:
        topic = str(entry["topic"])
        topic_specs = by_topic.get(topic, [])
        if not topic_specs:
            continue
        lines.extend(
            [
                f"## {entry['title']} (`{topic}`)",
                "",
                f"Tutorial sections: {SITE}#{entry['sections'][0][1]}",
                "",
                "| Exercise | Objective | Tutorial section |",
                "| --- | --- | --- |",
            ]
        )
        for spec in topic_specs:
            lines.append(f"| `{spec.ident}` | {spec.objective} | {spec.reference} |")
        lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Loading and validation
# --------------------------------------------------------------------------


def load_specs(topic: str | None = None) -> list[ExerciseSpec]:
    """Load every spec module, or just one topic's.

    Filtering by filename before importing matters: ``--topic`` is used while
    several people (or agents) are writing different spec files at the same
    time, and a half-written sibling file must not break the import.
    """
    if str(TOOLS_DIR) not in sys.path:
        sys.path.insert(0, str(TOOLS_DIR))

    specs: list[ExerciseSpec] = []
    for path in sorted(TOOLS_DIR.glob("specs_*.py")):
        if topic is not None and path.stem != f"specs_{topic}":
            continue
        module = importlib.import_module(path.stem)
        found = getattr(module, "SPECS", None)
        if found is None:
            raise SystemExit(f"{path.name}: no SPECS list")
        specs.extend(found)

    seen: set[str] = set()
    for spec in specs:
        if spec.ident in seen:
            raise SystemExit(f"duplicate exercise id: {spec.ident}")
        seen.add(spec.ident)
        validate(spec)

    specs.sort(key=lambda spec: (spec.topic, spec.slug))
    return specs


def validate(spec: ExerciseSpec) -> None:
    if spec.topic not in TOPIC_BY_NAME:
        raise SystemExit(f"{spec.ident}: unknown topic {spec.topic!r}")
    if not spec.breaks and not spec.file_breaks:
        raise SystemExit(f"{spec.ident}: needs at least one break")
    if not spec.steps:
        raise SystemExit(f"{spec.ident}: needs at least one check step")
    for correct, learner in spec.breaks:
        if correct not in spec.makefile:
            raise SystemExit(f"{spec.ident}: break not found in Makefile:\n{correct}")
        if correct == learner:
            raise SystemExit(f"{spec.ident}: break is a no-op:\n{correct}")
    for name, correct, _learner in spec.file_breaks:
        if name not in spec.files:
            raise SystemExit(f"{spec.ident}: file_break targets unknown file {name}")
        if correct not in spec.files[name]:
            raise SystemExit(f"{spec.ident}/{name}: break not found:\n{correct}")
    for index, step in enumerate(spec.steps):
        for mode in (step.stdout_mode, step.stderr_mode):
            if mode not in MATCH_MODES:
                raise SystemExit(f"{spec.ident}: step {index}: bad match mode {mode!r}")
        if step.stdout is not None and step.stdout_mode == "exact" and not step.stdout.strip():
            raise SystemExit(f"{spec.ident}: step {index}: empty exact stdout")
        if not step.args or not step.args[0]:
            raise SystemExit(f"{spec.ident}: step {index}: empty argv")


# --------------------------------------------------------------------------
# Emitting
# --------------------------------------------------------------------------


def emit(spec: ExerciseSpec) -> dict[Path, str]:
    """Every file the given spec is responsible for."""
    out: dict[Path, str] = {}
    document = json.dumps(checks_document(spec), indent=2, ensure_ascii=False) + "\n"

    for root, learner in (
        (EXERCISES_DIR, True),
        (TEMPLATES_DIR, True),
        (SOLUTIONS_DIR, False),
    ):
        base = root / spec.topic / spec.slug
        makefile = broken_text(spec) if learner else spec.makefile
        out[base / "Makefile"] = header(spec) + "\n" + makefile
        out[base / "checks.json"] = document
        for name, content in spec.files.items():
            out[base / name] = (
                broken_file(spec, name, content) if learner else content
            )
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true",
                        help="fail if the generated files are stale")
    parser.add_argument("--topic", help="only regenerate one topic")
    args = parser.parse_args(argv)

    specs = load_specs(args.topic)
    if args.topic:
        specs = [spec for spec in specs if spec.topic == args.topic]
        if not specs:
            print(f"no exercises for topic {args.topic}")
            return 1

    generated: dict[Path, str] = {}
    for spec in specs:
        generated.update(emit(spec))

    by_topic: dict[str, list[ExerciseSpec]] = {}
    for spec in specs:
        by_topic.setdefault(spec.topic, []).append(spec)
    for topic, topic_specs in by_topic.items():
        generated[EXERCISES_DIR / topic / "README.md"] = topic_readme(
            topic_specs, TOPIC_BY_NAME[topic]
        )

    if not args.topic:
        generated[ROOT / "docs" / "curriculum.md"] = curriculum(load_specs())

    if args.check:
        stale = [
            path
            for path, content in generated.items()
            if not path.exists() or path.read_text(encoding="utf-8") != content
        ]
        if stale:
            for path in stale:
                print(f"stale: {path.relative_to(ROOT)}")
            return 1
        print(f"{len(generated)} generated files are up to date")
        return 0

    for path, content in generated.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"generated {len(specs)} exercises ({len(generated)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
