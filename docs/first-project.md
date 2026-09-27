# 小项目：为一个小型 C 项目写 Makefile

完成基础路线后，打开 `exercises/12_cookbook/09_full_cookbook/`，先不要看答案，
尝试解释并实现下面的目标：

- `make` 构建 `build/final_program`（完成后可以自己添加 `all` 入口）；
- C 和 C++ 源文件生成到 `build/` 下的对象文件；
- 头文件变化时只重新编译受影响的对象；
- `make clean` 删除整个 `build/`；
- 连续运行两次时，第二次不重新编译。

验证时运行：

```sh
./makefiling run 12_cookbook/09_full_cookbook
```

完成后，尝试脱离题目写一个自己的小项目：先画出依赖图，再为每条边写规则，
最后添加 `all`、`clean` 和 `.PHONY`。能解释每个目标何时重建，比背下一份
“万能 Makefile”更重要。
