# Conditional Part of Makefiles

[makefiletutorial.com](https://makefiletutorial.com/#conditional-ifelse)

Choosing what a Makefile contains at parse time: ``ifeq`` and friends, testing for empty and undefined variables, and reading ``$(MAKEFLAGS)``.

Run an exercise with:

```sh
./makefiling run 09_conditionals/01_ifeq_else
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_ifeq_else` | Branch on the value of foo so that make prints the matching message for both the file's value and an override on the command line. | Conditional if/else |
| `02_branches_choose_rules` | Let the conditional decide which rule the Makefile contains, so that make debug builds when MODE is debug and make release builds when MODE is release. | Conditional if/else |
| `03_parsed_top_to_bottom` | Assign MODE before the conditional that tests it, so that a bare make reports the debug build. | Conditional if/else |
| `04_both_sides_expanded` | Compare two variables whose values are themselves variable references, so that the branch is taken. | Conditional if/else |
| `05_quoting` | Write the comparisons so that quoting both sides matches and quoting only one side does not. | Conditional if/else |
| `06_spaces_in_the_values` | Compare a value that itself contains a space, and rely on the space after the comma being ignored. | Conditional if/else |
| `07_ifneq` | Use ifneq to choose the architecture message, for both the file's value of arch and an override on the command line. | Conditional if/else |
| `08_ifdef_and_ifndef` | Report that foo is defined even though its value is a reference to the empty variable bar, and that bar itself is not. | Check if a variable is defined |
| `09_ifdef_does_not_expand` | Show both sides of the trap: an empty variable and an undefined one compare equal, while ifdef still calls foo set. | Check if a variable is defined |
| `10_empty_means_stripped` | Use the $(strip) idiom to recognise that foo holds only a space, and still detect a variable that was never given a value. | Check if a variable is empty |
| `11_whitespace_is_not_empty` | Show that ifdef is true for a variable whose value is one space, while ifeq only sees it as empty once it is stripped. | Check if a variable is defined |
| `12_makeflags_detecting_i` | Print the message when the user passed -i, and stay quiet otherwise, by searching $(MAKEFLAGS) for the letter. | $(MAKEFLAGS) |
| `13_makeflags_silent` | Branch on whether -s was passed: bare make echoes the command, make -s only prints the message. | $(MAKEFLAGS) |
| `14_shell_and_command_line` | Probe the filesystem with $(shell) and pick the value with ifeq, letting the probed file name come from the command line. | Conditional if/else |

Tutorial sections covered:

- [Conditional if/else](https://makefiletutorial.com/#conditional-ifelse)
- [Check if a variable is empty](https://makefiletutorial.com/#check-if-a-variable-is-empty)
- [Check if a variable is defined](https://makefiletutorial.com/#check-if-a-variable-is-defined)
- [$(MAKEFLAGS)](https://makefiletutorial.com/#makeflags)
