# Jason Gibson
# 10/12/2026
# P2LAB1
# using raduis to calculate diamiter


import math

# Get the radius from the user as a float
radius = float(input("What is the radius of the circle? "))

# Calculate the values
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display the results with the required decimal places
print()
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")