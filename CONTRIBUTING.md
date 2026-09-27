# Contributing

感谢你愿意改进 `makefiling`。这个项目的核心原则是：

1. 练习必须能用系统自带的 `make` 独立运行，不依赖第三方工具。
2. 初始状态必须失败；参考答案必须通过。
3. 每个练习只聚焦一个概念，但可以把相关细节讲透。
4. 提示应当引导思考，而不是直接给出答案。
5. 每个练习都要标注它对应的 makefiletutorial.com 小节。
6. 练习与参考答案由生成器保持同步，不要手工编辑生成的文件。

## 添加一个练习

1. 找到对应的专题规格文件 `tools/specs_<topic>.py`，如果没有就新建一个
   （文件名必须与专题名一致）。
2. 调用 `ex(...)` 添加规格：

```python
ex(
    topic="03_variables",
    slug="13_new_exercise",
    title="...",
    objective="...",
    reference="Variables",          # 教程小节名
    hint="...",
    makefile="""
target: prereq
\tcommand
""",
    steps=[
        mk(stdout="what make prints", stdout_mode="contains"),
        mk("other-target", exit_code=2, stderr="No rule to make target"),
    ],
    breaks=[("correct text", "learner text")],
),
```

3. 重新生成并验证：

```sh
python3 tools/generate_exercises.py
./makefiling verify
./makefiling selftest
python3 tools/generate_exercises.py --check
make check-tracked
```

`make check-tracked` 确认 `exercises/`、`solutions/`、`templates/` 下的每个文件都
真的进了仓库。练习会故意携带 `report.d`、`blah.o` 这类看起来像构建产物的文件，
一旦 `.gitignore` 里出现宽泛的 `*.d` / `*.o` 规则，它们就会只在本地存在、不在
clone 里存在——本地全绿，CI 全红。CI 也会跑这一步。

## 规格的写法

### Tab

recipe 行必须以真正的 TAB 开头。规格是 Python 源码，直接写 TAB 既不可见
又容易丢失，因此约定用 `\t` 转义：

```python
makefile="""
hello:
\techo "Hello, World"
""",
```

Python 会把它变成真正的 TAB。Makefile 里需要的字面反斜杠要写成 `\\`。

### breaks

`breaks` 是 `(正确片段, 初始片段)` 的列表，生成器把它们依次应用在正确
内容上，得到学习者看到的初始版本。至少要有一次替换，而且替换之后必须
让**至少一个**检查步骤失败——`./makefiling selftest` 会强制检查这一点。

要改辅助文件（例如子目录里的 Makefile、C 源码）时用 `file_breaks`：

```python
file_breaks=[("sub/Makefile", "正确片段", "初始片段")],
```

### 检查步骤

每一步是 `mk(...)`（运行 make）或 `step(cmd, ...)`（运行任意命令），
可以指定：

| 参数 | 含义 |
| --- | --- |
| `exit_code` | 期望的退出码，默认 0 |
| `stdout` / `stdout_mode` | 对标准输出的期望和比较方式 |
| `stderr` / `stderr_mode` | 对标准错误的期望和比较方式 |
| `env` | 追加的环境变量 |
| `files` | 这一步之后必须存在、且内容完全一致的文件 |
| `missing` | 这一步之后必须不存在的文件 |
| `description` | 这一步在报告里显示的名字 |

比较方式见 [docs/architecture.md](docs/architecture.md#匹配模式)。默认是
`contains_lines`；优先使用 `contains` 和 `ordered_lines`，只有在确实
需要时才用 `exact`。

### 期望值必须是真实的

写期望之前，先在 `/tmp` 下建一个临时目录，把正确内容和辅助文件放进去，
把你打算写进 `steps` 的命令真正跑一遍，把观察到的输出抄进去。不要凭
记忆猜 make 会打印什么——这句话在本项目里是硬性要求。

### 确定性

- 不使用 `date`、`$$RANDOM`、`$$PPID` 之类会变化的输入。
- 不使用绝对路径；工作目录会被规范化成 `<stage>`。
- 不 `sleep`，不依赖时序。
- 不访问网络。
- 只操作编排目录内的文件。

### 时间戳必须显式指定

运行器会把 staging 出来的文件统一改成很久以前的固定时间（见
[docs/architecture.md](docs/architecture.md)），所以「配方刚写出的文件比练习
自带的文件新」是自动成立的，不需要你操心。

但**不要用裸 `touch` 去制造「某个文件更新了」**。上一条 recipe 刚把目标写出
来，而有些文件系统（CI runner 就是）把时间戳量化到整秒，`touch` 和目标可能落
在同一刻度里，make 就会认为无事可做，断言随机失败。要显式指定两个时间：

```python
step("touch", "-t", "202001010000", "out.txt",
     description="age the built file"),
step("touch", "-t", "202101010000", "b.txt",
     description="make the second prerequisite newer"),
```

先把目标调旧，再把需要变新的文件调到更晚，两者相差一年，任何时间戳粒度下都
不会含糊。`touch -t` 的格式是 `[[CC]YY]MMDDhhmm`；时间要落在过去，否则 make
会报 clock skew。

自查有没有漏网的：

```sh
python3 -c "
import json, glob
bad = [(d['exercise'], i) for f in glob.glob('exercises/*/*/checks.json')
       for d in [json.load(open(f))]
       for i, s in enumerate(d['steps'], 1)
       if s['args'] and s['args'][0] == 'touch' and '-t' not in s['args']]
print(bad)"
```

## 只重新生成一个专题

```sh
python3 tools/generate_exercises.py --topic 03_variables
./makefiling verify   --topic 03_variables
./makefiling selftest --topic 03_variables
```

`--topic` 只会导入对应的那一个规格文件，因此多个专题可以并行编写。

## 不要手工编辑的文件

`exercises/`、`solutions/`、`templates/`、各专题 `exercises/<topic>/README.md`
和 `docs/curriculum.md` 都是生成产物。要修改它们，请改
`tools/specs_*.py`，然后重新生成。CI 里的
`python3 tools/generate_exercises.py --check` 会拒绝不一致的提交。
