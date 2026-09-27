# Makefile Syntax and the Essence of Make

[makefiletutorial.com](https://makefiletutorial.com/#makefile-syntax)

The shape of a rule, the role of targets, prerequisites and recipes, and the file-existence rule that decides whether a recipe runs at all.

Run an exercise with:

```sh
./makefiling run 01_syntax_and_essence/01_rule_anatomy
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_rule_anatomy` | Write a rule whose target is report.txt, whose prerequisite is notes.txt, and whose recipe builds the report in two commands. | Makefile Syntax |
| `02_several_targets_one_rule` | Write a single rule that applies to two target names, so that make can build either one of them. | Makefile Syntax |
| `03_prerequisite_order` | Order the prerequisites of the all target so that make builds one, then two, then three. | Makefile Syntax |
| `04_recipe_creates_the_target` | Make the hello target write its two lines into a file called hello, so that a second make finds nothing to do. | The essence of Make |
| `05_timestamps_decide` | Give blah a prerequisite so that touching blah.c rebuilds it, while an older blah.c is ignored. | The essence of Make |
| `06_every_prerequisite_counts` | Declare both parts as prerequisites of combined.txt so that touching either one rebuilds it. | The essence of Make |
| `07_existing_file_is_skipped` | Name the target after the file that is already there, so that make skips the recipe instead of running it. | The essence of Make |
| `08_no_prerequisites_always_runs` | Write a target that has no prerequisites and creates no file, and confirm that make runs it every time. | The essence of Make |
| `09_directory_target` | Let make treat the existing directory out as the target's file, skipping the recipe until out/.keep becomes newer. | The essence of Make |
| `10_no_rule_to_make_target` | Give broken a prerequisite that nothing creates, and watch make refuse to build it. | The essence of Make |
| `11_nothing_to_do_vs_up_to_date` | Use a target with no recipe so make reports nothing to be done, and a target whose file exists so make reports it is up to date. | The essence of Make |

Tutorial sections covered:

- [Makefile Syntax](https://makefiletutorial.com/#makefile-syntax)
- [The essence of Make](https://makefiletutorial.com/#the-essence-of-make)
