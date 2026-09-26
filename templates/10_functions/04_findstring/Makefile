# makeling exercise: 10_functions/04_findstring
# title: Looking for a substring with $(findstring)
# objective: Ask whether the haystack contains the word quick, and whether it contains the word slow.
# reference: First Functions
# hint: $(findstring find,in) searches in for the text find and returns find itself when it is there, or the empty string when it is not. The arguments are (needle, haystack).

haystack := the quick brown fox

$(info found=[$(findstring $(haystack),quick)])
$(info single=[$(findstring o,$(haystack))])
$(info missing=[$(findstring slow,$(haystack))])

all:
	@echo searched for quick and slow
