# Curriculum: makefiletutorial.com, section by section

This map turns every section of [makefiletutorial.com](https://makefiletutorial.com/) into runnable
exercises.  Each exercise names the tutorial section it drills in its
`reference` field, so the two can be read side by side.

Total exercises: **177** across **13** topics.

## Getting Started (`00_getting_started`)

Tutorial sections: https://makefiletutorial.com/#why-do-makefiles-exist

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `00_getting_started/01_first_rule` | Write a rule that prints Hello, World when make runs. | Running the Examples |
| `00_getting_started/02_default_goal` | Order the rules so that a bare make runs the greeting, while make goodbye still runs the farewell. | Running the Examples |
| `00_getting_started/03_essence_target_file` | Make the hello target create a file called hello, so that a second make reports it is already up to date. | The essence of Make |
| `00_getting_started/04_essence_prerequisites` | Declare blah.c as a prerequisite of blah so that touching the source recompiles the program. | The essence of Make |
| `00_getting_started/05_which_makefile` | Give GNUmakefile and Makefile different default goals and confirm which one a bare make picks up. | Running the Examples |
| `00_getting_started/06_beyond_compilation` | Chain two non-compilation targets so that make builds a report file before printing it. | Why do Makefiles exist? |

## Makefile Syntax and the Essence of Make (`01_syntax_and_essence`)

Tutorial sections: https://makefiletutorial.com/#makefile-syntax

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_syntax_and_essence/01_rule_anatomy` | Write a rule whose target is report.txt, whose prerequisite is notes.txt, and whose recipe builds the report in two commands. | Makefile Syntax |
| `01_syntax_and_essence/02_several_targets_one_rule` | Write a single rule that applies to two target names, so that make can build either one of them. | Makefile Syntax |
| `01_syntax_and_essence/03_prerequisite_order` | Order the prerequisites of the all target so that make builds one, then two, then three. | Makefile Syntax |
| `01_syntax_and_essence/04_recipe_creates_the_target` | Make the hello target write its two lines into a file called hello, so that a second make finds nothing to do. | The essence of Make |
| `01_syntax_and_essence/05_timestamps_decide` | Give blah a prerequisite so that touching blah.c rebuilds it, while an older blah.c is ignored. | The essence of Make |
| `01_syntax_and_essence/06_every_prerequisite_counts` | Declare both parts as prerequisites of combined.txt so that touching either one rebuilds it. | The essence of Make |
| `01_syntax_and_essence/07_existing_file_is_skipped` | Name the target after the file that is already there, so that make skips the recipe instead of running it. | The essence of Make |
| `01_syntax_and_essence/08_no_prerequisites_always_runs` | Write a target that has no prerequisites and creates no file, and confirm that make runs it every time. | The essence of Make |
| `01_syntax_and_essence/09_directory_target` | Let make treat the existing directory out as the target's file, skipping the recipe until out/.keep becomes newer. | The essence of Make |
| `01_syntax_and_essence/10_no_rule_to_make_target` | Give broken a prerequisite that nothing creates, and watch make refuse to build it. | The essence of Make |
| `01_syntax_and_essence/11_nothing_to_do_vs_up_to_date` | Use a target with no recipe so make reports nothing to be done, and a target whose file exists so make reports it is up to date. | The essence of Make |

## More Quick Examples (`02_quick_examples`)

Tutorial sections: https://makefiletutorial.com/#more-quick-examples

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `02_quick_examples/01_three_step_chain` | Build blah in three steps: blah from blah.o, blah.o from blah.c, and a rule that creates blah.c itself. | More quick examples |
| `02_quick_examples/02_delete_a_source_reruns_everything` | Keep the three rules in place, then watch what happens when the generated blah.c is deleted: every recipe runs again. | More quick examples |
| `02_quick_examples/03_touching_an_intermediate_file` | Give blah.o its blah.c prerequisite so that touching either file rebuilds exactly as much as it has to. | More quick examples |
| `02_quick_examples/04_prerequisite_that_is_never_created` | Make some_file depend on other_file, a target whose recipe never creates a file, so that both recipes run every single time. | More quick examples |
| `02_quick_examples/05_several_goals_on_one_line` | Ask make for two targets at once and see that it builds them left to right, while a bare make still builds only the first. | More quick examples |
| `02_quick_examples/06_four_step_chain` | Extend the build with a fourth rule, so that blah.c is copied from source.txt, which is itself written by a recipe. | More quick examples |
| `02_quick_examples/07_shared_prerequisite` | Build a report from two files that are both copied from the same base file, and confirm the order the recipes run in. | More quick examples |
| `02_quick_examples/08_clean_can_run_twice` | Add a clean target that deletes some_file and can be run again when there is nothing left to delete. | Make clean |
| `02_quick_examples/09_a_file_named_clean` | Make clean run even though the directory contains a stray file with the same name as the target. | Make clean |
| `02_quick_examples/10_build_clean_build` | Complete the Makefile with a clean target that removes everything make created, so the same three recipes can run from scratch again. | Make clean |

## Variables (`03_variables`)

Tutorial sections: https://makefiletutorial.com/#variables

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `03_variables/01_a_list_in_a_variable` | Keep the file names in a variable and use the same variable as the prerequisite list and inside the recipe. | Variables |
| `03_variables/02_parens_or_braces` | Expand the same variable three ways: with parentheses, with braces, and with the bare $x form. | Variables |
| `03_variables/03_quotes_are_characters` | Assign a quoted string to a variable and see that make keeps the quote characters while the shell uses them. | Variables |
| `03_variables/04_a_value_passed_to_a_program` | Feed the value of a variable to printf and see that make splits it into words unless the expansion is quoted. | Variables |
| `03_variables/05_a_value_is_a_list_of_words` | Point a target at a variable whose value has irregular spacing and see make turn it into an ordinary word list. | Variables |
| `03_variables/06_dir_notdir_basename_suffix` | Apply $(dir), $(notdir), $(basename) and $(suffix) to one variable holding a list of paths. | Variables |
| `03_variables/07_addprefix_and_addsuffix` | Use $(addprefix) and $(addsuffix) to build an object list and a backup list out of one source list. | Makefile Cookbook |
| `03_variables/08_substitution_reference` | Turn a list of object files into the matching source list with the $(var:suffix=replacement) shorthand. | String Substitution |
| `03_variables/09_the_four_common_automatic_variables` | Print the target name, the out-of-date prerequisites, every prerequisite, and the first prerequisite from one recipe. | Automatic Variables |
| `03_variables/10_only_the_newer_prerequisites` | Make one of two prerequisites newer than the target and watch $? shrink while $^ stays the same. | Automatic Variables |
| `03_variables/11_one_rule_two_targets` | Write a single rule for f1.o and f2.o and let $@ name the output of each run. | Automatic Variables |
| `03_variables/12_target_directory_and_file` | Build a file inside a directory that does not exist yet, using $(@D) for the directory and $(@F) for the file name. | Automatic Variables |
| `03_variables/13_the_stem_variable` | Print $* for a target that ends in a known suffix and for one that does not. | Automatic Variables |
| `03_variables/14_first_prerequisite_only` | Copy the first of two prerequisites into the target while still reporting all of them. | Automatic Variables |

## Targets (`04_targets`)

Tutorial sections: https://makefiletutorial.com/#targets

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `04_targets/01_target_is_a_name` | Give the first rule the target name notes and the second the name real_file, so that make notes prints the note while real_file creates a file. | Targets |
| `04_targets/02_target_need_not_exist` | Make report depend on data.txt so that the data file is generated first, even though report itself is never created. | Targets |
| `04_targets/03_phony_clean` | Declare clean phony so that the stray file called clean does not make make skip the recipe. | Make clean |
| `04_targets/04_all_builds_everything` | List one, two and three in the all rule so that a bare make builds all three files. | The all target |
| `04_targets/05_all_from_a_variable` | Keep the list of targets in a variable and let all expand it instead of writing the names out. | The all target |
| `04_targets/06_multiple_targets_one_rule` | Put f1.o and f2.o on a single rule line and confirm that the recipe runs once for each target. | Multiple targets |
| `04_targets/07_shared_recipe_per_target` | Let a single recipe build both red.txt and blue.txt by writing to $@, so each target gets its own file. | Multiple targets |
| `04_targets/08_one_recipe_many_files` | Make a single recipe create both first.part and second.part for the bundle target. | Multiple targets |
| `04_targets/09_all_and_clean` | Keep all as the first rule and clean at the bottom, so that a bare make builds and make all clean builds then removes. | The all target |
| `04_targets/10_duplicate_prerequisites` | Make the inspect recipe print the deduplicated list with $^ and every mention of the repeated prerequisite with $+. | Automatic Variables |
| `04_targets/11_phony_all` | Declare all, one and two phony so that files of those names do not stop make from running the recipes. | .phony |
| `04_targets/12_shared_prerequisite_order` | Give one and two the same prerequisite base so that make builds base first and only once. | The all target |

## Automatic Variables and Wildcards (`05_wildcards_and_automatic_variables`)

Tutorial sections: https://makefiletutorial.com/#-wildcard

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `05_wildcards_and_automatic_variables/01_wildcard_function_in_a_variable` | Collect every .c file with $(wildcard *.c) and use the resulting list as the prerequisites of a target. | * Wildcard |
| `05_wildcards_and_automatic_variables/02_wildcard_empty_versus_shell_glob` | Show that $(wildcard *.dat) expands to nothing while a shell that globs *.dat in a recipe leaves the pattern as it is. | * Wildcard |
| `05_wildcards_and_automatic_variables/03_star_in_a_variable_stays_literal` | Contrast thing_wrong := *.o with thing_right := $(wildcard *.o) and observe what make does with each one as a prerequisite. | * Wildcard |
| `05_wildcards_and_automatic_variables/04_wildcard_in_a_target_list` | Write all: $(wildcard *.o) so that it still works when no object file exists, and see why a bare *.o in the same place does not. | * Wildcard |
| `05_wildcards_and_automatic_variables/05_parse_time_versus_recipe_time` | Have one rule create a .c file and another report both the parse-time $(wildcard *.c) and the recipe-time shell glob. | * Wildcard |
| `05_wildcards_and_automatic_variables/06_percent_in_patsubst` | Turn a list of .c names into .o names with $(patsubst %.c,%.o,...) and with the $(list:%.c=%.o) shorthand. | % Wildcard |
| `05_wildcards_and_automatic_variables/07_static_pattern_rule_stem` | Use $(targets): %.out: %.raw so that each target is matched by the target pattern and the stem is substituted into the prerequisite pattern. | % Wildcard |
| `05_wildcards_and_automatic_variables/08_dollar_at_and_dollar_less` | Copy the first prerequisite onto the target while printing both $@ and $< from the recipe. | Automatic Variables |
| `05_wildcards_and_automatic_variables/09_dollar_caret_and_dollar_question` | Build a target from two prerequisites and show that $^ names both while $? names only the one that has been touched since. | Automatic Variables |
| `05_wildcards_and_automatic_variables/10_dollar_star_without_a_pattern` | Print $* for a target ending in .o, for a target ending in .txt and for a target with no suffix at all. | Automatic Variables |
| `05_wildcards_and_automatic_variables/11_dollar_star_in_a_pattern_rule` | Write a pattern rule that copies %.txt to %.backup and prints the stem it matched. | Automatic Variables |
| `05_wildcards_and_automatic_variables/12_directory_and_file_variants` | Print $(@D), $(@F), $(<D), $(<F), $(^D) and $(^F) for a target that lives in a subdirectory. | Automatic Variables |
| `05_wildcards_and_automatic_variables/13_wildcard_patsubst_and_pattern_rule` | Discover the sources with $(wildcard src/*.c), rewrite them into build/ names with $(patsubst), and let a pattern rule build each one into its own directory. | * Wildcard |

## Fancy Rules (`06_fancy_rules`)

Tutorial sections: https://makefiletutorial.com/#implicit-rules

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `06_fancy_rules/01_implicit_link_rule` | Ask for an executable called blah without writing a single recipe, and let make's built-in C rules do the compiling and the linking. | Implicit Rules |
| `06_fancy_rules/02_generate_source_with_rule` | Let make create blah.c with a rule of your own, then watch the built-in rules compile and link it using CFLAGS. | Implicit Rules |
| `06_fancy_rules/03_implicit_rule_variables` | Set CC, CFLAGS and CPPFLAGS so the built-in compile rule builds blah.o with exactly those flags, and read the command with make -n. | Implicit Rules |
| `06_fancy_rules/04_cancel_pattern_rule` | Cancel make's built-in %.o: %.c rule with an empty pattern rule, so that only the object files you build by hand can exist. | Implicit Rules |
| `06_fancy_rules/05_erase_suffixes` | Empty the suffix list so make forgets how to compile and link C sources, and see that only explicit recipes are left. | Implicit Rules |
| `06_fancy_rules/06_static_pattern_objects` | Replace three hand-written object rules with a single static pattern rule over $(objects), and link them into a program. | Static Pattern Rules |
| `06_fancy_rules/07_static_pattern_stem` | Turn a list of .txt files into .raw ones with a static pattern rule, and print the stem that %.txt matched. | Static Pattern Rules |
| `06_fancy_rules/08_more_specific_match` | Keep the explicit rule for all.c so that it is written by hand, while the %.c pattern rule touches an empty file for the rest. | Static Pattern Rules |
| `06_fancy_rules/09_static_pattern_filter` | Use $(filter) to give .o files and .result files their own static pattern rules, so that each kind is built from the right source. | Static Pattern Rules and Filter |
| `06_fancy_rules/10_static_pattern_filter_out` | Build only the objects that are not test.o, using $(filter-out) in front of a static pattern rule. | Static Pattern Rules and Filter |
| `06_fancy_rules/11_pattern_rule_compile` | Write a %.o: %.c pattern rule whose recipe uses $< and $@, and see it applied to every matching target. | Pattern Rules |
| `06_fancy_rules/12_pattern_rule_no_prereq` | Add a %.c rule that has no prerequisite pattern, so make can always create a missing .c file -- empty. | Pattern Rules |
| `06_fancy_rules/13_pattern_vs_static` | Replace the two hand-listed targets with a pattern rule, so that extra.out is built as well even though no rule names it. | Pattern Rules |
| `06_fancy_rules/14_double_colon_order` | Define the same target twice with :: so that both recipes run, in the order they appear in the file. | Double-Colon Rules |
| `06_fancy_rules/15_single_colon_warning` | Repeat the target with single colons and confirm what make says: it warns and keeps only the last recipe. | Double-Colon Rules |
| `06_fancy_rules/16_double_colon_prereqs` | Give each :: rule its own prerequisite and its own recipe, so that make rebuilds only the rule whose prerequisite changed. | Double-Colon Rules |

## Commands and Execution (`07_commands_and_execution`)

Tutorial sections: https://makefiletutorial.com/#command-echoingsilencing

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `07_commands_and_execution/01_silencing_one_line` | Watch make print a recipe line before running it, and keep one line out of that echo with @. | Command Echoing/Silencing |
| `07_commands_and_execution/02_silencing_a_whole_target` | Keep one target's commands out of the output with .SILENT, and compare that with make -s, which silences everything. | Command Echoing/Silencing |
| `07_commands_and_execution/03_one_shell_per_line` | Prove that a cd on one recipe line does not reach the next line, and that joining two commands with a semicolon does. | Command Execution |
| `07_commands_and_execution/04_continuation_keeps_one_shell` | Show that a shell variable set on one line is gone by the next, and keep it alive by continuing the recipe line with a backslash. | Command Execution |
| `07_commands_and_execution/05_the_default_shell_is_sh` | Look at which program runs your recipe lines, and change it by giving make a different SHELL. | Default Shell |
| `07_commands_and_execution/06_shellflags` | Make a recipe line stop at its first failing command by adding -e to .SHELLFLAGS, and see what the default -c does instead. | Default Shell |
| `07_commands_and_execution/07_parallel_jobs` | Ask make for two jobs at once with -j2 and read the flags it hands to the recipe: the -j2 and the jobserver behind it. | Arguments to make |
| `07_commands_and_execution/08_make_variables_vs_shell_variables` | Give the shell a variable of its own in a recipe line, and see why $(...) and $$... are not interchangeable. | Double dollar sign |
| `07_commands_and_execution/09_literal_dollars` | Print a literal dollar sign, a command substitution and a loop variable by doubling the dollars make would otherwise eat. | Double dollar sign |
| `07_commands_and_execution/10_error_stops_make` | Run a command that fails and confirm that make stops right there: the rest of the recipe and the other target must not run. | Error handling with -k, -i, and - |
| `07_commands_and_execution/11_dash_suppresses_the_error` | Prefix a failing command with - so make prints the error, carries on with the recipe, and still reports the run as a success. | Error handling with -k, -i, and - |
| `07_commands_and_execution/12_ignore_errors_flag` | Compare a plain make, which stops at the failing line, with make -i, which ignores it and carries on. | Error handling with -k, -i, and - |
| `07_commands_and_execution/13_keep_going_flag` | Build three targets where the first one fails, and tell make -k and make -i apart. | Error handling with -k, -i, and - |
| `07_commands_and_execution/14_half_built_target` | Fail a recipe after it has written part of its output, and see that make keeps the partial file and treats it as finished. | Interrupting or killing make |
| `07_commands_and_execution/15_plan_with_dry_run` | Read every command a target would run with make -n, and check that the dry run really does not touch the filesystem. | Arguments to make |
| `07_commands_and_execution/16_recursive_make` | Have the top-level Makefile build the project in sub/ by asking $(MAKE) to read that directory's Makefile. | Recursive use of make |
| `07_commands_and_execution/17_dollar_make_not_bare_make` | Show what breaks when a recipe calls make instead of $(MAKE): the second make loses the flags and make -n no longer descends. | Recursive use of make |
| `07_commands_and_execution/18_exported_variables` | Print a make variable and a shell variable side by side, and show that environment variables are make variables from the start. | Export, environments, and recursive make |
| `07_commands_and_execution/19_unexport_and_export_all` | Export every variable at once with an argumentless export, then keep one of them out of the environment with unexport. | Export, environments, and recursive make |
| `07_commands_and_execution/20_export_across_recursion` | Let the Makefile in sub/ see a variable that only the top-level Makefile defines, by exporting it before the recursive call. | Export, environments, and recursive make |
| `07_commands_and_execution/21_command_line_variables` | Give MODE a default in the Makefile, override it with make MODE=..., and ask for several goals in one run. | Arguments to make |
| `07_commands_and_execution/22_directory_flag` | Run the Makefile in sub/ from the top of the tree with -C, keep the directory chatter down with --no-print-directory, and rebuild an up-to-date target with -B. | Arguments to make |

## Variables Pt. 2 (`08_variables_pt2`)

Tutorial sections: https://makefiletutorial.com/#flavors-and-modification

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `08_variables_pt2/01_recursive_vs_simply_expanded` | Assign one variable from another before that other variable exists, then define it: = picks up the new value, := keeps the one it saw at assignment time. | Flavors and modification |
| `08_variables_pt2/02_simply_expanded_appending` | Extend one variable with its own old value plus a suffix, so that make prints the combined value instead of refusing to run. | Flavors and modification |
| `08_variables_pt2/03_appending_recursive_vs_simply_expanded` | Append the same text to both flavours of variable, then change the variable they both refer to, and show that only the recursive one follows the change. | Flavors and modification |
| `08_variables_pt2/04_default_with_question_mark` | Give one variable a default without clobbering the value it already has, and let a brand new variable take the default. | Flavors and modification |
| `08_variables_pt2/05_spaces_and_the_null_string` | Build a value that ends in three spaces and a variable holding exactly one space, using the empty variable as the trick. | Flavors and modification |
| `08_variables_pt2/06_undefined_is_empty` | Append a variable that nothing defines to a flag list, and confirm it contributes nothing until a value is supplied. | Flavors and modification |
| `08_variables_pt2/07_substitution_references` | Turn a list of object files into the matching source files with the suffix shorthand and with the explicit pattern form. | Flavors and modification |
| `08_variables_pt2/08_command_line_beats_plain_assignment` | Make the build mode a default that any value passed on the command line can replace, while a bare make still uses it. | Command line arguments and override |
| `08_variables_pt2/09_override_wins` | Force one variable to keep the Makefile's own value no matter what the command line says, while the variable next to it is still replaceable. | Command line arguments and override |
| `08_variables_pt2/10_environment_wins_with_dash_e` | Keep the Makefile's value in charge by default, let the environment take over when make runs with -e, and check that even then the command line still wins. | Command line arguments and override |
| `08_variables_pt2/11_define_holds_several_commands` | Put three commands into a single define variable and run them all from the recipe with one $(name) reference. | List of commands and define |
| `08_variables_pt2/12_define_and_separate_shells` | Keep a one-line variable that exports and prints in a single shell, and a define block that exports and prints in two, and show which one actually prints the value. | List of commands and define |
| `08_variables_pt2/13_target_specific_variable` | Give the all target its own flavour without letting the other target see it. | Target-specific variables |
| `08_variables_pt2/14_target_specific_reaches_prerequisites` | Declare the variable on all so that the target it depends on inherits it, while the same target built on its own does not. | Target-specific variables |
| `08_variables_pt2/15_pattern_specific_variable` | Attach a variable to every target ending in .c, so that blah.c sees it and other targets do not. | Pattern-specific variables |
| `08_variables_pt2/16_pattern_and_target_specific_together` | Let a pattern give every .o file a mode, then give one of them its own value, and leave a third target with neither. | Pattern-specific variables |

## Conditional Part of Makefiles (`09_conditionals`)

Tutorial sections: https://makefiletutorial.com/#conditional-ifelse

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `09_conditionals/01_ifeq_else` | Branch on the value of foo so that make prints the matching message for both the file's value and an override on the command line. | Conditional if/else |
| `09_conditionals/02_branches_choose_rules` | Let the conditional decide which rule the Makefile contains, so that make debug builds when MODE is debug and make release builds when MODE is release. | Conditional if/else |
| `09_conditionals/03_parsed_top_to_bottom` | Assign MODE before the conditional that tests it, so that a bare make reports the debug build. | Conditional if/else |
| `09_conditionals/04_both_sides_expanded` | Compare two variables whose values are themselves variable references, so that the branch is taken. | Conditional if/else |
| `09_conditionals/05_quoting` | Write the comparisons so that quoting both sides matches and quoting only one side does not. | Conditional if/else |
| `09_conditionals/06_spaces_in_the_values` | Compare a value that itself contains a space, and rely on the space after the comma being ignored. | Conditional if/else |
| `09_conditionals/07_ifneq` | Use ifneq to choose the architecture message, for both the file's value of arch and an override on the command line. | Conditional if/else |
| `09_conditionals/08_ifdef_and_ifndef` | Report that foo is defined even though its value is a reference to the empty variable bar, and that bar itself is not. | Check if a variable is defined |
| `09_conditionals/09_ifdef_does_not_expand` | Show both sides of the trap: an empty variable and an undefined one compare equal, while ifdef still calls foo set. | Check if a variable is defined |
| `09_conditionals/10_empty_means_stripped` | Use the $(strip) idiom to recognise that foo holds only a space, and still detect a variable that was never given a value. | Check if a variable is empty |
| `09_conditionals/11_whitespace_is_not_empty` | Show that ifdef is true for a variable whose value is one space, while ifeq only sees it as empty once it is stripped. | Check if a variable is defined |
| `09_conditionals/12_makeflags_detecting_i` | Print the message when the user passed -i, and stay quiet otherwise, by searching $(MAKEFLAGS) for the letter. | $(MAKEFLAGS) |
| `09_conditionals/13_makeflags_silent` | Branch on whether -s was passed: bare make echoes the command, make -s only prints the message. | $(MAKEFLAGS) |
| `09_conditionals/14_shell_and_command_line` | Probe the filesystem with $(shell) and pick the value with ifeq, letting the probed file name come from the command line. | Conditional if/else |

## Functions (`10_functions`)

Tutorial sections: https://makefiletutorial.com/#first-functions

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `10_functions/01_subst` | Use $(subst from,to,text) to turn the sentence "I am not superman" into '"I am "totally" superman"'. | First Functions |
| `10_functions/02_subst_spaces_and_commas` | Turn the list a b c into the single word a,b,c by replacing every space with a comma. | First Functions |
| `10_functions/03_strip` | Normalise the messy variable into a b c: no leading, trailing or repeated whitespace left. | First Functions |
| `10_functions/04_findstring` | Ask whether the haystack contains the word quick, and whether it contains the word slow. | First Functions |
| `10_functions/05_patsubst` | Turn a.o b.o l.a c.o into a.c b.c l.a c.c, and turn the two src/ paths into build/ paths, with %.o and %.c patterns. | String Substitution |
| `10_functions/06_substitution_reference` | Express the same rewrite twice: once with the % shorthand and once with the suffix-only shorthand. | String Substitution |
| `10_functions/07_word_functions` | Report how many words names holds, then pick out its first, last, second and middle words. | First Functions |
| `10_functions/08_sort` | Merge the two lists of sources into one alphabetical list without repeating a.c, and count the result. | First Functions |
| `10_functions/09_filename_functions` | Take src/a.c src/b.h apart into directories, file names, suffixes and stems. | First Functions |
| `10_functions/10_addprefix_addsuffix_join` | Turn the two names main util into object files, then put them under src/, and pair the prefixes src/ and build/ with two files. | First Functions |
| `10_functions/11_wildcard` | Collect the C sources in the current directory and in the sub/ directory, and confirm that a pattern with no matches gives an empty list. | First Functions |
| `10_functions/12_realpath_and_abspath` | Show that realpath resolves a name that exists on disk while abspath gives an absolute path for any name at all. | First Functions |
| `10_functions/13_foreach` | Append an exclamation mark to each word of who are you, producing who! are! you! | The foreach function |
| `10_functions/14_foreach_paths` | Map the module names auth cart order to build/auth.o build/cart.o build/order.o using a single foreach. | The foreach function |
| `10_functions/15_if` | Produce then! for a condition that expands to something, else! for one that expands to nothing, and use the two-argument form too. | The if function |
| `10_functions/16_call_basics` | Report the name of the called variable and its parameters with $(0), $(1) and $(2), and make a template that repeats its first parameter three times. | The call function |
| `10_functions/17_call_template` | Use $(call) to turn the names main util into the object files src/main.o src/util.o, and let a pattern rule build them. | The call function |
| `10_functions/18_shell` | Make snapshot capture the value of who as it is when the variable is defined, so it stays first even though who becomes second afterwards. | The shell function |
| `10_functions/19_filter` | Keep only the .o files from obj_files, then keep the .o and .result files, then keep every C source and header. | The filter function |
| `10_functions/20_filter_out` | Drop the headers from files, drop everything starting with test from objects, and nest the two ideas to keep only the objects that are left. | The filter function |

## Other Features (`11_other_features`)

Tutorial sections: https://makefiletutorial.com/#include-makefiles

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `11_other_features/01_include_variables` | Move the project settings out of the Makefile into config.mk and include that file, so the recipes can still see the variables. | Include Makefiles |
| `11_other_features/02_include_rules` | Keep the build rules in tools.mk and include it: the rules must work and the included file's first target becomes the default goal. | Include Makefiles |
| `11_other_features/03_include_optional` | Read deps.mk when it is there and carry on when it is not, so a fresh checkout still builds. | Include Makefiles |
| `11_other_features/04_include_generated` | Give make a rule for version.mk and include it, so the version file is generated on the first run and reread. | Include Makefiles |
| `11_other_features/05_include_generated_deps` | Include report.d, the file a compiler writes with -M, so that make learns which sources the report is built from. | Include Makefiles |
| `11_other_features/06_vpath_headers` | Use vpath so that blah.h, which only exists in headers/, is found as a prerequisite of some_binary. | The vpath Directive |
| `11_other_features/07_vpath_clear` | Forget the old headers directory before adding the new one, so that blah.h resolves to the file in new/. | The vpath Directive |
| `11_other_features/08_vpath_variable` | Point VPATH at both directories that hold prerequisites, so blah.h and extra.txt are found without a vpath pattern. | The vpath Directive |
| `11_other_features/09_multiline_recipe` | Break one long shell command over two lines with a backslash so that the shell still receives it as a single command. | Multiline |
| `11_other_features/10_multiline_variable` | Continue the SOURCES variable onto a second line, so the list works both as prerequisites and as a value. | Multiline |
| `11_other_features/11_phony_file_conflict` | Declare clean phony so that the file named clean, created by some_file, cannot stop the clean rule from running. | .phony |
| `11_other_features/12_phony_conventional_targets` | Declare the conventional targets phony so a file named install and a directory named clean cannot shadow them. | .phony |
| `11_other_features/13_delete_on_error` | Switch on DELETE_ON_ERROR so that a rule which fails halfway leaves no half written target behind. | .delete_on_error |
| `11_other_features/14_delete_on_error_default` | Turn the declaration off to see make's default: a rule that fails leaves its half written target on disk. | .delete_on_error |

## Makefile Cookbook (`12_cookbook`)

Tutorial sections: https://makefiletutorial.com/#makefile-cookbook

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `12_cookbook/01_find_sources` | Let make collect every C and C++ file under ./src with $(shell find ...), leaving the patterns quoted. | Makefile Cookbook |
| `12_cookbook/02_object_paths` | Turn the source list into the object list the cookbook uses: $(BUILD_DIR)/./src/hello.cpp.o. | Makefile Cookbook |
| `12_cookbook/03_dependency_files` | Derive the .d files from the object list with the suffix-only substitution $(OBJS:.o=.d). | Makefile Cookbook |
| `12_cookbook/04_include_dirs` | Collect ./src and its subdirectories with $(shell find ... -type d) and prefix each one with -I. | Makefile Cookbook |
| `12_cookbook/05_compile_rules` | Write the two pattern rules that compile every source into $(BUILD_DIR), creating the object's directory first. | Makefile Cookbook |
| `12_cookbook/06_dependency_flags` | Add -MMD -MP to CPPFLAGS so that every compile also writes a .d file listing the headers it read. | Makefile Cookbook |
| `12_cookbook/07_link_executable` | Link the objects into $(BUILD_DIR)/$(TARGET_EXEC) with $(CXX) $(OBJS) -o $@. | Makefile Cookbook |
| `12_cookbook/08_include_deps` | Pull the .d files into the Makefile with -include, so that touching a header recompiles only the objects that include it. | Makefile Cookbook |
| `12_cookbook/09_full_cookbook` | Assemble the complete cookbook Makefile: sources, objects, dependency files, include flags, both compile rules, the link step and clean. | Makefile Cookbook |
