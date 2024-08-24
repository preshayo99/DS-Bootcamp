"""

This loop asks users to input any number.
To exit the loop the user has to enter -1.
The program will calculate the average of the entered value and print the output.
The average is not inclusive of the -1 entered.

"""

total = 0
count = 0

print('This program calculates the average of any number given. Enter -1 to exit the program.')

# Start of loop asking user to input values
while True:
    try:
        user_number = float(input('Please enter a number: '))

        # The If block adds the values entered together whilst counting the number of values inputted by user
        if user_number != -1:
            total += user_number
            count += 1
            continue

        if user_number == -1:
            # Calculate the average of the entered numbers
            average = total / count
            print(f"The average of the numbers entered is: {average:.2f}")
        else:
            print("No numbers entered. Exiting program.")
        break

# The except clause is triggered when user enters no value or any string characters
    except ValueError:
        print('Error - Please enter a valid number.')
    break
