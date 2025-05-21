# Problem Statement
# A mobile shop wants to create an online application to sell mobile phones.
# Write a python program to implement the class diagram given below.

        

# Class description
# OnlinePortal class:

# item_list: Static list which contains the list of names of phones that are sold using the online portal

# quantity_list: Static list which contains the quantity of each item

# price_list: Static list which contains the price of each item

# The above three lists have one-to-one correspondence

# search_item(item): Search for the given item in item_list. If found, return the index position of the item. Else return -1

# place_order(index,emi,quantity): Accept index position of the item being ordered, emi (True or False) and quantity and place order based on details given below:

# Update the quantity of the item in quantity_list

# Calculate the total cost of the item based on price in price_list and quantity ordered

# If the buyer has opted for emi, add 2% interest of total cost. Else provide 2% discount on total cost

# Return the final cost

# add_stock(item_name,quantity): Add stock for the given item based on rules mentioned below.

# Check if the given item is present in item_list.

# If found, check if the existing quantity of given item is less than or equal to 10. If so, add the given quantity to the existing stock. Else return -1

# Else return -2

# add_item(item_name,price,quantity): Add the given new item to the stock.

# Check if the given item is present in item_list. If not, append item_name, price and quantity to the appropriate static lists of the class

# If present, return -2

# Buyer class:
# purchase(item_name,quantity,emi): Purchase the given item from Online portal based on details given below.

# Check if the given item is present in OnlinePortal

# If present, check if the required quantity is available.

# If so, place the order by invoking the appropriate method of OnlinePortal class and return the cost

# Else, return -1

# Else, return -2

# Perform case sensitive comparison.
# Create objects of Buyer, OnlinePortal classes, invoke appropriate methods and test your program.
class OnlinePortal:
    item_list = ["iPhone", "Samsung", "OnePlus"]
    quantity_list = [5, 12, 8]
    price_list = [80000, 50000, 45000]

    @classmethod
    def search_item(cls, item):
        try:
            return cls.item_list.index(item)
        except ValueError:
            return -1

    @classmethod
    def place_order(cls, index, emi, quantity):
        if cls.quantity_list[index] < quantity:
            return -1
        cls.quantity_list[index] -= quantity
        cost = cls.price_list[index] * quantity
        if emi:
            cost += cost * 0.02
        else:
            cost -= cost * 0.02
        return round(cost, 2)

    @classmethod
    def add_stock(cls, item_name, quantity):
        index = cls.search_item(item_name)
        if index == -1:
            return -2
        if cls.quantity_list[index] <= 10:
            cls.quantity_list[index] += quantity
            return cls.quantity_list[index]
        return -1

    @classmethod
    def add_item(cls, item_name, price, quantity):
        if item_name in cls.item_list:
            return -2
        cls.item_list.append(item_name)
        cls.price_list.append(price)
        cls.quantity_list.append(quantity)
        return 1


class Buyer:
    def __init__(self, buyer_name):
        self.buyer_name = buyer_name

    def purchase(self, item_name, quantity, emi):
        index = OnlinePortal.search_item(item_name)
        if index == -1:
            return -2
        if OnlinePortal.quantity_list[index] < quantity:
            return -1
        return OnlinePortal.place_order(index, emi, quantity)


buyer1 = Buyer("John")
buyer2 = Buyer("Alice")

cost1 = buyer1.purchase("iPhone", 2, True)
cost2 = buyer2.purchase("Samsung", 15, False)
cost3 = buyer1.purchase("Nokia", 1, False)

OnlinePortal.add_stock("OnePlus", 3)
OnlinePortal.add_item("Realme", 30000, 6)

print("Cost 1:", cost1)
print("Cost 2:", cost2)
print("Cost 3:", cost3)
print("Items:", OnlinePortal.item_list)
print("Quantities:", OnlinePortal.quantity_list)
print("Prices:", OnlinePortal.price_list)


