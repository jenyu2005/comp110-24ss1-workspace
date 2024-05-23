"""Practice with Expressions- 5/17/24!"""

print("Adding incompatible types:")
# "Hello" + 1 (Error- need another string, not integer)

# print(3 * "Hello") and print("Hello" * 1) is the same value
# Division always result in a float

# Relational Operators (uses < , > , <= , >=, etc)- ALWAYS result in True or False

"""Variables!"""
# Declaration of a variable (A: B = C)
# A: name of variable
# B: type of datatype
# C: value

"""Example!!!!"""
# Example of declaring a variable
name: str = "Jennifer"

# Accessing and printing a variable
print(name)

# Updating variable
name = "Dr. Jennifer Yu"
print(name)

# Multiplying string by two
print(name * 2)

"""Example 2!!!!"""
# Numerical variables
trail_a: int = 1
trail_b: int = 3
print(trail_a + trail_b)
# will print out 4

# Changing variable name to total_miles
total_miles: int = trail_a + trail_b
print(total_miles)
# will print out 4 (same)

"""User Input:"""
# input("What's your favorite color?")
# Question what you want to ask- results in a type in box (answer the question)

"""Stored input as a variable"""
fav_color: str = input("What's your favorite color?")
print(fav_color + "is a cool color!")

lucky_number: int = int(input("What's your lucky number?"))
my_number: int = lucky_number + 1
print("My lucky number is" + str(my_number))
