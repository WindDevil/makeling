# Fancy Rules

[makefiletutorial.com](https://makefiletutorial.com/#implicit-rules)

Implicit rules, static pattern rules, pattern rules, and double-colon rules: the four ways to say ``build things that look like this''.

Run an exercise with:

```sh
./makeling run 06_fancy_rules/01_implicit_link_rule
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_implicit_link_rule` | Ask for an executable called blah without writing a single recipe, and let make's built-in C rules do the compiling and the linking. | Implicit Rules |
| `02_generate_source_with_rule` | Let make create blah.c with a rule of your own, then watch the built-in rules compile and link it using CFLAGS. | Implicit Rules |
| `03_implicit_rule_variables` | Set CC, CFLAGS and CPPFLAGS so the built-in compile rule builds blah.o with exactly those flags, and read the command with make -n. | Implicit Rules |
| `04_cancel_pattern_rule` | Cancel make's built-in %.o: %.c rule with an empty pattern rule, so that only the object files you build by hand can exist. | Implicit Rules |
| `05_erase_suffixes` | Empty the suffix list so make forgets how to compile and link C sources, and see that only explicit recipes are left. | Implicit Rules |
| `06_static_pattern_objects` | Replace three hand-written object rules with a single static pattern rule over $(objects), and link them into a program. | Static Pattern Rules |
| `07_static_pattern_stem` | Turn a list of .txt files into .raw ones with a static pattern rule, and print the stem that %.txt matched. | Static Pattern Rules |
| `08_more_specific_match` | Keep the explicit rule for all.c so that it is written by hand, while the %.c pattern rule touches an empty file for the rest. | Static Pattern Rules |
| `09_static_pattern_filter` | Use $(filter) to give .o files and .result files their own static pattern rules, so that each kind is built from the right source. | Static Pattern Rules and Filter |
| `10_static_pattern_filter_out` | Build only the objects that are not test.o, using $(filter-out) in front of a static pattern rule. | Static Pattern Rules and Filter |
| `11_pattern_rule_compile` | Write a %.o: %.c pattern rule whose recipe uses $< and $@, and see it applied to every matching target. | Pattern Rules |
| `12_pattern_rule_no_prereq` | Add a %.c rule that has no prerequisite pattern, so make can always create a missing .c file -- empty. | Pattern Rules |
| `13_pattern_vs_static` | Replace the two hand-listed targets with a pattern rule, so that extra.out is built as well even though no rule names it. | Pattern Rules |
| `14_double_colon_order` | Define the same target twice with :: so that both recipes run, in the order they appear in the file. | Double-Colon Rules |
| `15_single_colon_warning` | Repeat the target with single colons and confirm what make says: it warns and keeps only the last recipe. | Double-Colon Rules |
| `16_double_colon_prereqs` | Give each :: rule its own prerequisite and its own recipe, so that make rebuilds only the rule whose prerequisite changed. | Double-Colon Rules |

Tutorial sections covered:

- [Implicit Rules](https://makefiletutorial.com/#implicit-rules)
- [Static Pattern Rules](https://makefiletutorial.com/#static-pattern-rules)
- [Static Pattern Rules and Filter](https://makefiletutorial.com/#static-pattern-rules-and-filter)
- [Pattern Rules](https://makefiletutorial.com/#pattern-rules)
- [Double-Colon Rules](https://makefiletutorial.com/#double-colon-rules)
