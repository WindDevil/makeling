# makefiling exercise: 09_conditionals/05_quoting
# title: Quotes in an ifeq comparison
# objective: Write the comparisons so that quoting both sides matches and quoting only one side does not.
# reference: Conditional if/else
# hint: Inside ifeq (...) the two arguments are compared as text, so a quote is just another character: ('ok',"ok") never matches, because 'ok' and "ok" are different strings. Quote both sides or neither.

a = ok
b = ok

all:
ifeq ($(a),$(b))
	echo "plain comparison matches"
endif
ifeq ("$(a)","$(b)")
	echo "quoting both sides matches"
endif
ifeq "$(a)" "$(b)"
	echo "the space separated quoted form works"
endif
ifeq ('$(a)','$(b)')
	echo "mixed quotes match"
else
	echo "a quote is a literal character"
endif
