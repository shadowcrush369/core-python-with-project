# Modules in Python
# Python package index
# what is import
# Two module function import
# How to create new module
# Class
# yeild
# Decorators
# Enumerate

# ================================
# Modules in Python
# ================================

# A module is simply a Python file containing definitions (functions, variables, classes)
# You can import modules to reuse their code

import math  # importing a built-in module
print(math.sqrt(16))  # using a function from math module

# ================================
# Python Package Index (PyPI)
# ================================
# PyPI is an online repository of Python packages (like libraries).
# You can install packages from PyPI using: pip install <package_name>

# Example (run in terminal, not in Python file):
# pip install requests

# ================================
# What is import
# ================================
# The 'import' keyword lets us bring other modules' code into our program.

import random
print(random.randint(1, 5))  # random number between 1 and 5

# ================================
# Two module function import
# ================================
# You can import specific functions from multiple modules

from math import ceil, floor
print(ceil(4.2))   # 5
print(floor(4.8))  # 4

# ================================
# How to create new module
# ================================
# 1. Create a Python file with functions, e.g., mymodule.py:
# def greet(name):
#     return f"Hello, {name}!"
#
# 2. Import it in your main script:
# import mymodule
# print(mymodule.greet("Alice"))

# ================================
# Class
# ================================

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

dog1 = Dog("Buddy")
print(dog1.bark())

# ================================
# yield
# ================================
# 'yield' makes a function a generator — it returns values one by one

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(3):
    print(number)  # prints 3, 2, 1

# ================================
# Decorators
# ================================
# A decorator changes or extends the behavior of a function without changing its code

def shout_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@shout_decorator
def say_hello():
    return "hello there"

print(say_hello())  # "HELLO THERE"

# ================================
# Enumerate
# ================================
# enumerate() gives both index and value when looping

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
