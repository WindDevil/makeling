# Automatic Variables and Wildcards

[makefiletutorial.com](https://makefiletutorial.com/#-wildcard)

The ``*`` and ``%`` wildcards, when each one is expanded, and the full set of automatic variables available inside a recipe.

Run an exercise with:

```sh
./makeling run 05_wildcards_and_automatic_variables/01_wildcard_function_in_a_variable
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_wildcard_function_in_a_variable` | Collect every .c file with $(wildcard *.c) and use the resulting list as the prerequisites of a target. | * Wildcard |
| `02_wildcard_empty_versus_shell_glob` | Show that $(wildcard *.dat) expands to nothing while a shell that globs *.dat in a recipe leaves the pattern as it is. | * Wildcard |
| `03_star_in_a_variable_stays_literal` | Contrast thing_wrong := *.o with thing_right := $(wildcard *.o) and observe what make does with each one as a prerequisite. | * Wildcard |
| `04_wildcard_in_a_target_list` | Write all: $(wildcard *.o) so that it still works when no object file exists, and see why a bare *.o in the same place does not. | * Wildcard |
| `05_parse_time_versus_recipe_time` | Have one rule create a .c file and another report both the parse-time $(wildcard *.c) and the recipe-time shell glob. | * Wildcard |
| `06_percent_in_patsubst` | Turn a list of .c names into .o names with $(patsubst %.c,%.o,...) and with the $(list:%.c=%.o) shorthand. | % Wildcard |
| `07_static_pattern_rule_stem` | Use $(targets): %.out: %.raw so that each target is matched by the target pattern and the stem is substituted into the prerequisite pattern. | % Wildcard |
| `08_dollar_at_and_dollar_less` | Copy the first prerequisite onto the target while printing both $@ and $< from the recipe. | Automatic Variables |
| `09_dollar_caret_and_dollar_question` | Build a target from two prerequisites and show that $^ names both while $? names only the one that has been touched since. | Automatic Variables |
| `10_dollar_star_without_a_pattern` | Print $* for a target ending in .o, for a target ending in .txt and for a target with no suffix at all. | Automatic Variables |
| `11_dollar_star_in_a_pattern_rule` | Write a pattern rule that copies %.txt to %.backup and prints the stem it matched. | Automatic Variables |
| `12_directory_and_file_variants` | Print $(@D), $(@F), $(<D), $(<F), $(^D) and $(^F) for a target that lives in a subdirectory. | Automatic Variables |
| `13_wildcard_patsubst_and_pattern_rule` | Discover the sources with $(wildcard src/*.c), rewrite them into build/ names with $(patsubst), and let a pattern rule build each one into its own directory. | * Wildcard |

Tutorial sections covered:

- [* Wildcard](https://makefiletutorial.com/#-wildcard)
- [% Wildcard](https://makefiletutorial.com/#-wildcard-1)
- [Automatic Variables](https://makefiletutorial.com/#automatic-variables)
