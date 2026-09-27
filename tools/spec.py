"""Shared data structures for the makefiling exercise generator.

Each exercise is described once, here.  The generator turns a spec into three
trees of files:

* ``solutions/``  the correct Makefile and its supporting files
* ``exercises/``  the same thing with the spec's ``breaks`` applied
* ``templates/``  a byte-identical copy of ``exercises/``, used by ``reset``

The third file every exercise directory carries is ``checks.json``.  It is the
machine-readable contract for the exercise: a list of steps, each one a command
to run plus what the result must look like.  The runner (``./makefiling``) is
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


# A short, model-first route for absolute beginners.  The complete catalogue
# remains available, but these lessons make the first twenty exercises feel
# like one story: predict the dependency graph, run make, then explain why it
# did (or did not) run a recipe.
BASIC_LESSONS: dict[str, dict[str, object]] = {
    "00_getting_started/01_first_rule": {
        "order": 1,
        "goal": "让 make 执行一条最简单的 recipe。",
        "prediction": "运行 make 会读取哪个目标？终端会先显示命令，还是只显示命令的输出？",
        "hints": [
            "规则由目标行和 recipe 组成：hello: 下一行才是要执行的命令。",
            "recipe 行必须以真正的 TAB 开头。",
            "把 echo 命令放在 hello: 下方，并用 TAB 缩进。",
        ],
        "explanation": "make 默认构建第一个目标；recipe 会先被回显，再交给 shell 执行。",
    },
    "00_getting_started/02_default_goal": {
        "order": 2,
        "goal": "理解默认目标和显式目标的区别。",
        "prediction": "裸 make 和 make goodbye 会分别选择哪条规则？",
        "hints": [
            "没有命令行目标时，make 选择读到的第一个目标。",
            "移动整条规则时，目标名和它的 recipe 要一起移动。",
            "让 hello 规则出现在 goodbye 之前。",
        ],
        "explanation": "裸 make 只构建第一个目标；显式写出 goodbye 才会选择 goodbye。",
    },
    "00_getting_started/03_essence_target_file": {
        "order": 3,
        "goal": "观察目标名如何对应磁盘上的文件。",
        "prediction": "第一次 make 后，第二次 make 为什么不再执行 echo？",
        "hints": [
            "make 通过文件系统判断 hello 是否已经存在。",
            "recipe 必须真的创建名为 hello 的文件。",
            "把 echo 的输出重定向到 hello。",
        ],
        "explanation": "目标文件存在且没有更晚的前置条件时，make 认为目标已经最新。",
    },
    "00_getting_started/04_essence_prerequisites": {
        "order": 4,
        "goal": "用前置条件表达“源文件变化后需要重建”。",
        "prediction": "只修改 blah.c 后，make 会不会再次执行 cc？",
        "hints": [
            "在目标名后面的冒号右侧列出它依赖的文件。",
            "blah 应该依赖 blah.c。",
            "make 比较目标和前置条件的修改时间。",
        ],
        "explanation": "目标不存在，或任一前置条件比目标更新时，make 才执行 recipe。",
    },
    "00_getting_started/05_which_makefile": {
        "order": 5,
        "goal": "知道 make 如何选择 Makefile。",
        "prediction": "目录中同时存在 GNUmakefile 和 Makefile 时，裸 make 读取谁？",
        "hints": [
            "GNU Make 有固定的文件名搜索顺序。",
            "make -f 文件名可以跳过默认搜索。",
            "让两个文件输出不同文本，再用三条检查命令比较。",
        ],
        "explanation": "GNUmakefile 的优先级高于 makefile 和 Makefile；-f 可以显式指定。",
    },
    "00_getting_started/06_beyond_compilation": {
        "order": 6,
        "goal": "把 make 看成依赖图执行器，而不只是编译器包装器。",
        "prediction": "make report 时，summary.txt 和 report 的顺序是什么？",
        "hints": [
            "report 的 recipe 会读取 summary.txt，所以 report 应依赖它。",
            "summary.txt 又依赖 names.txt。",
            "把依赖关系写在冒号右侧，recipe 只负责动作。",
        ],
        "explanation": "make 先递归构建前置条件，再执行目标 recipe；任何命令都可以成为 recipe。",
    },
    "01_syntax_and_essence/01_rule_anatomy": {
        "order": 7,
        "goal": "拆开一条规则的目标、前置条件和 recipe。",
        "prediction": "make report.txt 会先检查 notes.txt，还是直接运行两条命令？",
        "hints": [
            "规则头的形式是 target: prerequisites。",
            "两条 recipe 可以连续写在同一个目标下面。",
            "第二条命令也必须以 TAB 开头。",
        ],
        "explanation": "目标行描述依赖关系，缩进的每一行才属于 recipe。",
    },
    "01_syntax_and_essence/02_several_targets_one_rule": {
        "order": 8,
        "goal": "让一条规则服务多个目标名。",
        "prediction": "分别请求两个目标时，make 是否都能执行同一条 recipe？",
        "hints": [
            "多个目标可以写在同一个冒号左侧。",
            "目标名之间用空格分隔。",
            "不要把第二个目标写成前置条件。",
        ],
        "explanation": "同一规则可以为多个目标提供相同的 recipe；目标列表仍在冒号左侧。",
    },
    "01_syntax_and_essence/03_prerequisite_order": {
        "order": 9,
        "goal": "观察 make 按依赖顺序遍历图。",
        "prediction": "all: one two three 时，三个 recipe 的输出顺序是什么？",
        "hints": [
            "all 的前置条件就是构建顺序的入口。",
            "把 one、two、three 按期望顺序写在冒号右侧。",
            "recipe 的输出顺序能帮助你验证依赖图。",
        ],
        "explanation": "make 会先处理前置条件，再回到目标；同层前置条件按书写顺序访问。",
    },
    "01_syntax_and_essence/04_recipe_creates_the_target": {
        "order": 10,
        "goal": "让 recipe 创建它声明的目标文件。",
        "prediction": "如果 recipe 创建 hello，第二次 make 会发生什么？",
        "hints": [
            "目标是否最新取决于同名文件是否存在。",
            "把两行文本写入 hello，而不是只打印到终端。",
            "可以用 echo 和 >、>> 组合写文件。",
        ],
        "explanation": "recipe 的副作用必须和目标名一致，否则 make 每次都只能再次尝试。",
    },
    "01_syntax_and_essence/05_timestamps_decide": {
        "order": 11,
        "goal": "用时间戳理解增量构建。",
        "prediction": "源文件比目标旧时会重建吗？源文件更新后呢？",
        "hints": [
            "目标需要一个源文件作为前置条件。",
            "make 只关心修改时间的先后，不理解文件内容。",
            "先确保 blah.c 更旧，再让它变新观察两次结果。",
        ],
        "explanation": "Make 的默认增量策略是：目标缺失或任一依赖更新，就重建目标。",
    },
    "01_syntax_and_essence/06_every_prerequisite_counts": {
        "order": 12,
        "goal": "理解多个前置条件中的任意一个都能触发重建。",
        "prediction": "只更新 a.txt 或只更新 b.txt，combined.txt 是否都会重建？",
        "hints": [
            "所有依赖都写在同一个目标行的冒号右侧。",
            "缺少 b.txt 时，make 不会知道它参与了生成。",
            "recipe 可以继续按需要读取两个文件。",
        ],
        "explanation": "目标必须比所有前置条件都新；任何一个依赖变新都会使目标过期。",
    },
    "02_quick_examples/01_three_step_chain": {
        "order": 13,
        "goal": "构建一个三层依赖链。",
        "prediction": "从空目录构建 blah 时，blah.c、blah.o、blah 的顺序是什么？",
        "hints": [
            "最终目标 blah 依赖 blah.o，blah.o 依赖 blah.c。",
            "每一层都需要一条规则。",
            "从最终目标向下画箭头，再按反方向执行。",
        ],
        "explanation": "Make 递归走完整条依赖链，再从最底层开始执行 recipe。",
    },
    "02_quick_examples/03_touching_an_intermediate_file": {
        "order": 14,
        "goal": "观察只重建受影响的链段。",
        "prediction": "只更新 blah.o 时，blah.c 会重新编译吗？",
        "hints": [
            "blah.o 必须声明 blah.c 依赖。",
            "最终目标 blah 依赖 blah.o。",
            "比较每次输出，找出没有重新执行的 recipe。",
        ],
        "explanation": "增量构建只执行从过期节点到最终目标所需的那部分 recipe。",
    },
    "02_quick_examples/08_clean_can_run_twice": {
        "order": 15,
        "goal": "用 clean 把构建产物恢复到可重建状态。",
        "prediction": "clean 运行两次时，第二次应该失败还是成功？",
        "hints": [
            "clean 通常不产生名为 clean 的文件。",
            "rm -f 在文件不存在时也保持成功。",
            "clean 是动作目标，不是构建产物。",
        ],
        "explanation": "clean 负责删除产物；幂等的清理命令可以安全重复执行。",
    },
    "02_quick_examples/10_build_clean_build": {
        "order": 16,
        "goal": "完整体验 build → clean → build。",
        "prediction": "清理后再次构建，哪些 recipe 会重新执行？",
        "hints": [
            "clean 必须删除这组练习创建的所有产物。",
            "先构建一次，再清理，再观察第三次。",
            "如果有文件残留，make 会把它当作已有目标。",
        ],
        "explanation": "clean 删除目标后，下一次 make 会重新走完整依赖链。",
    },
    "03_variables/01_a_list_in_a_variable": {
        "order": 17,
        "goal": "用变量给同一组文件命名。",
        "prediction": "$(files) 出现在目标行和 recipe 中时，make 会如何展开？",
        "hints": [
            "变量定义形如 files := file1 file2。",
            "some_file 应把 files 放在冒号右侧。",
            "recipe 中也可以直接写 $(files)。",
        ],
        "explanation": "变量先展开成文本；在依赖列表中，它会成为多个文件名。",
    },
    "03_variables/09_the_four_common_automatic_variables": {
        "order": 18,
        "goal": "认识 recipe 中最常用的自动变量。",
        "prediction": "$@、$<、$^、$? 分别代表什么？",
        "hints": [
            "$@ 是当前目标，$< 是第一个前置条件。",
            "$^ 是全部前置条件，$? 是比目标更新的那些。",
            "自动变量只在 recipe 执行时有意义。",
        ],
        "explanation": "自动变量由 make 根据当前规则上下文填充，不需要手工定义。",
    },
    "04_targets/03_phony_clean": {
        "order": 19,
        "goal": "理解 .PHONY 如何声明动作目标。",
        "prediction": "目录里已经有一个叫 clean 的文件时，make clean 会删除产物吗？",
        "hints": [
            "make 默认把目标名当作可能存在的文件。",
            ".PHONY: clean 告诉 make clean 永远不是文件。",
            "把 .PHONY 声明放在 clean 规则前后都可以。",
        ],
        "explanation": ".PHONY 目标不参与文件时间戳判断，每次被请求都会执行。",
    },
    "04_targets/04_all_builds_everything": {
        "order": 20,
        "goal": "用 all 作为一个聚合目标。",
        "prediction": "裸 make 时，all 的三个前置条件会不会全部构建？",
        "hints": [
            "all 是普通目标，只是约定俗成的总入口。",
            "把 one、two、three 都列为 all 的前置条件。",
            "让 all 成为文件中的第一个目标。",
        ],
        "explanation": "all 本身可以没有 recipe；它通过前置条件聚合多个独立目标。",
    },
}


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
    document = {
        "exercise": spec.ident,
        "title": spec.title,
        "objective": spec.objective,
        "reference": spec.reference,
        "hint": spec.hint,
        "steps": [s.to_json() for s in spec.steps],
    }
    lesson = BASIC_LESSONS.get(spec.ident)
    if lesson:
        document["lesson"] = lesson
    return document
