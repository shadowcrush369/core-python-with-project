# Exception handling
# iterables - iter(), next()
# File handling 
# Basic file operation
# Common functions in file handling

# =========================================
# EXCEPTION HANDLING
# =========================================
print("=== Exception Handling ===")
try:
    num = int(input("Enter a number: "))
    print(f"100 divided by your number = {100 / num}")
except ValueError:
    print("That's not a valid integer!")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This block runs no matter what.\n")

# =========================================
# ITERABLES, iter(), next()
# =========================================
print("=== Iterables, iter(), next() ===")
my_list = [10, 20, 30]
iterator = iter(my_list)  # Convert list to iterator

print(next(iterator))  # First element
print(next(iterator))  # Second element
print(next(iterator))  # Third element
# If we do next(iterator) again, it will raise StopIteration

# =========================================
# FILE HANDLING
# =========================================
print("\n=== File Handling ===")
# Basic file creation and writing
with open("sample.txt", "w") as file:
    file.write("Hello, file handling in Python!\n")
    file.write("Second line here.")

# Reading the file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# =========================================
# BASIC FILE OPERATIONS
# =========================================
print("\n=== Basic File Operations ===")
# Append to file
with open("sample.txt", "a") as file:
    file.write("\nThis line was appended.")

# Read again to see the change
with open("sample.txt", "r") as file:
    print("Updated content:\n", file.read())

# =========================================
# COMMON FUNCTIONS IN FILE HANDLING
# =========================================
print("\n=== Common File Functions ===")
with open("sample.txt", "r") as file:
    print("readline():", file.readline())  # Reads first line
    file.seek(0)  # Move pointer back to start
    print("readlines():", file.readlines())  # Reads all lines as a list

# Deleting a file (optional demo)
import os
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("sample.txt deleted.")
