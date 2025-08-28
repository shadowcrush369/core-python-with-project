# Funtion
# variables & collections
# Oops key concepts of oops -  class, object, encapulation, inheritance, polymorphism and abstraction
# lists - higher order function
# adding item to end list
# remove item to list
# appedn multiple values

# ----------Function----------
def greet(name):  # def → keyword to define a function | greet → function name | (name) → parameter
    return f"Hello {name}"  # returns a string using f-string formatting
print(greet("Ajay"))  # calls function with argument "Ajay"

# ----------Variables & Collections----------
age = 25  # int variable
price = 19.99  # float variable
name = "Ajay"  # string variable
is_active = True  # boolean variable
fruits = ["apple", "banana", "cherry"]  # list (mutable)
coordinates = (10, 20)  # tuple (immutable)
person = {"name": "Ajay", "age": 25}  # dictionary (mutable)

# ----------OOPS Key Concepts----------
# Class → Blueprint for creating objects
class Car:
    def __init__(self, brand, model):  # Constructor method
        self.brand = brand  # attribute
        self.model = model  # attribute
    def drive(self):  # Method
        print(f"{self.brand} {self.model} is driving")

# Object → Instance of a class
car1 = Car("Toyota", "Corolla")  # creates object
car1.drive()  # calls method

# Encapsulation → Restricting direct access to data
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance

# Inheritance → Child class inherits from parent class
class ElectricCar(Car):  # ElectricCar inherits from Car
    def charge(self):
        print(f"{self.brand} is charging")

# Polymorphism → Same method name works differently for different classes
class Bike:
    def drive(self):
        print("Bike is driving")

for vehicle in [Car("Ford", "Focus"), Bike()]:
    vehicle.drive()

# Abstraction → Hiding details using abstract classes
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# ----------Lists - Higher Order Function----------
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))  # map → applies function to each item
evens = list(filter(lambda x: x % 2 == 0, numbers))  # filter → keeps items meeting condition
total = sum(numbers)  # sum → adds all items

# ----------Adding item to end list----------
fruits = ["apple", "banana"]
fruits.append("cherry")  # append → adds one item to end

# ----------Remove item from list----------
fruits.remove("banana")  # remove → deletes first matching value
popped_item = fruits.pop()  # pop → removes last item (or index if given)

# ----------Append multiple values----------
fruits.extend(["mango", "grape"])  # extend → adds multiple items at once
