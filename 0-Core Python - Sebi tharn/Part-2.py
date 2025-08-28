#-----Data type memory management-----
# Mutable Data type
# Immutable Data type

# ----------Data type memory management----------

# Mutable Data type
# (Can be changed after creation without changing memory address)
mutable_list = [1, 2, 3]
print(id(mutable_list))   # Memory address before change
mutable_list.append(4)    # Change the list
print(id(mutable_list))   # Same memory address (mutable)

mutable_dict = {"a": 1, "b": 2}
print(id(mutable_dict))
mutable_dict["c"] = 3
print(id(mutable_dict))   # Same memory address (mutable)

# Immutable Data type
# (Cannot be changed after creation — a new memory address is created)
immutable_int = 10
print(id(immutable_int))  # Memory address before change
immutable_int += 5        # Creates a new object in memory
print(id(immutable_int))  # Different memory address (immutable)

immutable_str = "Hello"
print(id(immutable_str))
immutable_str += " World"
print(id(immutable_str))  # Different memory address (immutable)

immutable_tuple = (1, 2, 3)
print(id(immutable_tuple))
immutable_tuple += (4,)
print(id(immutable_tuple))  # Different memory address (immutable)
