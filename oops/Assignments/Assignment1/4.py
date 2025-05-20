# Problem Statement
# A garment ware house wants to automate its order taking and delivery process.
# Write a python program to implement the class diagram given below.

                                              

# Class description:

# garment_dict: Static dictionary which stores cloth type (key) and a list (value) which contains the number of pieces available, price per piece and number of days it would take to deliver it. Initialize it using the sample data given: {"shirt":[45,400,30],"trousers":[250,500,25],"saree":[500,750,10],"jersey": [750,200,5]}

# Constructor: Initialize attribute, order_date to today's date. (Hint: time.strftime("%d/%m/%Y") returns today's date in the provided string format)

# calculate_amount(): Calculate and return the total amount to be paid based on the cloth type and number of pieces ordered

# update_stock(): Update stock based on details given below.

# Set the attribute, delivery_date to order_date + number of days required to deliver the ordered item. Hint: d = date.today() + timedelta(days=n) will give the resultant date which is the sum of today's date and 'n' number of days. Convert it to string using time.strftime("%d/%m/%Y") where time is the datetime variable to be converted to string.

# Update the number of pieces available for the ordered cloth type based on number of pieces ordered

# take_order(): Take the order, calculate amount and update stock based on rules given below.

# If the ordered cloth type and quantity (no_of_piece) are available based on details in garment_dict

# Calculate amount

# Update stock

# Return the calculated amount

# Else, return -1

# Perform case sensitive string comparison.
# Create an objects of GarmentOrder class, invoke take_order() method on the GarmentOrder objects, display the details and test your program.

from datetime import datetime, timedelta

class GarmentOrder:
    garment_dict = {
        "shirt": [45, 400, 30],
        "trousers": [250, 500, 25],
        "saree": [500, 750, 10],
        "jersey": [750, 200, 5]
    }

    def __init__(self, cloth_type, no_of_piece):
        self.cloth_type = cloth_type
        self.no_of_piece = no_of_piece
        self.order_date = datetime.today().strftime("%d/%m/%Y")
        self.delivery_date = None

    def calculate_amount(self):
        price_per_piece = GarmentOrder.garment_dict[self.cloth_type][1]
        return price_per_piece * self.no_of_piece

    def update_stock(self):
        GarmentOrder.garment_dict[self.cloth_type][0] -= self.no_of_piece
        delivery_days = GarmentOrder.garment_dict[self.cloth_type][2]
        delivery_dt = datetime.today() + timedelta(days=delivery_days)
        self.delivery_date = delivery_dt.strftime("%d/%m/%Y")

    def take_order(self):
        if self.cloth_type in GarmentOrder.garment_dict:
            available_pieces = GarmentOrder.garment_dict[self.cloth_type][0]
            if available_pieces >= self.no_of_piece:
                amount = self.calculate_amount()
                self.update_stock()
                return amount
        return -1


order1 = GarmentOrder("shirt", 10)
amount1 = order1.take_order()
if amount1 != -1:
    print("Order Date:", order1.order_date)
    print("Delivery Date:", order1.delivery_date)
    print("Amount to be paid:", amount1)
else:
    print("Order cannot be processed.")

order2 = GarmentOrder("saree", 600)
amount2 = order2.take_order()
if amount2 != -1:
    print("Order Date:", order2.order_date)
    print("Delivery Date:", order2.delivery_date)
    print("Amount to be paid:", amount2)
else:
    print("Order cannot be processed.")
