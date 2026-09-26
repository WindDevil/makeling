# 架构

`makeling` 由四个互相独立的层次组成：

```text
规格层 (tools/specs_*.py)
        │
        ▼
生成层 (tools/generate_exercises.py)
        │
        ├── exercises/   初始练习
        ├── templates/   原始练习，用于 reset
        ├── solutions/   参考答案
        └── docs/        课程映射
        │
        ▼
契约层 (每个练习目录里的 checks.json)
        │
        ▼
运行层 (./makeling)
        │
        ├── 发现练习
        ├── 隔离编排到 build/makeling/
        ├── 重放契约中的每一步
        ├── 记录进度
        └── verify / selftest
```

## 为什么被测对象不是 C 程序

`clings` 和 `lspling` 的练习是 C 程序，测试代码可以写在同一个文件里，
由一个很小的断言头文件驱动。Makefile 练习没有这个便利：被测的对象是
**make 本身的行为**——它打印什么、以什么退出码结束、留下了哪些文件。

因此 `makeling` 把每个练习的验收条件抽出来，写成一个数据文件：

```text
exercises/<topic>/<slug>/checks.json
```

它列出了若干步骤，每一步是一条命令加上对结果的期望。运行器只是这个
文件的解释器。这样做有三个好处：

- 期望值是**数据**，不是代码，可以被生成、被 diff、被 `--check` 校验。
- 一个练习可以有任意多步，因此可以表达「先构建、再重新构建、观察
  第二次什么都不做」这类只有跨命令才能观察到的行为。
- 断言不限于标准输出，还包括退出码、stderr、以及命令结束后磁盘上
  该有哪些文件、不该有哪些文件。

## 规格驱动生成

每个练习的正确版本和初始版本来自同一份规格。生成器对正确内容应用
`breaks` 替换，得到初始练习。这样做的好处是：

- 修改正确内容时，初始练习自动同步。
- 参考答案和练习的验收条件完全一致。
- `./makeling selftest` 可以自动检查「初始失败、答案通过」这一不变量。
- 初始练习一定会失败，因为 `breaks` 至少替换掉一处；如果某次替换恰好
  没让任何检查失败，`selftest` 会报错。

`tools/generate_exercises.py --check` 用于 CI：如果生成文件与规格不一致，
CI 会失败。`exercises/`、`solutions/`、`templates/`、各专题 `README.md`
和 `docs/curriculum.md` 都是生成产物，不要手工修改。

只想重新生成一个专题时用 `--topic`：

```sh
python3 tools/generate_exercises.py --topic 03_variables
```

`--topic` 只导入对应的那个规格文件，因此多个专题可以并行编写。

## 运行器

`./makeling` 是一个零依赖 Python CLI。它的主要命令：

| 命令 | 作用 |
| --- | --- |
| `list` | 按专题列出练习和完成状态 |
| `next` | 显示下一个未完成练习 |
| `run [exercise]` | 在隔离目录里运行练习并核对契约 |
| `run --all` | 按顺序运行所有练习 |
| `hint` | 显示目标、参考小节和提示 |
| `hint --steps` | 同时打印这个练习的全部检查步骤 |
| `solution` | 打印或应用参考答案 |
| `reset` | 从 `templates/` 恢复初始练习 |
| `watch` | 文件变化后自动重跑 |
| `verify [exercise]` | 运行全部（或指定）参考答案 |
| `selftest` | 检查全部练习初始失败、答案通过 |
| `doctor` | 打印 Python 和 make 等工具链信息 |
| `clean` | 删除 `build/makeling/` |

进度保存在 `.makeling/progress.json`，该文件已被 `.gitignore` 忽略。

## 隔离编排

运行器**不在** `exercises/` 里直接跑 make。每次运行都会把练习目录复制到

```text
build/makeling/<topic>/<slug>/
```

再在那里执行契约中的步骤。这样做解决了三个问题：

- 学习者的 `exercises/` 目录不会被 `make` 产生的 `.o`、可执行文件、
  中间文件污染，`git status` 始终干净。
- 契约可以包含「第一次运行」和「第二次运行」，因为每次运行都从干净的
  副本开始，不会受上一次运行的残留影响。
- 顺序执行的多个步骤之间又确实共享状态（构建之后重新构建），这正是
  表达增量行为所需要的。

失败时运行器会打印被保留的工作目录路径，可以直接进去手工复现。

## 时间戳

make 判断该不该重建，靠的是比较目标和依赖的修改时间，而练习大量依赖这个
行为：「文件已经存在，所以什么都不用做」「这个依赖更新了，所以要重建」。
如果这些时间来自真实时钟，结论就取决于文件系统的时间戳粒度——CI runner 上
粒度是整整一秒，配方写出的目标和它刚读过的依赖可能落在同一刻度里，make 于是
认为无事可做，断言随机失败。

所以 staging 完成后，运行器会把复制出来的每个文件都改成一个固定的、很久以前
的时间：

```text
2000-01-01 00:00:00 起，按路径排序每个文件 +1 秒
```

两个效果：

- **练习自带的文件一律「很旧」**，契约里任何配方写出的文件都严格更新，比较
  结果不再取决于运行速度，在任何粒度下都成立。按路径排序同时让自带文件之间
  的相对顺序也确定下来——`copytree` 的顺序本来是 `readdir` 给的，不确定。
- **时间远在过去**，所以永远不会触发 make 的 clock skew 警告。

配方之间需要比较时间时（「把这个文件改成比那个新」），规格必须显式写出两个
时间，不能用裸 `touch`；写法见
[CONTRIBUTING.md](../CONTRIBUTING.md#时间戳必须显式指定)。

## 输出规范化

为了断言能跨机器成立，运行器在比较之前会规范化输出：

- 把工作目录的绝对路径替换成 `<stage>`。这样 `make -C`、递归 make 的
  `make[1]: Entering directory ...` 之类的消息就可以稳定断言。
- 去掉每行末尾的空白，去掉末尾的空行。
- 以 `LC_ALL=C` 运行，因此 make 自身的消息是英文的。
- 清空 `MAKEFLAGS`、`MFLAGS`、`MAKELEVEL`，避免外层环境影响结果。

期望值同样经过这套规范化，所以规格里写的是「make 会打印什么」，
而不是「在某个目录下会打印什么」。

## 匹配模式

每一步都可以为 stdout 和 stderr 各选一种比较方式：

| 模式 | 含义 |
| --- | --- |
| `exact` | 规范化之后完全相等 |
| `contains` | 输出包含给定文本 |
| `contains_lines` | 给定文本的每一行都出现，顺序任意 |
| `ordered_lines` | 给定文本的每一行都按顺序出现 |
| `regex` | 给定文本是正则表达式，在输出中搜索 |
| `not_contains` | 输出不包含给定文本 |

默认是 `contains_lines`。规格里应优先使用 `contains` 和 `ordered_lines`，
只有在确实需要时才用 `exact`：make 的输出里包含命令回显、目录名等
容易变化的部分，过严的断言会让练习在别的机器上误报失败。

`not_contains` 是很有用的一种：它让「第二次运行**没有**重新编译」这类
否定断言变得直接。

## 测试设计约束

Makefile 的输出很容易写出不确定的断言。本项目的约定是：

- 不使用 `date`、`$$RANDOM`、`$$PPID` 之类会变化的输入。
- 不使用绝对路径，不依赖运行时的当前目录名。
- 不 `sleep`，不依赖时序；需要观察「文件更新了」时用 `touch` 显式改变
  时间戳。
- 不访问网络，不写入 `exercises/`。
- 只操作编排目录内的文件；临时文件放在编排目录里而不是 `/tmp`，
  这样 `make clean` 之类的练习可以自己清理。
- 编译 C 的练习只使用 `int main(void) { return 0; }` 这种平凡源码，
  目的是观察 make 的行为，而不是测试编译器。

## 目录约定

- `exercises/`：学习者实际编辑的文件。
- `solutions/`：参考答案，不要在这里练习。
- `templates/`：初始练习的只读副本，由 `reset` 使用。
- `tools/specs_*.py`：唯一的练习事实来源。
- `.ref/`：`makefiletutorial.com` 的离线文本，供编写规格时对照；
  被 `.gitignore` 忽略。

如果只想修改一个练习的提示或目标，应修改对应的规格文件，然后运行
生成器，而不是直接编辑生成的文件。

## 规格里的 Tab

Makefile 的 recipe 行必须以真正的 TAB 开头。规格文件是 Python 源码，
直接嵌入 TAB 字符既不可见也容易在编辑过程中丢失，因此约定：

```python
makefile="""
hello:
\techo "Hello, World"
""",
```

Python 会把 `\t` 转义成真正的 TAB。同理，Makefile 里需要的字面反斜杠
（例如续行）要写成 `\\`。

如果写错成四个空格，make 会报 `missing separator`，`./makeling verify`
会立刻失败——错误不会静默通过。
