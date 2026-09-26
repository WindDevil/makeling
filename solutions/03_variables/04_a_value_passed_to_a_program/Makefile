# makeling exercise: 03_variables/04_a_value_passed_to_a_program
# title: Passing $(files) to a program
# objective: Feed the value of a variable to printf and see that make splits it into words unless the expansion is quoted.
# reference: Variables
# hint: The value of $(files) is the string "file1 file2". Unquoted it reaches printf as two arguments; put the expansion in double quotes to pass it as one.

files := file1 file2

all:
	echo "list: $(files)"
	printf '[%s]\n' $(files)
	printf '[%s]\n' "$(files)"
