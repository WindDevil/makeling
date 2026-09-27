# Getting Started

[makefiletutorial.com](https://makefiletutorial.com/#why-do-makefiles-exist)

Why Makefiles exist, what people use instead, which flavour of make you are running, and how an example is actually executed.

Run an exercise with:

```sh
./makefiling run 00_getting_started/01_first_rule
```

| Exercise | Objective | Tutorial section |
| --- | --- | --- |
| `01_first_rule` | Write a rule that prints Hello, World when make runs. | Running the Examples |
| `02_default_goal` | Order the rules so that a bare make runs the greeting, while make goodbye still runs the farewell. | Running the Examples |
| `03_essence_target_file` | Make the hello target create a file called hello, so that a second make reports it is already up to date. | The essence of Make |
| `04_essence_prerequisites` | Declare blah.c as a prerequisite of blah so that touching the source recompiles the program. | The essence of Make |
| `05_which_makefile` | Give GNUmakefile and Makefile different default goals and confirm which one a bare make picks up. | Running the Examples |
| `06_beyond_compilation` | Chain two non-compilation targets so that make builds a report file before printing it. | Why do Makefiles exist? |

Tutorial sections covered:

- [Why do Makefiles exist?](https://makefiletutorial.com/#why-do-makefiles-exist)
- [What alternatives are there to Make?](https://makefiletutorial.com/#what-alternatives-are-there-to-make)
- [The versions and types of Make](https://makefiletutorial.com/#the-versions-and-types-of-make)
- [Running the Examples](https://makefiletutorial.com/#running-the-examples)
