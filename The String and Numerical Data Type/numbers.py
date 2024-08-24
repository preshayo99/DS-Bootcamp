# Ask user to input  3 different integers
integer1 = int(input('Please enter the first integer : '))
integer2 = int(input('Please enter the second integer : '))
integer3 = int(input('Please enter the third integer : '))

# Calculate sum of integers
answer_sum = integer1 + integer2 + integer3

# Calculate first number minus second
answer = integer1 - integer2

# Calculate third number multiplied by the first
answer_multiply = integer3 * integer1

# Calculate sum of integers divided by the third integer
answer_divide = (integer1 + integer2 + integer3)/integer3

# The calculations displayed
print(f'The sum of {integer1}+{integer2}+{integer3} = {answer_sum}')
print(f'The sum of {integer1} -{integer2}  = {answer}')
print(f'The answer to {integer3} multiplied by {integer1}  = {answer_multiply}')
print(f'The answer to {integer1}+{integer2}+{integer3} all divided by{integer3} = {answer_divide}')
