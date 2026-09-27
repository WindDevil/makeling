# makefiling exercise: 07_commands_and_execution/19_unexport_and_export_all
# title: A bare export, and unexport to undo it
# objective: Export every variable at once with an argumentless export, then keep one of them out of the environment with unexport.
# reference: Export, environments, and recursive make
# hint: 'export' on its own line exports every variable, including the ones defined after it. A later 'unexport name' takes that variable back out of the environment, which is how you keep a secret out of your recipes.

greeting = hello from the Makefile
loud = exported on purpose
hidden = keep me out of the environment

export loud
unexport loud

# a bare export turns on exporting for every variable
export
unexport hidden

all:
	@echo "greeting make: [$(greeting)]"
	@echo "greeting shell: [$$greeting]"
	@echo "loud shell: [$$loud]"
	@echo "hidden shell: [$$hidden]"
