# makeling exercise: 08_variables_pt2/10_environment_wins_with_dash_e
# title: make -e lets the environment win
# objective: Keep the Makefile's value in charge by default, let the environment take over when make runs with -e, and check that even then the command line still wins.
# reference: Command line arguments and override
# hint: ?= would hand the win to the environment always, because an exported variable already counts as defined. A plain = plus -e is the way to make the switch happen only when asked.

# Without -e this wins; with -e the environment wins instead.
mode ?= makefile

all:
	echo mode is $(mode)
