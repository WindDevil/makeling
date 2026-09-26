# Makefile Cookbook

[makefiletutorial.com](https://makefiletutorial.com/#makefile-cookbook)

The full project Makefile from the end of the tutorial: source discovery, out-of-tree objects, generated header dependencies, and both C and C++ compilation.

Run an exercise with:

```sh
./makeling run 12_cookbook/01_find_sources
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_find_sources` | Let make collect every C and C++ file under ./src with $(shell find ...), leaving the patterns quoted. | Makefile Cookbook |
| `02_object_paths` | Turn the source list into the object list the cookbook uses: $(BUILD_DIR)/./src/hello.cpp.o. | Makefile Cookbook |
| `03_dependency_files` | Derive the .d files from the object list with the suffix-only substitution $(OBJS:.o=.d). | Makefile Cookbook |
| `04_include_dirs` | Collect ./src and its subdirectories with $(shell find ... -type d) and prefix each one with -I. | Makefile Cookbook |
| `05_compile_rules` | Write the two pattern rules that compile every source into $(BUILD_DIR), creating the object's directory first. | Makefile Cookbook |
| `06_dependency_flags` | Add -MMD -MP to CPPFLAGS so that every compile also writes a .d file listing the headers it read. | Makefile Cookbook |
| `07_link_executable` | Link the objects into $(BUILD_DIR)/$(TARGET_EXEC) with $(CXX) $(OBJS) -o $@. | Makefile Cookbook |
| `08_include_deps` | Pull the .d files into the Makefile with -include, so that touching a header recompiles only the objects that include it. | Makefile Cookbook |
| `09_full_cookbook` | Assemble the complete cookbook Makefile: sources, objects, dependency files, include flags, both compile rules, the link step and clean. | Makefile Cookbook |

Tutorial sections covered:

- [Makefile Cookbook](https://makefiletutorial.com/#makefile-cookbook)
