# makefiling exercise: 05_wildcards_and_automatic_variables/12_directory_and_file_variants
# title: The D and F variants of the automatic variables
# objective: Print $(@D), $(@F), $(<D), $(<F), $(^D) and $(^F) for a target that lives in a subdirectory.
# reference: Automatic Variables
# hint: Every automatic variable that holds file names has a D variant for the directory part and an F variant for the file part. A name with no directory gives . as its D part, which is exactly what mkdir -p $(@D) needs.

out/report.txt: src/one.txt src/two.txt
	@echo at: D=[$(@D)] F=[$(@F)]
	@echo lt: D=[$(<D)] F=[$(<F)]
	@echo all: D=[$(^D)] F=[$(^F)]
	@mkdir -p $(@D)
	@touch $@

orphan.txt: src/one.txt
	@echo orphan D=[$(@D)] F=[$(@F)]
	@touch $@
