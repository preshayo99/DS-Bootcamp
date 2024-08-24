# Asking user to enter a sentence and then calculate length of sentence
str_manip = input('Please enter a sentence : ')
str_length = len(str_manip)
print(f"The sentence has {str_length} characters, including spaces\n")

# Find the last letter in str_manip and replace every occurrence of this letter with '@'
last_letter = str_manip[-1]
new_str = str_manip.replace(last_letter, '@')

print(f"The new sentence with every '{last_letter}', replaced by '@' is: ")
print(new_str + '\n')

# Printing the last 3 characters of str_manip backwards
print(f'The last 3 characters of your sentence backwards is: {str_manip[-1:-4:-1]}\n')

# Creating a five-letter word made up of the first three characters and last two characters of str_manip
five_letter_word = str_manip[:3] + str_manip[-2:]
print(f'''The five-letter word made up of the first three characters 
and last two characters of your sentence is: {five_letter_word}''')
