# Problem Statement
# A toll booth on the way to Bangalore wants to keep the track of the number of vehicles passed through it and total amount collected by them.
# Write a python program to implement the class diagram given below.

                                 

# Class description:
# Constructor: Initialize both the instance variables, no_of_vehicle, total_amount to 0

# count_vehicle(): Increment total number of vehicle by 1
# calculate_amount(vehicle_type): Accept vehicle type and identify toll amount for that vehicle based on details given in the table. Add it to the total_amount instance variable.
# collect_toll(owner_type,vehicle_type): Accept owner type and vehicle type of the vehicle for which toll should be collected.
# If the owner of the vehicle is a "VIP", then toll amount need not be collected but number of vehicles should be updated.
# For any other type of owner, calculate the toll amount and update the number of vehicles.
# (Hint: Invoke appropriate methods to complete the functionality)
# Perform case insensitive string comparison.
# Create an object of Tollbooth class, invoke collect_toll() method for different vehicles and test your program.

class Tollbooth:
    def __init__(self):
        self.no_of_vehicle = 0
        self.total_amount = 0

    def count_vehicle(self):
        self.no_of_vehicle += 1

    def calculate_amount(self, vehicle_type):
        vehicle_type = vehicle_type.lower()
        toll = 0

        if vehicle_type == "car":
            toll = 50
        elif vehicle_type == "bus":
            toll = 100
        elif vehicle_type == "truck":
            toll = 150
        elif vehicle_type == "bike":
            toll = 20
        else:
            print(f"Unknown vehicle type: {vehicle_type}")
            toll = 0
        
        self.total_amount += toll

    def collect_toll(self, owner_type, vehicle_type):
        if owner_type.lower() == "vip":
            self.count_vehicle()
        else:
            self.calculate_amount(vehicle_type)
            self.count_vehicle()

    def display_details(self):
        print("Total Vehicles Passed:", self.no_of_vehicle)
        print("Total Toll Amount Collected: ₹", self.total_amount)



booth = Tollbooth()


booth.collect_toll("VIP", "Car")
booth.collect_toll("General", "Bus")
booth.collect_toll("General", "Bike")
booth.collect_toll("General", "Truck")
booth.collect_toll("VIP", "Bike")
booth.collect_toll("General", "Car")


booth.display_details()
