import math
'''
This program is a financial calculator. 

It allows user to calculate how much their investment and bond would be after a certain time frame. 
Users can choose to calculate investment with either simple or compound interest.
'''
investment = 'investment'
bond = 'bond'

# Menu options:
print('\nInvestment - to calculate the amount of interest you will earn on your investment')
print('Bond - to calculate the amount you will have to pay on a home loan')

# User inputs their selection
option = input('\nEnter either "investment" or "bond" from the menu above to proceed: ').lower()

if option == investment:
    # Investment calculation
    interest_type = input('Enter either "simple" or "compound": ').lower()
    principal = float(input('\nEnter the Principal amount: '))
    time = float(input('Enter the number of years you plan on investing: '))
    rate = float(input('Enter the rate of interest: '))

    # Formula to calculate simple and compound investment
    simple_interest = principal * (1 + time * (rate / 100))
    compound_interest = principal * math.pow((1 + (rate / 100)), time)

    if interest_type == 'simple':
        print(f'After {time} years, you will earn £{round(simple_interest, 2)} in interest.')

    elif interest_type == 'compound':
        print(f'\nAfter {time} years, you will earn £{round(compound_interest, 2)} in interest')

    else:
        print('Invalid option, try again.')

elif option == bond:
    # Bond repayment calculation
    principal = float(input('\nEnter the principal amount: '))
    n = int(input('Please enter number of months: '))
    rate = float(input('Enter the rate of interest: '))
    monthly_rate = (rate / 100) / 12
    bond_repayment = (monthly_rate * principal) / (1 - (1 + monthly_rate) ** (- n))
    print(f'\nYou will repay £{round(bond_repayment, 2)} each month for {n} months towards your home loan.')

else:
    print('Invalid option, try again.')
