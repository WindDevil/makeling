# Variables

[makefiletutorial.com](https://makefiletutorial.com/#variables)

Assigning to variables, expanding them in targets and recipes, the quoting rules that surprise everyone, and the automatic variables every Makefile ends up using.

Run an exercise with:

```sh
./makeling run 03_variables/01_a_list_in_a_variable
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_a_list_in_a_variable` | Keep the file names in a variable and use the same variable as the prerequisite list and inside the recipe. | Variables |
| `02_parens_or_braces` | Expand the same variable three ways: with parentheses, with braces, and with the bare $x form. | Variables |
| `03_quotes_are_characters` | Assign a quoted string to a variable and see that make keeps the quote characters while the shell uses them. | Variables |
| `04_a_value_passed_to_a_program` | Feed the value of a variable to printf and see that make splits it into words unless the expansion is quoted. | Variables |
| `05_a_value_is_a_list_of_words` | Point a target at a variable whose value has irregular spacing and see make turn it into an ordinary word list. | Variables |
| `06_dir_notdir_basename_suffix` | Apply $(dir), $(notdir), $(basename) and $(suffix) to one variable holding a list of paths. | Variables |
| `07_addprefix_and_addsuffix` | Use $(addprefix) and $(addsuffix) to build an object list and a backup list out of one source list. | Makefile Cookbook |
| `08_substitution_reference` | Turn a list of object files into the matching source list with the $(var:suffix=replacement) shorthand. | String Substitution |
| `09_the_four_common_automatic_variables` | Print the target name, the out-of-date prerequisites, every prerequisite, and the first prerequisite from one recipe. | Automatic Variables |
| `10_only_the_newer_prerequisites` | Make one of two prerequisites newer than the target and watch $? shrink while $^ stays the same. | Automatic Variables |
| `11_one_rule_two_targets` | Write a single rule for f1.o and f2.o and let $@ name the output of each run. | Automatic Variables |
| `12_target_directory_and_file` | Build a file inside a directory that does not exist yet, using $(@D) for the directory and $(@F) for the file name. | Automatic Variables |
| `13_the_stem_variable` | Print $* for a target that ends in a known suffix and for one that does not. | Automatic Variables |
| `14_first_prerequisite_only` | Copy the first of two prerequisites into the target while still reporting all of them. | Automatic Variables |

Tutorial sections covered:

- [Variables](https://makefiletutorial.com/#variables)
- [Automatic Variables](https://makefiletutorial.com/#automatic-variables)
