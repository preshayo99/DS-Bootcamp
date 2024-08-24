# Ask user to enter the lengths of three sides of a triangle
import math

side1 = float(input('Please enter length one : '))
side2 = float(input('Please enter length two : '))
side3 = float(input('Please enter length three : '))

# Calculate semi-perimeter
s = (side1 + side2 + side3)/2

# Calculate area of triangle using the semi-perimeter
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

# Print area of triangle
print(f"The area of the triangle is '{round(area, 2)}'cm^2")
