# An apparel shop wants to manage the items which it sells. 
# Write a python program to implement the class diagram given below.



# Class Description:
# Apparel class:

# Initialize static variable counter to 100
# In the constructor, auto-generate item_id starting from 101 prefixed by "C" for cotton apparels and "S" for silk apparels. Example – C101, S102, S103, C104 etc.
# calculate_price(): Add 5% service tax on the price of the apparel and update attribute, price with the new value
# Cotton class:

# While invoking parent constructor from child constructor, pass "Cotton" as item_type
# calculate_price(): Update attribute, price of Apparel class based on rules given below
# Add service tax on price by invoking appropriate method of Apparel class
# Apply discount on price
# Add 5% VAT on final price
# Silk class:

# While invoking parent constructor from child constructor, pass "Silk" as item_type
# calculate_price(): Update attribute, price of Apparel class based on rules given below
# Add service tax on price by invoking appropriate method of Apparel class
# Identify points earned based on rules given below:
# Silk apparels with price more than Rs. 10000, earn 10 points and anything less than or equal to that earn 3 points
# Initialize attribute, points with the identified points
# Add 10% VAT on price
# Note: Perform case sensitive string comparison  

# For testing:

# Create objects of Cotton class and Silk class
# Invoke calculate_price() on Cotton objects and Silk objects
# Display their details

#lex_auth_012753087522512896330
#Start writing your code here
class Apparel:
    counter = 100
    def __init__(self, price, item_type):
        self.__price = price
        self.__item_type = item_type
        Apparel.counter += 1
        prefix = "C" if item_type == "Cotton" else "S"
        self.__item_id = prefix + str(Apparel.counter)
        
    def get_item_id(self):
        return self.__item_id

    def get_item_type(self):
        return self.__item_type

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price
        
    def calculate_price(self):
        self.__price += self.__price * 0.05


class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(price, "Cotton")
        self.__discount = discount
        
    def get_discount(self):
        return self.__discount
        
    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        price -= price * (self.__discount / 100)
        price += price * 0.05  # VAT
        self.set_price(price)


class Silk(Apparel):
    def __init__(self, price):
        super().__init__(price, "Silk")
        self.__points = 0

    def get_points(self):
        return self.__points

    def calculate_price(self):
        super().calculate_price()  # Add 5% service tax
        price = self.get_price()

        # Assign points
        if price > 10000:
            self.__points = 10
        else:
            self.__points = 3

        # Add 10% VAT
        price += price * 0.10
        self.set_price(price)


# Test cases
cotton = Cotton(5000, 10)
cotton.calculate_price()
print("Cotton Apparel")
print("Item ID:", cotton.get_item_id())
print("Item Type:", cotton.get_item_type())
print("Final Price:", round(cotton.get_price(), 2))
print("Discount:", cotton.get_discount())
print()

silk = Silk(12000)
silk.calculate_price()
print("Silk Apparel")
print("Item ID:", silk.get_item_id())
print("Item Type:", silk.get_item_type())
print("Final Price:", round(silk.get_price(), 2))
print("Points Earned:", silk.get_points())
