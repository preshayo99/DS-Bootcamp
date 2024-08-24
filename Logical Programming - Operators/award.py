# Ask user to enter the time taken to complete each race
swimming = float(input('Please enter the total time taken to complete swimming: '))
cycling = float(input('Please enter the total time taken to complete cycling: '))
running = float(input('Please enter the total time taken to complete running: '))

# Calculate the total time and then print statement
total_time = swimming + cycling + running
print(f'\nYou have completed the triathlon in {total_time} minutes')

# Use if, elif and else function to define qualifying criteria given in task
if total_time >= 110:
    print('Award given: No award')
elif total_time in range(106, 110):
    print('Award given: Provincial Scroll')
elif total_time in range(101, 106):
    print('Award given: Provincial Half Colours')
elif total_time in range(0, 101):
    print('Award given: Provincial Colours')
else:
    print('N/A')

# Compared to task 3, I started from the highest value (time in this case) to allow each condition to run
