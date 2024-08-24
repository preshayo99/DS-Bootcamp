# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Syntax error - Removed indentation from lines 6-7
animal = 'Lion'  # Runtime error - name variable not properly defined, missing quotation mark around lion
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a {}. It is a {} and it has {} teeth.".format(animal, animal_type, number_of_teeth)
# Runtime error - line 10 not formatted correctly and Logical error as variables are in the wrong order
print(full_spec)  # syntax error - missing brackets


# Can also use f-string notation for Line 10 and 12 to cut down to the code below:
# print(f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth.")
