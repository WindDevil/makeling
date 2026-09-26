# makeling exercise: 11_other_features/10_multiline_variable
# title: A variable that spans lines
# objective: Continue the SOURCES variable onto a second line, so the list works both as prerequisites and as a value.
# reference: Multiline
# hint: A continued assignment also needs the trailing backslash, but here make joins the lines itself, collapsing the backslash, the newline and the following spaces into a single space. Indent the continuation with spaces, never a tab.

SOURCES = one.txt
          two.txt

combined.txt: $(SOURCES)
	cat $(SOURCES) > combined.txt

show:
	echo "[$(SOURCES)]"
