# Targets

[makefiletutorial.com](https://makefiletutorial.com/#targets)

Targets as file names, the conventional ``all`` target, and rules that build more than one file at a time.

Run an exercise with:

```sh
./makefiling run 04_targets/01_target_is_a_name
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_target_is_a_name` | Give the first rule the target name notes and the second the name real_file, so that make notes prints the note while real_file creates a file. | Targets |
| `02_target_need_not_exist` | Make report depend on data.txt so that the data file is generated first, even though report itself is never created. | Targets |
| `03_phony_clean` | Declare clean phony so that the stray file called clean does not make make skip the recipe. | Make clean |
| `04_all_builds_everything` | List one, two and three in the all rule so that a bare make builds all three files. | The all target |
| `05_all_from_a_variable` | Keep the list of targets in a variable and let all expand it instead of writing the names out. | The all target |
| `06_multiple_targets_one_rule` | Put f1.o and f2.o on a single rule line and confirm that the recipe runs once for each target. | Multiple targets |
| `07_shared_recipe_per_target` | Let a single recipe build both red.txt and blue.txt by writing to $@, so each target gets its own file. | Multiple targets |
| `08_one_recipe_many_files` | Make a single recipe create both first.part and second.part for the bundle target. | Multiple targets |
| `09_all_and_clean` | Keep all as the first rule and clean at the bottom, so that a bare make builds and make all clean builds then removes. | The all target |
| `10_duplicate_prerequisites` | Make the inspect recipe print the deduplicated list with $^ and every mention of the repeated prerequisite with $+. | Automatic Variables |
| `11_phony_all` | Declare all, one and two phony so that files of those names do not stop make from running the recipes. | .phony |
| `12_shared_prerequisite_order` | Give one and two the same prerequisite base so that make builds base first and only once. | The all target |

Tutorial sections covered:

- [Targets](https://makefiletutorial.com/#targets)
- [The all target](https://makefiletutorial.com/#the-all-target)
- [Multiple targets](https://makefiletutorial.com/#multiple-targets)
