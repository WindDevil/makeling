# Commands and Execution

[makefiletutorial.com](https://makefiletutorial.com/#command-echoingsilencing)

How make prints and runs recipes: echoing and silencing, the shell it uses, ``$$``, error handling, interrupts, recursive make, exported environments, and the command line.

Run an exercise with:

```sh
./makeling run 07_commands_and_execution/01_silencing_one_line
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_silencing_one_line` | Watch make print a recipe line before running it, and keep one line out of that echo with @. | Command Echoing/Silencing |
| `02_silencing_a_whole_target` | Keep one target's commands out of the output with .SILENT, and compare that with make -s, which silences everything. | Command Echoing/Silencing |
| `03_one_shell_per_line` | Prove that a cd on one recipe line does not reach the next line, and that joining two commands with a semicolon does. | Command Execution |
| `04_continuation_keeps_one_shell` | Show that a shell variable set on one line is gone by the next, and keep it alive by continuing the recipe line with a backslash. | Command Execution |
| `05_the_default_shell_is_sh` | Look at which program runs your recipe lines, and change it by giving make a different SHELL. | Default Shell |
| `06_shellflags` | Make a recipe line stop at its first failing command by adding -e to .SHELLFLAGS, and see what the default -c does instead. | Default Shell |
| `07_parallel_jobs` | Ask make for two jobs at once with -j2 and read the flags it hands to the recipe: the -j2 and the jobserver behind it. | Arguments to make |
| `08_make_variables_vs_shell_variables` | Give the shell a variable of its own in a recipe line, and see why $(...) and $$... are not interchangeable. | Double dollar sign |
| `09_literal_dollars` | Print a literal dollar sign, a command substitution and a loop variable by doubling the dollars make would otherwise eat. | Double dollar sign |
| `10_error_stops_make` | Run a command that fails and confirm that make stops right there: the rest of the recipe and the other target must not run. | Error handling with -k, -i, and - |
| `11_dash_suppresses_the_error` | Prefix a failing command with - so make prints the error, carries on with the recipe, and still reports the run as a success. | Error handling with -k, -i, and - |
| `12_ignore_errors_flag` | Compare a plain make, which stops at the failing line, with make -i, which ignores it and carries on. | Error handling with -k, -i, and - |
| `13_keep_going_flag` | Build three targets where the first one fails, and tell make -k and make -i apart. | Error handling with -k, -i, and - |
| `14_half_built_target` | Fail a recipe after it has written part of its output, and see that make keeps the partial file and treats it as finished. | Interrupting or killing make |
| `15_plan_with_dry_run` | Read every command a target would run with make -n, and check that the dry run really does not touch the filesystem. | Arguments to make |
| `16_recursive_make` | Have the top-level Makefile build the project in sub/ by asking $(MAKE) to read that directory's Makefile. | Recursive use of make |
| `17_dollar_make_not_bare_make` | Show what breaks when a recipe calls make instead of $(MAKE): the second make loses the flags and make -n no longer descends. | Recursive use of make |
| `18_exported_variables` | Print a make variable and a shell variable side by side, and show that environment variables are make variables from the start. | Export, environments, and recursive make |
| `19_unexport_and_export_all` | Export every variable at once with an argumentless export, then keep one of them out of the environment with unexport. | Export, environments, and recursive make |
| `20_export_across_recursion` | Let the Makefile in sub/ see a variable that only the top-level Makefile defines, by exporting it before the recursive call. | Export, environments, and recursive make |
| `21_command_line_variables` | Give MODE a default in the Makefile, override it with make MODE=..., and ask for several goals in one run. | Arguments to make |
| `22_directory_flag` | Run the Makefile in sub/ from the top of the tree with -C, keep the directory chatter down with --no-print-directory, and rebuild an up-to-date target with -B. | Arguments to make |

Tutorial sections covered:

- [Command Echoing/Silencing](https://makefiletutorial.com/#command-echoingsilencing)
- [Command Execution](https://makefiletutorial.com/#command-execution)
- [Default Shell](https://makefiletutorial.com/#default-shell)
- [Double dollar sign](https://makefiletutorial.com/#double-dollar-sign)
- [Error handling with -k, -i, and -](https://makefiletutorial.com/#error-handling-with--k--i-and--)
- [Interrupting or killing make](https://makefiletutorial.com/#interrupting-or-killing-make)
- [Recursive use of make](https://makefiletutorial.com/#recursive-use-of-make)
- [Export, environments, and recursive make](https://makefiletutorial.com/#export-environments-and-recursive-make)
- [Arguments to make](https://makefiletutorial.com/#arguments-to-make)
