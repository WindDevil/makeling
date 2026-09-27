# makefiling exercise: 11_other_features/14_delete_on_error_default
# title: Without DELETE_ON_ERROR the target stays
# objective: Turn the declaration off to see make's default: a rule that fails leaves its half written target on disk.
# reference: .delete_on_error
# hint: Historical default: make only reports the error. Remove the .DELETE_ON_ERROR line and the half written file survives, which is why the next build may think the target is up to date.

.DELETE_ON_ERROR:

halfway.txt:
	echo "half written" > halfway.txt
	false
