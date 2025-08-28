# What is hashing 
# "in" keyword in dictionaries
# "del" keyword in dictionaries
# Packing and unpacking in dictionaries
# set (Not iterable)
# Sets operators

# ===============================
# What is Hashing
# ===============================
# Hashing is the process of converting data (like strings) into a fixed-size value (hash) 
# using a hash function. Dictionaries and sets in Python use hashing internally to 
# store and quickly access elements.
# Example: the built-in hash() function
text = "apple"
print("Hash value of 'apple':", hash(text))  # Returns an integer hash value

# ===============================
# "in" keyword in dictionaries
# ===============================
# Used to check if a key exists in the dictionary (not the value).
my_dict = {"name": "Alice", "age": 25}
print("'name' in my_dict?", "name" in my_dict)     # True (key exists)
print("'Alice' in my_dict?", "Alice" in my_dict)   # False (values are not checked by default)

# ===============================
# "del" keyword in dictionaries
# ===============================
# Deletes a key-value pair from a dictionary.
del my_dict["age"]
print("After deleting 'age':", my_dict)

# ===============================
# Packing and unpacking in dictionaries
# ===============================
# Packing: Creating a dictionary from key-value pairs.
packed_dict = dict(name="Bob", age=30, city="Paris")

# Unpacking: Using ** to unpack dictionary items into function arguments.
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

display_info(**packed_dict)  # Unpacks the dictionary into separate arguments

# ===============================
# Sets (Not indexable / Not iterable by index)
# ===============================
# Sets store unordered, unique elements. You can't access elements by index like in lists.
my_set = {1, 2, 3, 4}
# print(my_set[0])  # ❌ This would cause an error
for item in my_set:   # ✅ You can still iterate over them in a loop
    print("Set item:", item)

# ===============================
# Set Operators
# ===============================
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union:", set_a | set_b)          # {1, 2, 3, 4, 5}
print("Intersection:", set_a & set_b)   # {3}
print("Difference:", set_a - set_b)     # {1, 2}
print("Symmetric Difference:", set_a ^ set_b)  # {1, 2, 4, 5}
