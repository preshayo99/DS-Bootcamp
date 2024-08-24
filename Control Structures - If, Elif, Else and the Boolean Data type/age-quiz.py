# Ask user to input their age
age = int(input('Please enter your age: '))

# Use if, elif and else function to define conditions given in task
if age < 13:
    print('You qualify for the kiddie discount!')
elif age == 21:
    print('Congrats on your 21st!')
elif age in range(40, 65):
    print('You are over the hill.')
elif age in range(65, 100):
    print('Enjoy your retirement!')
elif age >= 100:
    print('Sorry, you are dead.')
else:
    print('Age is but a number')



# I used the range function in line 9 and 11 because when I used >= it didn't pick up 'sorry you're dead'
# If I kept it with >=, if I was to put 101, it would say 'enjoy your retirement' and not 'sorry you're dead'

# big-small when using if,elif and else to allow each condition to range