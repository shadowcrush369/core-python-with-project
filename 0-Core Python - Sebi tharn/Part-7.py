# Basic of - Function
# Function syntax
# Variable Scope
# First class Function 
# What is Instance
# Anonymous function
# map(), Filter()

# 1. Basics of Function
def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

print(greet("Alice"))


# 2. Function Syntax
def add(a, b):
    return a + b

print(add(5, 3))


# 3. Variable Scope
x = 10  # global

def scope_demo():
    x = 5  # local
    print("Inside function:", x)

scope_demo()
print("Outside function:", x)


# 4. First Class Function
def square(n):
    return n * n

func_var = square  # assigning function to variable
print(func_var(4))


# 5. What is Instance
class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
print(isinstance(dog1, Dog))  # True


# 6. Anonymous Function (lambda)
add_lambda = lambda a, b: a + b
print(add_lambda(4, 6))


# 7. map() and filter()
nums = [1, 2, 3, 4, 5]

# map() applies a function to each element
squares = list(map(lambda x: x ** 2, nums))
print(squares)

# filter() keeps only elements that satisfy a condition
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
