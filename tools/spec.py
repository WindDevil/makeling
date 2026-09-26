"""Shared data structures for the makeling exercise generator.

Each exercise is described once, here.  The generator turns a spec into three
trees of files:

* ``solutions/``  the correct Makefile and its supporting files
* ``exercises/``  the same thing with the spec's ``breaks`` applied
* ``templates/``  a byte-identical copy of ``exercises/``, used by ``reset``

The third file every exercise directory carries is ``checks.json``.  It is the
machine-readable contract for the exercise: a list of steps, each one a command
to run plus what the result must look like.  The runner (``./makeling``) is
nothing more than an interpreter for that file.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# How a step's captured output is compared with the expectation.
#
#   exact          the whole output must match
#   contains       the output must contain the given text
#   contains_lines every line of the expectation must appear, in any order
#   ordered_lines  every line must appear, in the given order
#   regex          the expectation is a regular expression searched in the output
#   not_contains   the output must not contain the given text
MATCH_MODES = (
    "exact",
    "contains",
    "contains_lines",
    "ordered_lines",
    "regex",
    "not_contains",
)


@dataclass(frozen=True)
class Step:
    """One command to run in the exercise directory, and what it must produce.

    ``args`` is a complete argv, so a step can invoke ``make`` with any flags,
    run ``./script.sh``, or call a tool that ``make`` itself is expected to
    have produced.  ``argv[0]`` is resolved on ``PATH``.
    """

    args: list[str]
    description: str = ""
    exit_code: int = 0
    stdout: str | None = None
    stdout_mode: str = "contains_lines"
    stderr: str | None = None
    stderr_mode: str = "contains"
    env: dict[str, str] = field(default_factory=dict)
    #: Files that must exist after the step, with exactly this content.
    files: dict[str, str] = field(default_factory=dict)
    #: Paths that must not exist after the step.
    missing: list[str] = field(default_factory=list)

    def to_json(self) -> dict[str, object]:
        return {
            "args": list(self.args),
            "description": self.description,
            "exit_code": self.exit_code,
            "stdout": self.stdout,
            "stdout_mode": self.stdout_mode,
            "stderr": self.stderr,
            "stderr_mode": self.stderr_mode,
            "env": dict(self.env),
            "files": dict(self.files),
            "missing": list(self.missing),
        }


@dataclass(frozen=True)
class ExerciseSpec:
    topic: str
    slug: str
    title: str
    objective: str
    reference: str
    hint: str
    #: The correct Makefile, as it ends up in ``solutions/``.
    makefile: str
    steps: list[Step]
    #: ``(correct, learner)`` replacements that turn the Makefile into the
    #: exercise.  At least one is required: an exercise that already passes
    #: would make ``selftest`` fail.
    breaks: list[tuple[str, str]] = field(default_factory=list)
    #: Extra files copied next to the Makefile, keyed by relative path.
    files: dict[str, str] = field(default_factory=dict)
    #: ``(filename, correct, learner)`` replacements applied to ``files``.
    file_breaks: list[tuple[str, str, str]] = field(default_factory=list)

    @property
    def ident(self) -> str:
        return f"{self.topic}/{self.slug}"


def ex(
    topic: str,
    slug: str,
    title: str,
    objective: str,
    reference: str,
    hint: str,
    makefile: str,
    steps: list[Step],
    breaks: list[tuple[str, str]],
    files: dict[str, str] | None = None,
    file_breaks: list[tuple[str, str, str]] | None = None,
) -> ExerciseSpec:
    """Describe one exercise.

    ``makefile`` and every entry in ``files`` are stripped of leading and
    trailing blank lines and end with exactly one newline, so specs can use
    triple-quoted strings without worrying about the surrounding whitespace.
    Recipe lines inside ``makefile`` must be indented with a real tab.
    """
    return ExerciseSpec(
        topic=topic,
        slug=slug,
        title=title,
        objective=objective,
        reference=reference,
        hint=hint,
        makefile=clean(makefile),
        steps=steps,
        breaks=breaks,
        files={name: clean(content) for name, content in (files or {}).items()},
        file_breaks=file_breaks or [],
    )


def mk(*args: str, **kwargs: object) -> Step:
    """A step that runs ``make`` with the given arguments."""
    return step("make", *args, **kwargs)


def step(cmd: str, *args: str, **kwargs: object) -> Step:
    """A step that runs ``cmd`` with the given arguments.

    Keyword arguments map onto :class:`Step` fields.  ``stdout`` (or
    ``stderr``) may be passed together with the matching ``*_mode``; passing
    ``stdout`` alone means "these lines must all appear, in this order".
    """
    if "stdout" in kwargs and "stdout_mode" not in kwargs:
        kwargs["stdout_mode"] = "ordered_lines"
    return Step(args=[cmd, *args], **kwargs)  # type: ignore[arg-type]


def clean(text: str) -> str:
    """Normalise a spec string: no surrounding blank lines, one final newline."""
    return text.strip("\n") + "\n"


def checks_document(spec: ExerciseSpec) -> dict[str, object]:
    """The contents of ``checks.json`` for an exercise."""
    return {
        "exercise": spec.ident,
        "title": spec.title,
        "objective": spec.objective,
        "reference": spec.reference,
        "hint": spec.hint,
        "steps": [s.to_json() for s in spec.steps],
    }
