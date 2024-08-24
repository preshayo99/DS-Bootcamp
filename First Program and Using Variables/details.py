# Ask for user's name and store in variable called 'name'
# Ask for user's age and store in variable called 'age'
# Ask for user's house number and store in variable called 'house_number'
# Ask for user's street name and store in variable called 'street_name'
# Print the above information out in a single sentence

name = input('Please enter your name: ').capitalize()
age = input('Please enter your age: ')
house_number = input('Please enter your house number: ')
street_name = input('Please enter your street name: ').capitalize()

print(f"This is {name}. They are {age} years old and they live at {house_number} {street_name}.")

