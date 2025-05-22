# Problem Statement
# "Mysore cabs" wants to automate their booking service.
# Write a python program to implement the class diagram given below.

                                

# Class description
# CabRepository:

# Initialize static lists, cab_type_list, charge_per_km and no_of_cars using the sample data given in the table

# There is one to one correspondence between these static lists

# Cab type list

# Hatch Back

# Sedan

# SUV

# Charge per km

# 9

# 12

# 5

# Number of cars

# 2

# 5

# 10

# CabService:

# check_availability(): Check whether the requested cab type is available or not for booking by checking in CabRepository.cab_type_list. If available return index position of the cab type in CabRepository.cab_type_list. Else return -1
# get_cab_charge(index): Find and return the charge per km for the car at the given index position from CabRepository.charge_per_km list
# calculate_waiting_charge( waiting_time_mins): Calculate and return waiting charge based on the given waiting_time_mins
# For first 30 minutes there is no waiting charge
# After 30 minutes, 5 rupees should be charged for every extra minute
# booking(waiting_time_mins): Calculate and return the final amount to be paid by the customer including the waiting charge for given waiting_time_mins. Also update the number of available cars and generate the service id for each booking starting from 1001. Return -1 if the car is not available.
# Perform case sensitive string comparison.
# Create objects of CabService class. Invoke booking() on CabService class by passing waiting time in mins and display the details.


class CabRepository:
    # Static lists with one-to-one correspondence
    cab_type_list = ["Hatch Back", "Sedan", "SUV"]
    charge_per_km = [9, 12, 5]
    no_of_cars = [2, 5, 10]


class CabService:
   
    service_id_counter = 1001

    def __init__(self, cab_type, distance_km):
        self.cab_type = cab_type
        self.distance_km = distance_km
        self.service_id = None
        self.final_amount = 0

    
    def check_availability(self):

        try:
            index = CabRepository.cab_type_list.index(self.cab_type)
            if CabRepository.no_of_cars[index] > 0:
                return index
            else:
                return -1  
        except ValueError:
            return -1 
    def get_cab_charge(self, index):
        return CabRepository.charge_per_km[index]

    def calculate_waiting_charge(self, waiting_time_mins):
        if waiting_time_mins <= 30:
            return 0
        else:
            extra_time = waiting_time_mins - 30
            return extra_time * 5

    def booking(self, waiting_time_mins):
        index = self.check_availability()
        if index == -1:
            return -1 
        cab_charge = self.get_cab_charge(index) * self.distance_km
        waiting_charge = self.calculate_waiting_charge(waiting_time_mins)

        self.final_amount = cab_charge + waiting_charge
        self.service_id = CabService.service_id_counter
        CabService.service_id_counter += 1

    
        CabRepository.no_of_cars[index] -= 1

        return {
            "Service ID": self.service_id,
            "Cab Type": self.cab_type,
            "Distance (km)": self.distance_km,
            "Waiting Time (mins)": waiting_time_mins,
            "Total Charge (Rs)": self.final_amount
        }



if __name__ == "__main__":
  
    booking1 = CabService("Sedan", 10)
    result1 = booking1.booking(45)
    
    booking2 = CabService("SUV", 5)
    result2 = booking2.booking(20)
    
    booking3 = CabService("Convertible", 8)
    result3 = booking3.booking(40) 

 
    for result in [result1, result2, result3]:
        if result == -1:
            print("Booking failed. Cab not available or invalid cab type.")
        else:
            print("\nBooking Successful:")
            for key, value in result.items():
                print(f"{key}: {value}")
