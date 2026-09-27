# makefiling exercise: 11_other_features/05_include_generated_deps
# title: The generated dependency file
# objective: Include report.d, the file a compiler writes with -M, so that make learns which sources the report is built from.
# reference: Include Makefiles
# hint: report.d holds one rule that adds prerequisites to report. Point the include at the file that is actually in the directory: the leading dash hides a misspelled name.

# report.d is what cc -M writes on an earlier build.
-include report.d

report:
	cat notes.txt > report
