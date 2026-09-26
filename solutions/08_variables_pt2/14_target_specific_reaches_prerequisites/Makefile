# makeling exercise: 08_variables_pt2/14_target_specific_reaches_prerequisites
# title: The variable reaches the prerequisites too
# objective: Declare the variable on all so that the target it depends on inherits it, while the same target built on its own does not.
# reference: Target-specific variables
# hint: A target-specific variable is inherited by everything all depends on, but only while all is being built. Naming the prerequisite directly on the command line skips all.

all: flavor = vanilla

all: cake

cake:
	echo cake is baked with [$(flavor)]

other:
	echo other is baked with [$(flavor)]
