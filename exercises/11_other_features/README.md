# Other Features

[makefiletutorial.com](https://makefiletutorial.com/#include-makefiles)

The directives and special targets that finish a real Makefile: ``include``, ``vpath``, multiline definitions, ``.PHONY`` and ``.DELETE_ON_ERROR``.

Run an exercise with:

```sh
./makeling run 11_other_features/01_include_variables
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_include_variables` | Move the project settings out of the Makefile into config.mk and include that file, so the recipes can still see the variables. | Include Makefiles |
| `02_include_rules` | Keep the build rules in tools.mk and include it: the rules must work and the included file's first target becomes the default goal. | Include Makefiles |
| `03_include_optional` | Read deps.mk when it is there and carry on when it is not, so a fresh checkout still builds. | Include Makefiles |
| `04_include_generated` | Give make a rule for version.mk and include it, so the version file is generated on the first run and reread. | Include Makefiles |
| `05_include_generated_deps` | Include report.d, the file a compiler writes with -M, so that make learns which sources the report is built from. | Include Makefiles |
| `06_vpath_headers` | Use vpath so that blah.h, which only exists in headers/, is found as a prerequisite of some_binary. | The vpath Directive |
| `07_vpath_clear` | Forget the old headers directory before adding the new one, so that blah.h resolves to the file in new/. | The vpath Directive |
| `08_vpath_variable` | Point VPATH at both directories that hold prerequisites, so blah.h and extra.txt are found without a vpath pattern. | The vpath Directive |
| `09_multiline_recipe` | Break one long shell command over two lines with a backslash so that the shell still receives it as a single command. | Multiline |
| `10_multiline_variable` | Continue the SOURCES variable onto a second line, so the list works both as prerequisites and as a value. | Multiline |
| `11_phony_file_conflict` | Declare clean phony so that the file named clean, created by some_file, cannot stop the clean rule from running. | .phony |
| `12_phony_conventional_targets` | Declare the conventional targets phony so a file named install and a directory named clean cannot shadow them. | .phony |
| `13_delete_on_error` | Switch on DELETE_ON_ERROR so that a rule which fails halfway leaves no half written target behind. | .delete_on_error |
| `14_delete_on_error_default` | Turn the declaration off to see make's default: a rule that fails leaves its half written target on disk. | .delete_on_error |

Tutorial sections covered:

- [Include Makefiles](https://makefiletutorial.com/#include-makefiles)
- [The vpath Directive](https://makefiletutorial.com/#the-vpath-directive)
- [Multiline](https://makefiletutorial.com/#multiline)
- [.phony](https://makefiletutorial.com/#phony)
- [.delete_on_error](https://makefiletutorial.com/#delete_on_error)
