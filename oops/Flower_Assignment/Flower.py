#lex_auth_012727119215337472135
#Start writing your code here
# Royal Orchid is a florist. They want to be alerted when stock of a flower goes below a particular level. 
# The flowers are identified using name, price per kg and stock available (in kgs).
# Write a Python program to implement the above requirement.

# Details of Flower class are given below:

# Class name: Flower

# Attributes
# (private)

# flower_name
# price_per_kg
# stock_available

 

# Methods
# (public)

# __init__()

# Create and initialize all instance variables to None

# validate_flower()

# Return true, if flower name is valid. Else, return false
# (Refer table for valid flower names)

# validate_stock(required_quantity)

# Accept the quantity required. Return true, if stock is available.
# Else return false.

# sell_flower(required_quantity)

# Accept the quantity required.
# Validate flower name and stock.
# If both are valid, update stock available based on the quantity required

# check_level()

# Check if available stock is below the order level
# If so, return true. Else, return false
# (Refer table for order level of each flower)

# setter methods

# Include setter methods for all instance variables to set its values

# getter methods

# Include getter methods for all instance variables to get its values

 

 

# Flower Name

# Level(in Kgs)

# Orchid

# 15

# Rose

# 25

# Jasmine

# 40

# Note: Perform case insensitive string comparison
# Represent few flowers, initialize instance variables using setter methods, invoke appropriate methods and test your program.

class Flower:
    def __init__(self,flower_name,price_per_kg,stock_available):
        self.__flower_name=flower_name
        self.__price_per_kg=price_per_kg
        self.__stock_available=stock_available

    def get_flower_name(self):
        return self.__flower_name
    def get_price_per_kg(self):
        return self.__price_per_kg
    def get_stock_available(self):
        return self.__stock_available
    
    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name
    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available

    def validate_flower(self):
        valid_flower=["orchid","rose","jasmine"]
        return self.__flower_name.lower() in valid_flower

    def validate_stock(self,required_quantity):
        return self.__stock_available >= required_quantity

    def sell_flower(self,required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available -= required_quantity
        else:
            return "sale cannot take place has stock not available"
        
    def check_level(self):
        reorder_level={
            "orchid":15,
            "rose":25,
            "jasmine":40
        }
        flower=self.__flower_name.lower()
        if flower in reorder_level:
            return self.__stock_available < reorder_level[flower]
        return False