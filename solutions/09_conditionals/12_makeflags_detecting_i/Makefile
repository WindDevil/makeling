# makefiling exercise: 09_conditionals/12_makeflags_detecting_i
# title: Detect the -i flag through $(MAKEFLAGS)
# objective: Print the message when the user passed -i, and stay quiet otherwise, by searching $(MAKEFLAGS) for the letter.
# reference: $(MAKEFLAGS)
# hint: MAKEFLAGS is a string of single letters, one per flag, without the leading dash. $(findstring i,$(MAKEFLAGS)) returns i when the flag is present and the empty string when it is not, so ifneq (,$(findstring ...)) is the test to write.

all:
ifneq (,$(findstring i, $(MAKEFLAGS)))
	echo "i was passed to MAKEFLAGS"
else
	echo "no i in MAKEFLAGS"
endif
