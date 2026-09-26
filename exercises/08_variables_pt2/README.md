# Variables Pt. 2

[makefiletutorial.com](https://makefiletutorial.com/#flavors-and-modification)

Recursive versus simply expanded variables, overriding from the command line, ``define``, and variables scoped to a target or a pattern.

Run an exercise with:

```sh
./makeling run 08_variables_pt2/01_recursive_vs_simply_expanded
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_recursive_vs_simply_expanded` | Assign one variable from another before that other variable exists, then define it: = picks up the new value, := keeps the one it saw at assignment time. | Flavors and modification |
| `02_simply_expanded_appending` | Extend one variable with its own old value plus a suffix, so that make prints the combined value instead of refusing to run. | Flavors and modification |
| `03_appending_recursive_vs_simply_expanded` | Append the same text to both flavours of variable, then change the variable they both refer to, and show that only the recursive one follows the change. | Flavors and modification |
| `04_default_with_question_mark` | Give one variable a default without clobbering the value it already has, and let a brand new variable take the default. | Flavors and modification |
| `05_spaces_and_the_null_string` | Build a value that ends in three spaces and a variable holding exactly one space, using the empty variable as the trick. | Flavors and modification |
| `06_undefined_is_empty` | Append a variable that nothing defines to a flag list, and confirm it contributes nothing until a value is supplied. | Flavors and modification |
| `07_substitution_references` | Turn a list of object files into the matching source files with the suffix shorthand and with the explicit pattern form. | Flavors and modification |
| `08_command_line_beats_plain_assignment` | Make the build mode a default that any value passed on the command line can replace, while a bare make still uses it. | Command line arguments and override |
| `09_override_wins` | Force one variable to keep the Makefile's own value no matter what the command line says, while the variable next to it is still replaceable. | Command line arguments and override |
| `10_environment_wins_with_dash_e` | Keep the Makefile's value in charge by default, let the environment take over when make runs with -e, and check that even then the command line still wins. | Command line arguments and override |
| `11_define_holds_several_commands` | Put three commands into a single define variable and run them all from the recipe with one $(name) reference. | List of commands and define |
| `12_define_and_separate_shells` | Keep a one-line variable that exports and prints in a single shell, and a define block that exports and prints in two, and show which one actually prints the value. | List of commands and define |
| `13_target_specific_variable` | Give the all target its own flavour without letting the other target see it. | Target-specific variables |
| `14_target_specific_reaches_prerequisites` | Declare the variable on all so that the target it depends on inherits it, while the same target built on its own does not. | Target-specific variables |
| `15_pattern_specific_variable` | Attach a variable to every target ending in .c, so that blah.c sees it and other targets do not. | Pattern-specific variables |
| `16_pattern_and_target_specific_together` | Let a pattern give every .o file a mode, then give one of them its own value, and leave a third target with neither. | Pattern-specific variables |

Tutorial sections covered:

- [Flavors and modification](https://makefiletutorial.com/#flavors-and-modification)
- [Command line arguments and override](https://makefiletutorial.com/#command-line-arguments-and-override)
- [List of commands and define](https://makefiletutorial.com/#list-of-commands-and-define)
- [Target-specific variables](https://makefiletutorial.com/#target-specific-variables)
- [Pattern-specific variables](https://makefiletutorial.com/#pattern-specific-variables)
