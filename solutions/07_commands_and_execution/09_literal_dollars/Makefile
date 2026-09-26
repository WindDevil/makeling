# makeling exercise: 07_commands_and_execution/09_literal_dollars
# title: Dollars that must survive into the shell
# objective: Print a literal dollar sign, a command substitution and a loop variable by doubling the dollars make would otherwise eat.
# reference: Double dollar sign
# hint: Every $$ becomes one $ once make has expanded the line, so $$$$ hands the shell two dollars and $$(cmd) hands it a command substitution. Quoting decides what the shell then does with them.

report:
	@echo 'a literal dollar: $$$$'
	@echo "a command substitution: $$(echo hi)"
	@echo "make expanded the target name: [$@]"
	@echo "the shell's positional list is empty: [$$@]"
	@for i in 1 2 3; do echo "item $$i"; done
