# makeling exercise: 11_other_features/04_include_generated
# title: Make rebuilds a makefile it includes
# objective: Give make a rule for version.mk and include it, so the version file is generated on the first run and reread.
# reference: Include Makefiles
# hint: Before giving up on an included file make looks for a rule that can build it. Add the rule and keep the include optional so the very first run can still start.

# include version.mk

VERSION ?= unknown

all:
	echo "version $(VERSION)"

version.mk:
	echo "VERSION = 1.0" > version.mk
