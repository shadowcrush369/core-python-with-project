# 1.Comments
# 2.Primitive_operators
# 3.Order_of_execution
# 4.Boolean
# 5.Comparision_operators
# 6.Channing_operators: GATES
# 7.Data_type

#----------1.Comments---------
Single_line = "single_line_Comment" # single line command

Multi_line = "Multi_line_Comment"  
"""
This is
Multi 
line 
Comment
"""

Short_cut_comments = "CTRL + /" #Drag all and ctral + /.

# ----------2.Primitive_operators----------
Add = 5 + 3          # Addition
Subtract = 10 - 4    # Subtraction
Multiply = 6 * 2     # Multiplication
Divide = 8 / 2       # Division (float)
Floor_Divide = 8 // 3  # Division (integer/floor)
Modulus = 10 % 3     # Remainder
Exponent = 2 ** 3    # Power

# ----------3.Order_of_execution----------
# boad mass rule: Brackets → Orders → Division/Multiplication → Addition → Subtraction
Order_Example = 2 + 3 * 4    # Multiplication first → 2 + 12 = 14
Order_Example2 = (2 + 3) * 4 # Brackets first → 5 * 4 = 20

# ----------4.Boolean----------
is_true = True
is_false = False
bool_expression = 5 > 3  # Returns True
bool_expression2 = 2 == 5  # Returns False

# ----------5.Comparision_operators----------
Equal = 5 == 5         # True
Not_Equal = 5 != 3     # True
Greater_Than = 7 > 4   # True
Less_Than = 3 < 8      # True
Greater_Equal = 5 >= 5 # True
Less_Equal = 2 <= 6    # True

# ----------6.Channing_operators: GATES----------
# Logical operators
AND_gate = (5 > 2) and (10 > 5)   # True and True → True
OR_gate = (5 > 10) or (10 > 5)    # False or True → True
NOT_gate = not (5 > 2)            # not True → False

# Example of chaining
Chained = 1 < 3 < 5  # True because 1 < 3 and 3 < 5

# ----------7.Data_type----------
data_int = 10                  # int
data_float = 3.14               # float
data_str = "Hello"              # string
data_bool = True                # boolean
data_list = [1, 2, 3]           # list
data_tuple = (1, 2, 3)          # tuple
data_set = {1, 2, 3}            # set
data_dict = {"a": 1, "b": 2}    # dictionary
