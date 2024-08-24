n = 5

# Outer for loop to create number of lines (9 in total)
for x in range(n * 2):

    # Pattern increase, if x is <= 5
    if x <= n:
        # Inner for loop creates number of * in each row
        for y in range(x):
            print('*', end='')

    # Pattern decrease, when x > 5
    else:
        for y in range(x, n * 2):
            print('*', end='')
    print()
