SHELL := /bin/sh

which_shell:
	@echo "SHELL is: $(SHELL)"
	@echo "this line was run by: $${0}"
