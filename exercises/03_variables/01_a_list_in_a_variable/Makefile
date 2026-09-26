# makeling exercise: 03_variables/01_a_list_in_a_variable
# title: A list stored in a variable
# objective: Keep the file names in a variable and use the same variable as the prerequisite list and inside the recipe.
# reference: Variables
# hint: A variable is just a string. Everywhere make meets $(files) it substitutes that string, in the prerequisite list of the target line exactly as in the recipe.

files := file1 file2

some_file:
	echo "Look at this variable: " $(files)
	touch some_file

file1:
	touch file1

file2:
	touch file2

clean:
	rm -f file1 file2 some_file
