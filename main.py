# A playground for python programming.
# print("Hello World!")
# print("Welcome to the world of Python programming!")

# Variable: A container for a value of type integer, float, string, boolean.
# A variable behaves as if it was the value it contains.

# String
# first_name = "Shubham"
# last_name = "Sihasane"
# email = "shubhamsihasane101@gmail.com"
# print(f"Hey, {first_name} {last_name}")
# print(f"Your email is {email}")

# Integer
# age = 30
# print(f"You are  {age} years old.")
# quantity = 5
# print(f"You are buying {quantity} items.")
# num_students = 30
# print(f"Your class has {num_students} students.")

# Float
# price = 11.99
# gpa = 9.5
# km = 5.5
# print(f"The price of items is {price}")
# print(f"Your GPA is {gpa}")
# print(f"You ran {km} kilometers.")

# Boolean
# is_active = True
# print(f"You are {is_active}")
# is_live = False
# print(f"You are {is_live}")
#
# if is_active:
#     print(f"You are online 🍏")
# else:
#     print(f"You are offline 🍎")

# Typecasting - The process of converting a variable from one data type tp another.
# str(), float(), int() bool()

# name = "shubham sihasane"
# age = 30
# price = 11.99
# is_student = True
#
# print(f"The type of {name} is {type(name)}")
# print(f"The type of {age} is {type(age)}")
# print(f"The type of {price} is {type(price)}")
# print(f"The type of {is_student} is {type(is_student)}")
#
# print(f"The type of {bool(name)} is {type(bool(name))}")
# print(f"The type of {str(age)} is {type(bool(age))}")
# print(f"The type of {int(price)} is {type(int(price))}")
# print(f"The type of {float(is_student)} is {type(float(is_student))}")

# input() - A function that prompts the user to enter data.
# It returns the entered data as a string.

# name = input("Enter your name: ")
# print(f"Hey, {name}!")
# age = int(input("Enter your age: "))
# age = age + 1
# print(f"Happy Birthday! 🎂\nYou are {age} years old.")

# Calculate area of rectangle
# length = float(input("Enter length: "))
# breadth = float(input("Enter breadth: "))
# area = length * breadth
# print(f"The area of rectangle is {area}")

# Shopping Cart Program
# item = input("Enter the name of item: ")
# price = float(input("Enter the price of item: "))
# quantity = int(input("Enter the quantity of item: "))
#
# cart_total = price * quantity
# print(f"Your cart total is ${cart_total}")

# Indexing - Accessing elements of a sequence using indexing operator [] with [start:end:step]

# credit_number = "3525-6856-2436"
# print(credit_number)
# print(f"The value at first index is {credit_number[0]}")
# print(f"The value at last index is {credit_number[-1]}")
# print(f"The first four items are {credit_number[0:4]}")
# print(f"The first four items are {credit_number[:4]}")
# print(f"The first four items are {credit_number[4:-1]}")
# print(f"The first four items are {credit_number[4:]}")
# print(f"The last four items are {credit_number[-4:]}")
# print(f"The last items are {credit_number[:-1]}")
# print(f"The alternate items are {credit_number[::2]}")
# print(f"The reverse credit number is {credit_number[::-1]}")

# While Loop = Execute some code while some condition remains true

# name = input("Enter your name: ")
#
# while name == "":
#     name = input("Please enter your name: ")
# else:
#     print(f"Hello {name}")

# age = int(input("Enter your age: "))
#
# while age < 0:
#     print("Age can't be negative.")
#     age = int(input("Enter your age: "))
# print("Your age is:", age)

# magic = int(input("Enter a number: "))
# if magic <= 0 or magic >= 100:
#     print("Your number is out of range.")
# else:
#     print("Your are lucky.")

# For Loops:  Execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence etc.

