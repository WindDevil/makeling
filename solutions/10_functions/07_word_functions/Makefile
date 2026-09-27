# makefiling exercise: 10_functions/07_word_functions
# title: Counting and picking words
# objective: Report how many words names holds, then pick out its first, last, second and middle words.
# reference: First Functions
# hint: $(words list) counts the words, $(firstword list) and $(lastword list) take the ends, $(word n,list) takes the nth, and $(wordlist start,end,list) takes a range. Asking for a word that is past the end returns nothing.

names := ada grace edsger barbara

$(info count=[$(words $(names))])
$(info first=[$(firstword $(names))])
$(info last=[$(lastword $(names))])
$(info second=[$(word 2,$(names))])
$(info middle=[$(wordlist 2,3,$(names))])
$(info past=[$(word 9,$(names))])

all:
	@echo $(firstword $(names)) and $(lastword $(names))
