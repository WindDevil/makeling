# makefiling

`makefiling` 是一套面向 GNU Make 的动手练习集，逐节覆盖
[makefiletutorial.com](https://makefiletutorial.com/) 的全部内容。

每个练习都是一个能独立运行的目录，里面有一个 `Makefile` 和一个
`checks.json`。初始的 `Makefile` 故意留有缺失的规则、写错的变量或
不成立的依赖关系；你需要修改它，让 `./makefiling run` 通过。

第一次学习建议从 [基础路线](docs/basics.md) 开始：它把前 20 题串成一条
“预测 → 修改 → 观察 → 解释”的主线，再用 [小项目](docs/first-project.md)
把概念连起来。

## 练习专题

共 **13 个专题、177 个练习**，覆盖教程的主要可操作内容；Getting Started
还提供了替代工具和 Make 实现背景的阅读链接。

| 专题 | 练习数 | 对应的教程小节 | 目录 |
| --- | ---: | --- | --- |
| Getting Started | 6 | Why do Makefiles exist?、Running the Examples（另含背景阅读） | [`00_getting_started`](exercises/00_getting_started/) |
| Makefile Syntax and the Essence of Make | 11 | Makefile Syntax、The essence of Make | [`01_syntax_and_essence`](exercises/01_syntax_and_essence/) |
| More Quick Examples | 10 | More quick examples、Make clean | [`02_quick_examples`](exercises/02_quick_examples/) |
| Variables | 14 | Variables、Automatic Variables | [`03_variables`](exercises/03_variables/) |
| Targets | 12 | Targets、The all target、Multiple targets | [`04_targets`](exercises/04_targets/) |
| Automatic Variables and Wildcards | 13 | * Wildcard、% Wildcard、Automatic Variables | [`05_wildcards_and_automatic_variables`](exercises/05_wildcards_and_automatic_variables/) |
| Fancy Rules | 16 | Implicit Rules、Static Pattern Rules、Static Pattern Rules and Filter、Pattern Rules、Double-Colon Rules | [`06_fancy_rules`](exercises/06_fancy_rules/) |
| Commands and Execution | 22 | Command Echoing/Silencing、Command Execution、Default Shell、Double dollar sign、Error handling with -k, -i, and -、Interrupting or killing make、Recursive use of make、Export, environments, and recursive make、Arguments to make | [`07_commands_and_execution`](exercises/07_commands_and_execution/) |
| Variables Pt. 2 | 16 | Flavors and modification、Command line arguments and override、List of commands and define、Target-specific variables、Pattern-specific variables | [`08_variables_pt2`](exercises/08_variables_pt2/) |
| Conditional Part of Makefiles | 14 | Conditional if/else、Check if a variable is empty、Check if a variable is defined、$(MAKEFLAGS) | [`09_conditionals`](exercises/09_conditionals/) |
| Functions | 20 | First Functions、String Substitution、The foreach function、The if function、The call function、The shell function、The filter function | [`10_functions`](exercises/10_functions/) |
| Other Features | 14 | Include Makefiles、The vpath Directive、Multiline、.phony、.delete_on_error | [`11_other_features`](exercises/11_other_features/) |
| Makefile Cookbook | 9 | Makefile Cookbook | [`12_cookbook`](exercises/12_cookbook/) |

每个专题的 `README.md` 会列出该专题的练习清单和顺序；逐题对照表见 [docs/curriculum.md](docs/curriculum.md)。

## 特性

- **完整覆盖教程**：从第一条规则、变量、通配符，到模式规则、条件、
  函数和结尾的 cookbook，教程的每一个小节都有对应练习。
- **契约驱动**：每个练习的验收条件写在 `checks.json` 里——运行哪些命令、
  期望的退出码、标准输出、以及命令结束后磁盘上该有哪些文件。运行器
  只是这个契约的解释器。
- **隔离运行**：练习会被复制到 `build/makefiling/` 再执行，因此 `make`
  产生的 `.o`、可执行文件和中间文件不会污染 `exercises/`，
  不会额外污染 git；`git status` 只会反映你对练习文件本身的编辑。
- **自带 CLI**：列出、运行、提示、查看答案、重置进度和监听文件变化。
- **适合初学者**：`./makefiling start` 提供 20 题基础路线，提示按级别展开，
  失败时保留工作目录并显示 make 的原始诊断。
- **几乎零依赖**：只需要 `make` 和 Python 3（读取 `cat`、`touch`、
  `grep` 等标准 Unix 工具；涉及编译的练习额外需要 `cc`）。
- **答案与初始模板分离**：`solutions/` 保存参考答案，`templates/`
  保存原始练习，`exercises/` 是你实际修改的目录。
- **教程对照**：每个练习都标注它对应的教程小节，可以和原文对着读。
- **现代工程结构**：Makefile、CMake Presets、CTest、CI、Docker、
  EditorConfig。

## 快速开始

### 环境要求

- GNU Make 3.81+ 或 4.x
- Python 3.8+
- `cc`（只有涉及编译 C 的练习需要；GCC 或 Clang 均可）

Linux 上通常只需要：

```sh
sudo apt install build-essential python3
```

### 运行

```sh
# 查看全部练习
./makefiling list

# 开始基础路线
./makefiling start
./makefiling list --basic

# 运行下一个未完成的练习
./makefiling run

# 运行指定练习（支持完整 ID、目录名或唯一后缀）
./makefiling run 08_variables_pt2/01_recursive_vs_simply_expanded
./makefiling run 01_first_rule

# 查看提示
./makefiling hint 01_first_rule --level 1

# 查看这个练习要检查哪些东西
./makefiling hint 01_first_rule --steps

# 查看参考答案
./makefiling solution 01_first_rule

# 直接应用答案（会覆盖你的练习文件）
./makefiling solution 01_first_rule --apply

# 恢复初始练习
./makefiling reset 01_first_rule

# 监听文件变化，保存后自动重跑
./makefiling watch 01_first_rule
```

也可以使用 Makefile：

```sh
make list
make run
make verify
make selftest
make test
make doctor
make clean
```

## 学习流程

1. 阅读 `exercises/<topic>/README.md` 和 `Makefile` 顶部的目标与提示。
2. 修改 `exercises/<topic>/<slug>/Makefile`（必要时也修改同目录下的
   辅助文件），运行 `./makefiling run <exercise>`。
3. 如果卡住，先用 `./makefiling hint <exercise> --level 1`，再仔细读 make 的
   stderr；需要时逐级提高到 `--level 3`。失败时运行器会打印它保留的工作
   目录和可直接复制的重试命令，可以进去手工复现。
4. 通过后继续下一个练习；进度记录在 `.makefiling/progress.json`。
5. 完成一个专题后，对照 `docs/knowledge-map.md` 检查是否理解相关概念。
6. 最后运行 `./makefiling verify` 验证所有参考答案；`./makefiling selftest`
   检查的是仓库中的原始模板和参考答案，不会因为你已经完成某道题而失败。

有些练习一开始会**直接失败**，有些能跑但输出不对，还有一些会报
`missing separator`——这是刻意的：Makefile 的制表符规则本身就是教程的
第一课。

## 项目结构

```text
.
├── makefiling                   # 零依赖 Python CLI
├── exercises/                 # 你要修改的练习
│   ├── 00_getting_started/
│   │   ├── README.md
│   │   └── 01_first_rule/
│   │       ├── Makefile       # 练习本体
│   │       └── checks.json    # 验收契约
│   └── ...
├── solutions/                 # 参考答案（与 exercises 同结构）
├── templates/                 # 原始练习，用于 ./makefiling reset
├── tools/
│   ├── generate_exercises.py  # 生成器
│   ├── spec.py                # 规格数据结构与检查步骤 DSL
│   └── specs_*.py             # 每个专题一个规格文件
├── docs/
│   ├── basics.md              # 面向小白的 20 题基础路线
│   ├── first-project.md       # 用 cookbook 完成一个小项目
│   ├── architecture.md        # 生成器、运行器、契约设计
│   ├── curriculum.md          # 按教程小节列出全部练习
│   └── knowledge-map.md       # 按 GNU Make 知识领域列出覆盖范围
├── CMakeLists.txt
├── CMakePresets.json
├── Makefile
└── Dockerfile
```

## 构建方式

### 方式一：CLI + 按需运行（推荐）

`./makefiling` 只依赖 Python 标准库。它在需要时把练习复制到
`build/makefiling/` 的独立临时目录并执行契约中的命令。这种方式适合日常学习，
也允许多个检查命令同时运行。

```sh
./makefiling doctor
./makefiling verify
```

### 方式二：Makefile

```sh
make verify
make selftest
make check-generated
```

### 方式三：CMake + CTest

每个参考答案都会注册成一个 CTest 测试：

```sh
cmake --preset default
ctest --preset default
```

这个项目没有需要编译的产品，所以 `cmake --build` 是空的；CTest 测试
直接调用 `./makefiling verify <exercise>`。

### 方式四：Docker

```sh
docker build -t makefiling .
docker run --rm -it -v "$PWD:/makefiling" makefiling ./makefiling list
```

## 关于 make 版本

教程以 **GNU Make** 为准，它在 Linux 和 macOS 上都是标准实现。本项目的
练习在 GNU Make 3 和 4 上都能通过，CI 使用 Ubuntu 自带的版本。

BSD make 和 nmake 的语法与本教程不同，本项目的练习不适用于它们。

## 添加新练习

练习由 `tools/specs_*.py` 中的规格生成。每个规格包含正确的 `Makefile`、
一组检查步骤，以及一组「正确片段 → 初始片段」的替换。这样练习和答案
不会不同步。

```sh
# 编辑 tools/specs_*.py
python3 tools/generate_exercises.py
./makefiling verify
./makefiling selftest
python3 tools/generate_exercises.py --check
```

详见 [CONTRIBUTING.md](CONTRIBUTING.md) 和
[docs/architecture.md](docs/architecture.md)。

## 许可

项目代码使用 MIT License，见 [LICENSE](LICENSE)。

## 参考

- [makefiletutorial.com](https://makefiletutorial.com/) —— 本项目的选题来源
- [GNU Make Manual](https://www.gnu.org/software/make/manual/)
- [rustlings](https://github.com/rust-lang/rustlings) —— 练习集的形式来源
