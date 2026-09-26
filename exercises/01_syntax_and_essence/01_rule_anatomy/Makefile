# makeling exercise: 01_syntax_and_essence/01_rule_anatomy
# title: The anatomy of a rule
# objective: Write a rule whose target is report.txt, whose prerequisite is notes.txt, and whose recipe builds the report in two commands.
# reference: Makefile Syntax
# hint: A rule is the line 'targets: prerequisites' followed by the recipe. Every recipe line must begin with a real TAB character; four spaces are rejected with 'missing separator'.

report.txt: notes.txt
    echo "Report" > report.txt
    cat notes.txt >> report.txt
