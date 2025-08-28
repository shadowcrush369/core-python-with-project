# Module
# Class
# Defination oops
# Object

# mymodule.py
# This file is a Module because it contains Python code we can reuse.

# ---- Class ----
class Car:
    """A simple example of OOP using a Car class."""
    
    def __init__(self, brand, color):
        # Attributes (data)
        self.brand = brand
        self.color = color
    
    # Method (behavior)
    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

# ---- Object ----
if __name__ == "__main__":
    # Creating two objects (instances of Car class)
    car1 = Car("Toyota", "Red")
    car2 = Car("Tesla", "Black")

    # Using object methods
    car1.drive()
    car2.drive()
