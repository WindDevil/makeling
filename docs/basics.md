# 基础路线：先建立 Make 的心智模型

如果你第一次接触 Make，不要一开始就把 177 道题当成一张考试卷。先用下面
的 20 题建立一个简单模型：

```text
目标 target  <-  前置条件 prerequisites
                    │
                    └─ recipe 负责产生目标
```

每次练习都按四步做：

1. 先看 `objective`，预测这次 `make` 会执行哪些命令。
2. 只修改题目要求的文件，然后运行 `./makefiling run`。
3. 失败时先读 make 的原始 stderr，再运行 `./makefiling hint --level 2`。
4. 通过后用自己的话解释“为什么这次执行或跳过了 recipe”。

启动基础路线：

```sh
./makefiling start
./makefiling next --basic
./makefiling run --basic
```

基础路线依次经过：第一条规则、默认目标、目标文件、前置条件、依赖链、增量
构建、变量、自动变量、`.PHONY` 和 `all`。完成后再进入其他专题；那些专题是
同一个模型的不同抽象，不要求你死记语法。

需要查看更具体的提示时逐级增加提示级别：

```sh
./makefiling hint 00_getting_started/01_first_rule --level 1
./makefiling hint 00_getting_started/01_first_rule --level 2
./makefiling hint 00_getting_started/01_first_rule --level 3
```
