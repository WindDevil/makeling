# makeling exercise: 11_other_features/01_include_variables
# title: Include another file's variables
# objective: Move the project settings out of the Makefile into config.mk and include that file, so the recipes can still see the variables.
# reference: Include Makefiles
# hint: The directive is a line of its own: include config.mk. make reads that file while it parses the Makefile, so everything it defines is available from that point on.

# include config.mk

all: banner
	echo "build $(NAME)"

banner:
	echo "starting $(NAME)"

settings:
	echo "$(GREETING), $(NAME)"
