# Problem Statement
# WeCare insurance company wants to calculate premium of vehicles.
# Vehicles are of two types – "Two Wheeler" and "Four Wheeler". Each vehicle is identified by vehicle id, type, cost and premium amount.
# Premium amount is 2% of the vehicle cost for two wheelers and 6% of the vehicle cost for four wheelers. Calculate the premium amount and display the vehicle details.

# Identify the class name and attributes to represent vehicles. 

# calculate_premium()
# vehicle_cost
# TwoWheeler
# vehicle_type
# vehicle_id
# Vehicle
# premium_amount
# FourWheeler
# premium_percentage
# calculate_vehicle_cost()
# __init__()
# display_vehicle_details()
# Write a Python program to implement the class chosen with its attributes and methods.

# Note:

# Consider all instance variables to be private and methods to be public
# Include getter and setter methods for all instance variables
# Display appropriate error message, if the vehicle type is invalid
# Perform case sensitive string comparison
# Represent few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.


class Vehicle:
    def __init__(self, vehicle_type, vehicle_id, vehicle_cost):
        self.__vehicle_type = vehicle_type
        self.__vehicle_id = vehicle_id
        self.__vehicle_cost = vehicle_cost
        self.__premium_amount = None
    
    def get_vehicle_type(self):
        return self.__vehicle_type
        
    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type
        
    def get_vehicle_id(self):
        return self.__vehicle_id
        
    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id
        
    def get_vehicle_cost(self):
        return self.__vehicle_cost
        
    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost
        
    def get_premium_amount(self):
        return self.__premium_amount
        
    def set_premium_amount(self, premium_amount):
        self.__premium_amount = premium_amount
        
    def calculate_premium(self):
        if self.__vehicle_type == "TwoWheeler":
            self.__premium_amount = 0.02 * self.__vehicle_cost
        elif self.__vehicle_type == "FourWheeler":
            self.__premium_amount = 0.06 * self.__vehicle_cost
        
    def display_vehicle_details(self):
        # Fixed spelling error from "VECHILE" to "VEHICLE"
        print(f"THE VEHICLE TYPE IS : {self.__vehicle_type}")
        print(f"THE vehicle_id IS : {self.__vehicle_id}")
        print(f"vehicle_cost IS : {self.__vehicle_cost}")
        print(f"THE premium_amount is : {self.__premium_amount}")
        print("\n")  # Added newline for clarity  # Change here
        
# Create instances of Vehicle
obj1 = Vehicle("TwoWheeler", 101, 105000)
obj2 = Vehicle("FourWheeler", 202, 200000)
print("\n") 

# Print vehicle type for both objects
print(obj1.get_vehicle_type())
print(obj2.get_vehicle_type())
print("\n") 

# Calculate premiums
obj1.calculate_premium()
obj2.calculate_premium()

# Display details for both vehicles
obj1.display_vehicle_details()
obj2.display_vehicle_details()

# Print premium amounts for both objects
print(obj1.get_premium_amount())
print(obj2.get_premium_amount())
