# Problem Statement
# ABC DTH (Direct to Home) firm wants to calculate monthly rent for its consumers. 
# A consumer can register for one Base Package. Write a python program to implement the below given class diagram.

                              

# Class Description:
# DirectToHomeService class:

# Initialize static variable counter to 101
# Inside constructor, auto-generate consumer_number starting from 101
# BasePackage class:

# validate_base_pack_name():
# Validate base pack name. Valid values are "Silver", "Gold" and "Platinum".
# If invalid, set attribute, base_pack_name as "Silver" and display "Base package name is incorrect, set to Silver"
# calculate_monthly_rent():
# Check if subscription period is between 1 and 24 (both inclusive). If so,
# Validate base pack name
# Identify monthly rent based on base pack. Refer table given.
# Consumers are eligible for discount of one month's rent, if subscription period is more than 12 months
# Calculate final monthly rent as per the formula given below:
# final monthly rent = ((monthly rent * subscription period) – discount amount)/subscription period
# Return the calculated final monthly rent
# If not, return -1
# Base Pack Name

# Monthly Rent

# Silver

# 350.00

# Gold

# 440.00

# Platinum

# 560.00

# Note: Perform case sensitive string comparison

# For testing:

# Create objects of BasePackage class
# Invoke calculate_monthly_rent() on BasePackage object
# Display the details

from abc import ABCMeta, abstractmethod

class DirectToHomeService(metaclass=ABCMeta):
    counter = 101

    def __init__(self, consumer_name):
        self.__consumer_number = DirectToHomeService.counter
        DirectToHomeService.counter += 1
        self.__consumer_name = consumer_name

    def get_consumer_number(self):
        return self.__consumer_number

    def get_consumer_name(self):
        return self.__consumer_name

    @abstractmethod
    def calculate_monthly_rent(self):
        pass

class BasePackage(DirectToHomeService):
    def __init__(self, consumer_name, base_pack_name, subscription_period):
        super().__init__(consumer_name)
        self.__base_pack_name = base_pack_name
        self.__subscription_period = subscription_period

    def get_base_pack_name(self):
        return self.__base_pack_name

    def get_subscription_period(self):
        return self.__subscription_period

    def validate_base_pack_name(self):
        valid_names = ["Silver", "Gold", "Platinum"]
        if self.__base_pack_name not in valid_names:
            print("Base package name is incorrect, set to Silver")
            self.__base_pack_name = "Silver"

    def calculate_monthly_rent(self):
        if 1 <= self.__subscription_period <= 24:
            self.validate_base_pack_name()

            pack_prices = {
                "Silver": 350.00,
                "Gold": 440.00,
                "Platinum": 560.00
            }

            monthly_rent = pack_prices[self.__base_pack_name]
            discount = 0

            if self.__subscription_period > 12:
                discount = monthly_rent

            final_rent = ((monthly_rent * self.__subscription_period) - discount) / self.__subscription_period
            return final_rent
        else:
            return -1

# Testing
bp1 = BasePackage("Alice", "Gold", 14)
rent1 = bp1.calculate_monthly_rent()
print(f"Consumer No: {bp1.get_consumer_number()}, Name: {bp1.get_consumer_name()}, Monthly Rent: {rent1:.2f}")

bp2 = BasePackage("Bob", "Diamond", 10)  # Invalid pack name
rent2 = bp2.calculate_monthly_rent()
print(f"Consumer No: {bp2.get_consumer_number()}, Name: {bp2.get_consumer_name()}, Monthly Rent: {rent2:.2f}")

bp3 = BasePackage("Charlie", "Platinum", 25)  # Invalid subscription period
rent3 = bp3.calculate_monthly_rent()
print(f"Consumer No: {bp3.get_consumer_number()}, Name: {bp3.get_consumer_name()}, Monthly Rent: {rent3}")
