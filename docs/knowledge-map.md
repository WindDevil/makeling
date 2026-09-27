# Knowledge map

This map lists the GNU Make knowledge areas `makefiling` covers and points at the
topic that drills each one.  It is the checklist to read after finishing a
topic, and the list to consult when adding new exercises.

The curriculum itself, exercise by exercise, is in
[curriculum.md](curriculum.md).

## The execution model

| Area | Topic |
| --- | --- |
| Rules, targets, prerequisites and recipes; the tab requirement | `01_syntax_and_essence` |
| The first target as the default goal, and naming goals on the command line | `00_getting_started`, `04_targets` |
| Gitignore-style comparison of target and prerequisite timestamps | `01_syntax_and_essence` |
| A target whose name matches an existing file is skipped | `01_syntax_and_essence`, `11_other_features` |
| Target selection order and the dependency graph walk | `02_quick_examples` |
| `make -n` as a way to see what make decided | `07_commands_and_execution` |
| Loading more than one makefile, and which file make reads first | `00_getting_started`, `11_other_features` |

## Targets

| Area | Topic |
| --- | --- |
| `all` as the conventional aggregate target | `04_targets` |
| Multiple targets on one rule line and one recipe per target | `04_targets` |
| Independent recipes for several targets | `04_targets` |
| `.PHONY` and the file-shadowing problem it prevents | `04_targets`, `11_other_features` |
| `clean` and re-building from scratch | `02_quick_examples` |
| Double-colon rules and independent recipes for one target | `06_fancy_rules` |

## Variables

| Area | Topic |
| --- | --- |
| Assignment with `=`, `:=`, `?=` and `+=` | `03_variables`, `08_variables_pt2` |
| Recursive versus simply expanded variables | `08_variables_pt2` |
| Variable references in targets, prerequisites and recipes | `03_variables` |
| Shell quoting and word splitting of variable values | `03_variables` |
| Command-line overrides, `override`, and `make -e` | `08_variables_pt2` |
| Target-specific and pattern-specific variables | `08_variables_pt2` |
| `define`/`endef` for multi-line values | `08_variables_pt2` |
| Automatic variables `$@`, `$<`, `$^`, `$?`, `$*` and their `D`/`F` forms | `03_variables`, `05_wildcards_and_automatic_variables` |
| `MAKEFLAGS`, `MAKE`, `CURDIR` and the other built-in variables | `09_conditionals`, `07_commands_and_execution` |

## Wildcards and pattern matching

| Area | Topic |
| --- | --- |
| `$(wildcard)` at parse time versus the shell expanding in a recipe | `05_wildcards_and_automatic_variables` |
| `%` as make's wildcard and the stem it produces | `05_wildcards_and_automatic_variables`, `06_fancy_rules` |
| `$(patsubst)` and substitution references | `03_variables`, `10_functions` |
| Static pattern rules and the explicit target list | `06_fancy_rules` |
| Pattern rules and implicit rule search | `06_fancy_rules` |
| Built-in implicit rules and how to cancel them | `06_fancy_rules` |

## Commands and the shell

| Area | Topic |
| --- | --- |
| Command echoing, `@`, `.SILENT` and `make -s` | `07_commands_and_execution` |
| One shell per recipe line, and the `; \` continuation | `07_commands_and_execution` |
| `SHELL` and `.SHELLFLAGS` | `07_commands_and_execution` |
| `$$` for shell variables, `$$$$` for a literal dollar | `07_commands_and_execution` |
| Error handling: the `-` prefix, `make -i`, `make -k` | `07_commands_and_execution` |
| Interrupting a build and half-written targets | `07_commands_and_execution`, `11_other_features` |
| Recursive make with `$(MAKE)` and `make -C` | `07_commands_and_execution` |
| `export`, `unexport` and the environment seen by recipes | `07_commands_and_execution` |
| Useful command-line arguments to make | `07_commands_and_execution` |

## Conditionals and functions

| Area | Topic |
| --- | --- |
| `ifeq`, `ifneq`, `ifdef`, `ifndef`, `else`, `endif` | `09_conditionals` |
| Testing for an empty variable, and `$(strip)` | `09_conditionals` |
| Testing whether a variable is defined | `09_conditionals` |
| Reading `$(MAKEFLAGS)` to detect the flags in force | `09_conditionals` |
| Text functions: `subst`, `patsubst`, `strip`, `findstring`, `sort` | `10_functions` |
| List functions: `word`, `wordlist`, `words`, `firstword`, `lastword` | `10_functions` |
| File-name functions: `dir`, `notdir`, `suffix`, `basename`, `addprefix`, `addsuffix`, `join` | `10_functions` |
| `$(foreach)`, `$(if)`, `$(call)` | `10_functions` |
| `$(shell)` at expansion time | `10_functions` |
| `$(filter)` and `$(filter-out)` | `06_fancy_rules`, `10_functions` |

## Project structure

| Area | Topic |
| --- | --- |
| `include` and `-include` of generated dependency files | `11_other_features`, `12_cookbook` |
| `vpath` and `VPATH` | `11_other_features` |
| Multi-line recipes and line continuation | `11_other_features` |
| `.DELETE_ON_ERROR` | `11_other_features` |
| Out-of-tree objects and `$(patsubst)`-derived build paths | `12_cookbook` |
| Generating `.d` dependency files with `-MMD -MP` | `12_cookbook` |
| Assembling include directories into `-I` flags | `12_cookbook` |

## Related topics deliberately left out

The tutorial does not cover them, so neither does `makefiling`:

- Automake, CMake and the other generators that emit Makefiles.
- Non-GNU make implementations (BSD make, nmake) beyond knowing they exist.
- `make --jobserver-auth`, `.ONESHELL`, `.NOTPARALLEL` and the other
  special targets that only matter once a build is already working.
- Guile and loadable-object extensions.
