# makefiling exercise: 01_syntax_and_essence/05_timestamps_decide
# title: Timestamps decide whether to rebuild
# objective: Give blah a prerequisite so that touching blah.c rebuilds it, while an older blah.c is ignored.
# reference: The essence of Make
# hint: Without a prerequisite make only asks whether blah exists. Add blah.c after the colon and make starts comparing timestamps.

blah: blah.c
	cp blah.c blah
