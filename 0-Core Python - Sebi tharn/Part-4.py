# slicing lists
# copy() 
# The key word "del"
# The key word "in"
# + operator with list
# Tuples
# explain about CURD
# Rules in truple
# Packing & unpacking in tuple list
# Dictionaries (Not iterale, no enumerated index)


# =============================
# Python Concepts in One File
# =============================

# --- 1. Slicing Lists ---
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Slicing example:", fruits[1:4])   # banana to date
print("Slicing with step:", fruits[::2]) # every 2nd item

# --- 2. copy() ---
fruits_copy = fruits.copy()
fruits_copy.append("fig")
print("Original:", fruits)
print("Copy:", fruits_copy)

# --- 3. del keyword ---
del fruits_copy[0]  # removes first element
print("After del:", fruits_copy)

# --- 4. in keyword ---
print("'apple' in fruits?", "apple" in fruits)
print("'kiwi' in fruits?", "kiwi" in fruits)

# --- 5. + operator with lists ---
more_fruits = ["grape", "honeydew"]
combined = fruits + more_fruits
print("Combined list:", combined)

# --- 6. Tuples ---
colors = ("red", "green", "blue")
print("Tuple:", colors)

# --- 7. CRUD Example ---
# Create
numbers = [1, 2, 3]
# Read
print("Read:", numbers[1])
# Update
numbers[1] = 20
print("Updated list:", numbers)
# Delete
del numbers[0]
print("After delete:", numbers)

# --- 8. Rules in tuple ---
# Tuples are immutable: cannot change items after creation
# colors[0] = "yellow"  # ❌ This would cause an error

# --- 9. Packing & Unpacking in tuple ---
packed_tuple = 1, 2, 3
a, b, c = packed_tuple
print("Packed tuple:", packed_tuple)
print("Unpacked values:", a, b, c)

# --- 10. Dictionaries (not iterable by index) ---
person = {"name": "Alice", "age": 25, "city": "London"}
# print(person[0])  # ❌ Will give error
print("Dictionary keys:", list(person.keys()))

# --- 11. 'in' keyword in dictionaries ---
print("'name' in person?", "name" in person)
print("'Alice' in person?", "Alice" in person)  # Checks keys, not values

# --- 12. del keyword in dictionaries ---
del person["city"]
print("After del city:", person)

# --- 13. Packing & unpacking in dictionaries ---
dict_packed = dict(name="Bob", age=30)
name, age = dict_packed["name"], dict_packed["age"]
print("Packed dict:", dict_packed)
print("Unpacked:", name, age)
