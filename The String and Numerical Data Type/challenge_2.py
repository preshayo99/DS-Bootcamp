# Ask user to enter their favourite restaurant and favourite number
string_fav = input('Please enter your favourite restaurant: ')
int_fav = int(input('Please enter your favourite number:'))

# Print the entered answers
print(f'\n Your favourite restaurant is:{string_fav}\n')
print(f'Your favourite number is:{int_fav}\n')

# When I try to cast string_fav as an integer, a value error occurred.
# This is because the answer given would be classed as a string as it is made up of text.
# The integer function is ONLY used for numbers
