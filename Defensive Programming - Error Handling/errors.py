# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")  # syntax error - missing brackets
print("\n")  # syntax error - missing brackets and unnecessary indentation  it's the same block

# Variables declaring the user's age, casting the str to an int, and printing the result

# syntax error - Removed indentation from lines 10-19 as it was not necessary
age_str = '24'  # logical error - used '==' an equality operator (normally used to compare),
# instead of '=' to assign 24 to a variable

age = int(age_str)
print(f"I'm {age} years old.")  # Runtime error - # used f-string to properly concatenate string

# Variables declaring additional years and printing the total years of age
years_from_now = 3  # Removed the quotation mark as it would turn the 3 into a string
total_years = age + years_from_now

print(f"The total number of years: {total_years}")  # syntax and runtime error - missing bracket for print statement and
# 'answer_years' is an undeclared variable

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6  # Runtime error - total is an undeclared variable, so changed it to
# 'total_months'. I added '+6' as the final output wants the age in 3yrs AND 6 months

print(f"In 3 years and 6 months, I'll be {total_months} months old")  # runtime error - used f-string to properly
# concatenate string.

# HINT, 330 months is the correct answer
