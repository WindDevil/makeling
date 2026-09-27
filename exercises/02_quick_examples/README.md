# More Quick Examples

[makefiletutorial.com](https://makefiletutorial.com/#more-quick-examples)

A first end-to-end build: several targets, real prerequisites between them, and a ``clean`` target to undo the work.

Run an exercise with:

```sh
./makefiling run 02_quick_examples/01_three_step_chain
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_three_step_chain` | Build blah in three steps: blah from blah.o, blah.o from blah.c, and a rule that creates blah.c itself. | More quick examples |
| `02_delete_a_source_reruns_everything` | Keep the three rules in place, then watch what happens when the generated blah.c is deleted: every recipe runs again. | More quick examples |
| `03_touching_an_intermediate_file` | Give blah.o its blah.c prerequisite so that touching either file rebuilds exactly as much as it has to. | More quick examples |
| `04_prerequisite_that_is_never_created` | Make some_file depend on other_file, a target whose recipe never creates a file, so that both recipes run every single time. | More quick examples |
| `05_several_goals_on_one_line` | Ask make for two targets at once and see that it builds them left to right, while a bare make still builds only the first. | More quick examples |
| `06_four_step_chain` | Extend the build with a fourth rule, so that blah.c is copied from source.txt, which is itself written by a recipe. | More quick examples |
| `07_shared_prerequisite` | Build a report from two files that are both copied from the same base file, and confirm the order the recipes run in. | More quick examples |
| `08_clean_can_run_twice` | Add a clean target that deletes some_file and can be run again when there is nothing left to delete. | Make clean |
| `09_a_file_named_clean` | Make clean run even though the directory contains a stray file with the same name as the target. | Make clean |
| `10_build_clean_build` | Complete the Makefile with a clean target that removes everything make created, so the same three recipes can run from scratch again. | Make clean |

Tutorial sections covered:

- [More quick examples](https://makefiletutorial.com/#more-quick-examples)
- [Make clean](https://makefiletutorial.com/#make-clean)
