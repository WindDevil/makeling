# makefiling exercise: 07_commands_and_execution/07_parallel_jobs
# title: make -j runs the goals as parallel jobs
# objective: Ask make for two jobs at once with -j2 and read the flags it hands to the recipe: the -j2 and the jobserver behind it.
# reference: Arguments to make
# hint: make -j2 runs the goal's prerequisites as separate jobs, so their output may arrive in any order. $(MAKEFLAGS) inside a recipe shows the -j2 and the jobserver make shares with nested makes.

all: one two
	@echo "jobs make handed the recipe: [$(MAKEFLAGS)]"

one:
	@echo "job one finished"

two:
	@echo "job two finished"
