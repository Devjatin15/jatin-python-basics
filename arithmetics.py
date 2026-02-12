import math
friends = 0

# friends = friends + 1
friends += 1  # This is a shorthand for friends = friends + 1

# -=, *=, /=, //=, **= are also available for subtraction, multiplication, division, floor division and exponentiation respectively.
print(friends)


x = 2
y = 3.456
z = 3

# result = round(y) # Rounds the float to the nearest integer

# print(result)

# pow(), abs(), min(), max() are some of the built-in functions for mathematical operations.


print(math.pi)
print(math.sqrt(16))  # Square root of 16
print(math.ceil(2.3))  # Rounds up to the nearest integer


# radius = int(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle is: {circumference}")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sqrt = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of the hypotenuse is: {sqrt}")