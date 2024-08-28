menu = ['Cake', 'Toast', 'Coffee', 'Soup']

# Create a dictionary for the prices of each item
stock = {
    'Cake': 1,
    'Toast': 13,
    'Coffee': 4,
    'Soup': 10
}

# Create a dictionary for the prices of each item
price = {
    "Cake": 2.5,
    "Toast": 3.0,
    "Coffee": 3.5,
    "Soup": 4.0
}

# Calculate the total stock worth
total_stock = sum(stock[item] * price[item] for item in menu)

# Print the results -- after 3 hrs break - too many scares we have this week
print("Menu:")
for item in menu:
    print(f"{item}: £{price[item]:.2f}")

print("\nStock:")
for item, value in stock.items():
    print(f"{item}: {value} units")

print(f"\nTotal Stock Worth: £{total_stock :.2f}")