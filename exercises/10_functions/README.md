# Functions

[makefiletutorial.com](https://makefiletutorial.com/#first-functions)

Text functions: substitution references, ``$(subst)``, ``$(foreach)``, ``$(if)``, ``$(call)``, ``$(shell)``, ``$(filter)`` and the rest of the family.

Run an exercise with:

```sh
./makefiling run 10_functions/01_subst
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_subst` | Use $(subst from,to,text) to turn the sentence "I am not superman" into '"I am "totally" superman"'. | First Functions |
| `02_subst_spaces_and_commas` | Turn the list a b c into the single word a,b,c by replacing every space with a comma. | First Functions |
| `03_strip` | Normalise the messy variable into a b c: no leading, trailing or repeated whitespace left. | First Functions |
| `04_findstring` | Ask whether the haystack contains the word quick, and whether it contains the word slow. | First Functions |
| `05_patsubst` | Turn a.o b.o l.a c.o into a.c b.c l.a c.c, and turn the two src/ paths into build/ paths, with %.o and %.c patterns. | String Substitution |
| `06_substitution_reference` | Express the same rewrite twice: once with the % shorthand and once with the suffix-only shorthand. | String Substitution |
| `07_word_functions` | Report how many words names holds, then pick out its first, last, second and middle words. | First Functions |
| `08_sort` | Merge the two lists of sources into one alphabetical list without repeating a.c, and count the result. | First Functions |
| `09_filename_functions` | Take src/a.c src/b.h apart into directories, file names, suffixes and stems. | First Functions |
| `10_addprefix_addsuffix_join` | Turn the two names main util into object files, then put them under src/, and pair the prefixes src/ and build/ with two files. | First Functions |
| `11_wildcard` | Collect the C sources in the current directory and in the sub/ directory, and confirm that a pattern with no matches gives an empty list. | First Functions |
| `12_realpath_and_abspath` | Show that realpath resolves a name that exists on disk while abspath gives an absolute path for any name at all. | First Functions |
| `13_foreach` | Append an exclamation mark to each word of who are you, producing who! are! you! | The foreach function |
| `14_foreach_paths` | Map the module names auth cart order to build/auth.o build/cart.o build/order.o using a single foreach. | The foreach function |
| `15_if` | Produce then! for a condition that expands to something, else! for one that expands to nothing, and use the two-argument form too. | The if function |
| `16_call_basics` | Report the name of the called variable and its parameters with $(0), $(1) and $(2), and make a template that repeats its first parameter three times. | The call function |
| `17_call_template` | Use $(call) to turn the names main util into the object files src/main.o src/util.o, and let a pattern rule build them. | The call function |
| `18_shell` | Make snapshot capture the value of who as it is when the variable is defined, so it stays first even though who becomes second afterwards. | The shell function |
| `19_filter` | Keep only the .o files from obj_files, then keep the .o and .result files, then keep every C source and header. | The filter function |
| `20_filter_out` | Drop the headers from files, drop everything starting with test from objects, and nest the two ideas to keep only the objects that are left. | The filter function |

Tutorial sections covered:

- [First Functions](https://makefiletutorial.com/#first-functions)
- [String Substitution](https://makefiletutorial.com/#string-substitution)
- [The foreach function](https://makefiletutorial.com/#the-foreach-function)
- [The if function](https://makefiletutorial.com/#the-if-function)
- [The call function](https://makefiletutorial.com/#the-call-function)
- [The shell function](https://makefiletutorial.com/#the-shell-function)
- [The filter function](https://makefiletutorial.com/#the-filter-function)
