# roblem Statement
# Mega Mart, a retail shop, wants to record the number of items bought by its customers.

# Write a python program to implement the class diagram given below.

                                                           

# Class Description:

# list_of_items: Static list which contains the list of items available in the store. Initialize it with sample data as given - [Cake, Soap, Jam, Cereal, Hand Sanitizer, Biscuits, Bread]
# list_of_count_of_each_item_sold: Static list which contains count of items sold. Initialize count of each item to 0
# The above two lists have one-to-one correspondence
# items_purchased: List which contains the list of items purchased by the customer. Initialize it to an empty list in the constructor
# item_on_offer: Name of the item provided as an offer. Initialize it to None in the constructor
# provide_offer(): The shop has decided to give 1 Hand sanitizer free if soap is bought by the customer
# Increment the count of hand sanitizer in list_of_count_of_each_item_sold by 1
# Update the instance variable, item_on_offer to "HAND SANITIZER"
# sell_items(list_of_items_to_be_purchased): Accept the list of items that are to be purchased by the customer
# For every item in list_of_items_to_be_purchased
# Increment count of the item in the static list, list_of_count_of_each_item_sold by 1
# Add the item to attribute, items_purchased list
# If soap is purchased by the customer, then provide the offer by invoking the appropriate method
# find_total_items_sold(): Return the total number of items sold by the shop
# Note:

# Perform case insensitive string comparison 
# Assume that customer purchases only 1 quantity of each item and an item will appear only once in the list, list_of_items_to_be_purchased
# For testing:

# Create objects of Purchase class
# Invoke sell_items() on Purchase object by passing the list of items to be purchased by the customer
# Display the details


class Purchase:
    
    list_of_items = ['Cake', 'Soap', 'Jam', 'Cereal', 'Hand Sanitizer', 'Biscuits', 'Bread']
    list_of_count_of_each_item_sold = [0] * len(list_of_items)

    def __init__(self):
        self.items_purchased = []
        self.item_on_offer = None

    def provide_offer(self):
        index = self.get_item_index('Hand Sanitizer')

        if index != -1:
            Purchase.list_of_count_of_each_item_sold[index] += 1
            self.item_on_offer = "HAND SANITIZER"

    def sell_items(self, list_of_items_to_be_purchased):

        for item in list_of_items_to_be_purchased:
            index = self.get_item_index(item)

            if index != -1:
                Purchase.list_of_count_of_each_item_sold[index] += 1
                self.items_purchased.append(Purchase.list_of_items[index])

                if item.lower() == 'soap':
                    self.provide_offer()

    def find_total_items_sold(self):

        return sum(Purchase.list_of_count_of_each_item_sold)

    def get_item_index(self, item_name):

        
        for i, item in enumerate(Purchase.list_of_items):
            if item.lower() == item_name.lower():
                return i
        return -1

    def display_customer_details(self):
        print("Items Purchased:", self.items_purchased)
        print("Item on Offer:", self.item_on_offer)

    @staticmethod
    def display_store_sales():

        print("Store-wise Items Sold:")

        for item, count in zip(Purchase.list_of_items, Purchase.list_of_count_of_each_item_sold):
            print(f"{item}: {count}")

        print("Total Items Sold:", sum(Purchase.list_of_count_of_each_item_sold))



customer1 = Purchase()
customer1.sell_items(["Soap", "Jam", "Bread"])
customer1.display_customer_details()

customer2 = Purchase()
customer2.sell_items(["Cake", "Cereal"])
customer2.display_customer_details()


Purchase.display_store_sales()
