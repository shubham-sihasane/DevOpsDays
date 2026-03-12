# A sample python program to display a message on console
# print("Hello World!\nWelcome to the world of Python programming!")

# Variable = A variable is like a container for storing values of type number, float, string and boolean.
# A variable is a behaves as if it was the value it contains.

# # Strings
# first_name = "Shubham"
# last_name = "Sihasane"
# fruit = "Apple"
# email = "shubhamsihasane@example.com"
# print(first_name + " " + last_name)
# print(f"Hello {first_name}\nYou love {fruit}")
# print(f"You email address is {email}")
#
# # Numbers
# age = 25
# quantity = 3
# num_of_students = 50
# print(f"You are {age} years old.")
# print(f"You are buying {quantity} {fruit}/s")
# print(f"Your class is having {num_of_students} students.")
#
# # Float
# price = 10.99
# gpa = 9.5
# distance = 5.5
# print(f"The price of {fruit} is {price}")
# print(f"Your GPA is {gpa}")
# print(f"You ran a distance of {distance} kilometers.")
#
# # Boolean
# is_student = True
# print(f"Are you a student? {is_student}")
# if is_student:
#     print(f"You are a student.")
# else:
#     print(f"You are not a student.")
#
# is_online = True
# if is_online:
#     print(f"You are online 🍏")
# else:
#     print(f"You are offline 🍎")

# Type Casting = The process of converting a type of variable from one type to another.
# Type casting functions = str(), int(), float(), bool()

# full_name = "shubham sihasane"
# age = 25
# gpa = 8.5
# is_student = True
#
# print(f"The type of {full_name} is: {type(full_name)}")
# print(f"The type of {age} is {type(age)}")
# print(f"The type of {gpa} is {type(gpa)}")
# print(f"The type of {is_student} is {type(is_student)}")
#
# print(f"Type cast integer {age} to float = {str(age)}")
# print(f"Type cast float {gpa} to integer = {int(gpa)}")
# print(f"Type cast boolean {is_student} to string = {float(is_student)}")
# print(f"Type cast string {full_name} to boolean = {bool(full_name)}")

# input() = A function that prompt the user to enter the data and returns the entered data as string

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hey, Your name is {name} and you are {age} years old.")

# Are of rectangle
# length = float(input("Enter the length of the rectangle: "))
# breadth = float(input("Enter the breadth of the rectangle: "))
# area = length * breadth
# print(f"The area of the rectangle is {area}cm²")

# Shopping cart program
# item = input("What item would you like to buy? ")
# price = float(input("What is the price of the item? "))
# quantity = int(input("How many items you want? "))
#
# total_price = price * quantity
#
# print(f"The total price of the cart is {total_price}")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# print(f"Addition of {num1} + {num2} = {num1+num2}")
# print(f"Subtraction of {num1} - {num2} = {num1 - num2}")
# print(f"Multiplication of {num1} * {num2} = {num1 * num2}")
# print(f"Division of {num1} / {num2} = {num1 / num2}")
# print(f"Remainder of {num1} % {num2} = {num1 % num2}")
# print(f"Integer Division of {num1} // {num2} = {num1 // num2}")
# print(f"Pow of {num1} ^ {num2} = {num1 ** num2}")

# a = 3.14
# b = 10
# c = 25.25
#
# print(f"Round of {a} = {round(a)}")
# print(f"Absolute value of {a} = {abs(a)}")
# print(f"Power of {a} = {pow(a, 2)}")
# print(f"Maximum of {a}, {b}, {c} = {max(a, b, c)}")
# print(f"Minimum of {a}, {b}, {c} = {min(a, b, c)}")

# import math
# x = 9.254
# print(f"The value of PI is {math.pi}")
# print(f"The value of e is {math.e}")
# print(f"The square root of {x} is {math.sqrt(x)}")
# print(f"The square of {x} is {math.pow(x, 2)}")
# print(f"The ceil of {x} is {math.ceil(x)}")
# print(f"The floor of {x} is {math.floor(x)}")
# print(f"The round of {x} is {round(x, 2)}")

# import math
# Calculate circumference of circle
# radius = float(input("Enter a radius: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle is {circumference:.2f}")

# Calculate area of circle
# radius = float(input("Enter radius: "))
# area = math.pi * radius * radius
# print(f"The area of the circle is {area:.2f}")

# Calculate the third side of a right-angled triangle
# side1 = float(input("Enter the length of the first side: "))
# side2 = float(input("Enter the length of the second side: "))
# side3 = math.sqrt(pow(side1, 2) + pow(side2, 2))
# print(f"The length of the third side is {side3:.2f}")

# IF & Else Statement
# Execute some piece of code only if condition is True, else execute some another piece of code

# age = int(input("Enter your age: "))
# if age > 100:
#     print("You should die now.")
# elif age >= 18:
#     print("You can vote.")
# elif age < 0:
#     print("You haven't been born yet.")
# else:
#     print("You can not vote.")

# response = input("Would you like to order food? (y/n) : ")
# if response == "y":
#     print("You must become atmanirbhar.")
# else:
#     print("Why you living man.")

# name = input("Enter your name: ")
# if name == "":
#     print("Please enter your name: ")
# else:
#     print(f"Hey, {name}")

# for_sale = True
# if for_sale:
#     print("Item is for sale.")
# else:
#     print("Item is not for sale.")

# Python Calculator
# operator = input("Enter an operator:\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\nEnter your choice: ")
# num1 = float(input("Enter a number 1: "))
# num2 = float(input("Enter a number 2: "))
#
# if operator == "1":
#     result = num1 + num2
#     print(f"The result of {num1} + {num2} is {result}")
# elif operator == "2":
#     result = num1 - num2
#     print(f"The result of {num1} - {num2} is {result}")
# elif operator == "3":
#     result = num1 * num2
#     print(f"The result of {num1} * {num2} is {result}")
# elif operator == "4":
#     result = num1 / num2
#     print(f"The result of {num1} / {num2} is {result}")
# else:
#     print("Invalid operator")

# Temperature conversion program
# unit = input("Is this temperature is in celsius or fahrenheit? (c/f): ")
# temp = float(input("Enter temperature: "))
# if unit == "c" or "C":
#     fahrenheit = temp * 9 / 5 + 32
#     print("Fahrenheit: ", fahrenheit)
# elif unit == "f" or "F":
#     celsius = (temp - 32) * 5 / 9
#     print("Celsius: ", celsius)
# else:
#     print("Enter a valid unit.")

# Logical Operators: Evaluate multiple conditions (and, or, not)
# and = Both conditions must be true
# or = At least one condition must be true
# not = Inverts a condition (not False = True)

# temp = 40
# is_raining = False
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is canceled.")
# else:
#     print("The outdoor event is on time.")

# temp = 25
# is_sunny = False
#
# if temp >= 25 and is_sunny:
#     print("It is hot outside.🥵")
# else:
#     print("It is cool.🥶")

# status = True
# if not status:
#     print("Please stop 🍎.")
# else:
#     print("Please go 🍏.")

# Conditional Expression = A one line shortcut for the if else statement (Ternary Operator)
# Print or assign one of two values based on a condition = X if condition Y
# num = 10
# x = 5
# y = 25
# print("Positive" if num > 0 else "Negative")
# print("Even" if num % 2 == 0 else "Odd")
# result = x if x > y else y
# print(f"Maximum number is {result}")
# result = x if x < y else y
# print(f"Minimum number is {result}")

# name = input("Enter your name: ")
# phone_no = input("Enter your phone number: ")
# print(f"The length of {name} is {len(name)}")
# print(f"The first occurrence of {name.find('b')}")
# print(f"The last occurrence of {name.rfind('b')}")
# print(f"The capitalized name is {name.capitalize()}")
# print(f"The uppercase name is {name.upper()}")
# print(f"The lowercase name is {name.lower()}")
# print(f"Is it digit {name.isdigit()}")
# print(f"Is alphanumeric {name.isalnum()}")
# print(f"Total count of character is {phone_no.count('7')}")
# print(f"Replace 7 with 9 = {phone_no.replace('7', '9')}")
# print(help(str))

# username = input("Enter your username: ")
# if len(username) > 12:
#     print("Your username is too long.")
# elif len(username) < 3:
#     print("Your username is too short.")
# elif not username.find(' ') == -1:
#     print("Your username should not contain spaces.")
# elif not username.isalnum():
#     print("Your username should not container numbers.")
# else:
#     print("Your username is valid.")

# Indexing - Accessing elements of a sequence using [] (indexing operator, start : end : step)

# credit_number = "1234-5678-9012-3456"
# print(credit_number)
# print(credit_number[0])
# print(credit_number[-1])
# print(credit_number[5:])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[::2])
# print(credit_number[::-1])

# price1 = 3.1459
# price2 = -987.65657

# print(f"Price 1 is {price1:.1f}")
# print(f"Price 2 is {price2:.2f}")

# While loop = Execute some code while some condition remains true

# name = input("Enter your name: ")
# while name == "":
#     print("Please enter your name: ")
#     name = input("Enter your name: ")
# else:
#     print("Hello " + name)

# age = int(input("Enter your age: "))
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old.")

# num = int(input("Enter  a number between 1 to 10: "))
# while num < 1 or num > 10:
#     print(f"{num} is not a valid number.")
#     num = int(input("Enter  a number between 1 to 10: "))
# print(f"Your lucky number is {num}")

# Python compound interest calculator
# principle = 0
# roi = 0
# time = 0
#
# while True < 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle cannot be less than zero.")
#     else:
#         break
#
# while roi < 0:
#     roi = float(input("Enter the rate of interest: "))
#     if roi < 0:
#         print("Rate of interest cannot be less than zero.")
#     else:
#         break
#
# while time <= 0:
#     time = float(input("Enter the time amount: "))
#     if time <= 0:
#         print("Time cannot be less than zero.")
#     else:
#         break
#
# total = principle * pow((1 + roi / 100), time)
# print(f"Balance after {time} year/s = ${total:.2f}")

# For Loops = Execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence etc.

# for x in range(1, 11):
#     print(x, end = ' ')
# print("End of Loop")
#
# for x in reversed(range(1, 11)):
#     print(x, end = ' ')
# print("End of Loop")
#
# for x in range(0,20,2):
#     print(x, end = ' ')
# print("End of Loop")
#
# credit_number = '1234-5678-9012-3456-7890'
# for x in credit_number:
#     print(x, end = ' ')
# print("End of Loop")
#
# for x in range(0,21):
#     if x == 13:
#         print("Skipping...")
#         continue
#     else:
#         print(x, end = ' ')
# print("End of Loop")

# import time
# time.sleep(1)
# print("Time is over.")
#
# my_time = int(input("Enter the time in seconds: "))
# for x in range(0, my_time):
#     print(x)
#     time.sleep(3)

# my_time = int(input("Enter the time in seconds: "))
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = x // 60
#     hour = x // 3600
#     print(f"{hour:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# Nested Loops = A loop within another loop (outer, inner)
# for x in range(1,11):
#     print()
#     for y in range(1,11):
#         print(f"{x} x {y} = {x*y}")

# Collection = Single variable used to store multiple values
# List = [] ordered and changeable. Duplicate OK
# Set = {} unordered and immutable, No duplicate, but Add/Remove OK
# Tuple = () ordered and unchangeable. Duplicates OK, Faster
# Dictionary = {}

## List
# fruits = ['apple', 'banana', 'coconut', 'banana']
# print(fruits[0])
# print(fruits[-1])
# print(fruits[::-1])
# for fruit in fruits:
#     print(f"I like {fruit}")
# print(f"The number of fruits is: {len(fruits)}")
# print(f"Apple is available = {'apple' in fruits}")
# fruits.append('pineapple')
# print(fruits)
# fruits.remove('apple')
# fruits.insert(0, 'strawberry')
# print(fruits)
# fruits.sort()
# fruits.reverse()
# print(fruits)
# print(fruits.index("banana"))
# print(f"The counts of banana is {fruits.count("banana")}")
# fruits.clear()
# print(dir(fruits))
# print(help(fruits))

# friends = {'shubham','manoj','prasanna','rashmi','vrushali','vedika','gargi'}
# print(dir(friends))
# print(help(friends))
# print(fruits)
# print(len(friends))
# print('shubham' in friends)
# friends.add('omkar')
# friends.remove('shubham')
# friends.pop()
# friends.clear()
# print(friends)

# languages = {'english','marathi','hindi','gujarati','tamil'}
# print(dir(languages))
# print(help(languages))
# print(languages)
# print(len(languages))
# print('english' in languages)
# print(languages.add('mallu'))
# print(languages.remove('mallu'))
# print(languages)

# Shopping Cart
# foods = ['']
# prices = []
# total = 0
#
# while True:
#     food =input("Enter food: (q to quit) ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of {food}: "))
#         foods.append(food)
#         prices.append(price)
#
# print("----- Your Cart -----")
# for food in foods:
#     print(food)
#
# for price in prices:
#     total = total + price
#
# print(f"Total price is ${total:.2f}")

# fruits = ['apple', 'banana', 'coconut', 'banana']
# vegetables = ['carrots', 'potatoes', 'celery']
# meats = ['chicken', 'fish', 'turkey']

# groceries = [fruits, vegetables, meats]
# print(groceries[1][2])
# for collection in groceries:
#     for food in collection:
#         print(food, end=' ')
#     print()

# num_pad = (
#             (1, 2, 3),
#             (4, 5, 6),
#             (7, 8, 9),
#             ('*', 0, '#')
#         )
#
# for row in num_pad:
#     for col in row:
#         print(col, end=' ')
#     print()

# Python Quiz Game

# questions = ("How many elements are in the periodic table? ",
#              "Which animal lays the largest eggs? ",
#              "What is the most abundant gas in Earth's atmosphere? ",
#              "How may bones are there in human body? ",
#              "Which planet in the solar system is hottest? ")
# options = (
#             ('A','B','C','D'),
#             ('A','B','C','D'),
#             ('A','B','C','D'),
#             ('A','B','C','D')
#         )
# answers = ('C', 'A', 'D','B')
# guesses = []
# question_num = 0
#
# for question in questions:
#     print("--------------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#     guess = input("Enter your guess: (A, B, C, D) ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         print("You guessed the answer!")
#     else:
#         print("Sorry, you did not guess the answer!")
#         print(f"{answers[question_num]} is the correct answer!")
#     question_num += 1

# Dictionary = A collection of {key:value} pairs, ordered and changeable. No duplicates

# capitals = {
#     "India": "New Delhi",
#     "China": "Beijing",
#     "Russia": "Moscow"
# }
#
# print(dir(capitals))
# print(help(capitals))
# print(capitals)
# print(capitals["India"])

# if capitals.get("India"):
#     print("It Exists.")
# else:
#     print("It does not exist.")

# capitals.update({"Germarny": "Berlin"})
# print("capitals: ", capitals)
# capitals.pop("China")
#
# print("capitals: ", capitals)
# capitals.clear()
# print("capitals: ", capitals)

# keys = capitals.keys()
# for key in keys:
#     print(key)

# items = capitals.items()
# for key, value in items:
#     print(f"{key}: {value}")

# Concession Stand program
# menu = {"Pizza": 3.00,
#         "Burger": 5.00,
#         "Soda": 3.00,
#         "Orange": 6.00,
#         "Lemondade": 4.00,
#         "Chips": 9.00
#         }
#
# cart = []
# total = 0
#
# print("-------MENU-------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("------------------")
#
# while True:
#     choice = input("Please enter your choice: q to quit: ")
#     if choice == "q":
#         break
#     elif menu.get(choice) is not None:
#         cart.append(choice)
#
# print("-----YOUR CART------")
# for choice in cart:
#     total = total + menu.get(choice)
#     print(choice, end=" ")
#
# print()
# print(f"Total: {total:.2f}")

import random

# print(help(random))

# low = 1
# high = 100
# options = ('rock', 'paper', 'scissors')
# cards = ["4", "7", "9", "2", "6", "5" ]
# number = random.randint(low, high)
# print(number)
# number = random.random()
# print(number)
# option = random.choice(options)
# print(option)
# random.shuffle(cards)
# print(cards)

# Python number guessing game
# import random
# low_num = 1
# high_num = 100
# answer = random.randint(low_num, high_num)
# guesses = 0
# is_running = True
# print("Python Number Guessing Game")
# print(f"Select a number between {low_num} and {high_num}: ")
# while is_running:
#     guess = input("Guess a number: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess < low_num or guess > high_num:
#             print("Your guess is out of the range.")
#             print(f"Select a number between {low_num} and {high_num}: ")
#         elif guess < answer:
#             print("Your guess is too low.")
#         elif guess > answer:
#             print("Your guess is too high.")
#         else:
#             print("Your guess is correct.")
#             print(f"You guessed {guesses} times.")
#             is_running = False
#     else:
#         print("Invalid input, please try again.")
#         print(f"Select a number between {low_num} and {high_num}: ")

# Rock, Paper, Scissors Game
# import random
# options = ("rock", "paper", "scissors")
# running = True
#
# while running:
#     player = None
#     computer = random.choice(options)
#
#     while player not in options:
#         player = input("Enter your choice: Rock, Paper, Scissors: ")
#     print(f"Player: {player}")
#     print(f"Computer: {computer}")
#
#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")
#
#     play_again = input("Do you want to play again? (y/n): ")
#     if not play_again.lower() == "y":
#         running = False
#
# print("Thank you for playing!")

# Function - A block of reusable code, place() after the function name to invoke it

# def wish(name):
#     print("Happy Birthday!", name)
#
# wish("Shubham")
# wish("Vrushali")
# wish("Rashmi")

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:2f} is due: {due_date}")
#
# display_invoice("Shubham", 100.10, "01/02/2025")

# Return = statement used to end a function and send a result back to the caller.
# def add(x, y):
#     z = x + y
#     return z
# def subtract(x, y):
#     z = x - y
#     return z
# def multiply(x, y):
#     z = x * y
#     return z
# def divide(x, y):
#     z = x / y
#     return z
#
# print(add(5,7))
# print(subtract(5,7))
# print(multiply(5,7))
# print(divide(5,7))

# def create_name(firstname, lastname):
#     first_name = firstname.capitalize()
#     last_name = lastname.capitalize()
#     return f"{first_name} {last_name}"
#
# full_name = create_name("shubham", "sihasane")
# print(f"Your full name is {full_name}")

# Default Arguments = A default value for certain parameters,
# default is used when that argument is omitted,
# make your function more flexible, reduces # of arguments
# 1. Positional, 2. Default 3. Keyboard 4. Arbitrary

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)
# print(f"Your net price is {net_price(50, 0.2, 0.01)}")

# import time
# def count(start, end):
#     for num in range(start, end+1):
#         print(num)
#         time.sleep(1)
#     print("Done!")
# count(0,10)

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")
#
# hello(title="Mr.", first="Shubham", last="Sihasane", greeting="Hello")

# print("1", "2", "3", "4", "5", sep="=")

# def get_phone(country, first, last):
#     return f"{country}+{first}_{last}"
#
# phone_num = get_phone(country=91, first="77578", last="96762")
# print(phone_num)

# *Args = Allows you to pass multiple non-key arguments
# **kwargs = Allows you to pass multiple keyword arguments
# * unpacking operator

# def add(*args):
#     total = 0
#     for arg in args:
#         total = total + arg
#     return total
#
# print(f"The sum of numbers is =", add(1,2,3,4,5,6,7,8,9))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Mr.", "Shubham", "Sihasane")

# def print_address(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_address("Mr.", "Shubham", "Sihasane", street="Galaxy Road", city="Pune", state="MH", country="India")

# Iterables = An object and collection that can return its elements one at a time,
# allowing it to be iterated over in a loop

