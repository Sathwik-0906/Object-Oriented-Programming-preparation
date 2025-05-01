class Customer:
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.__payment_status=None

    def get_customer_name(self):
        return self.__customer_name
    def get_payment_status(self):
        return self.__payment_status
    def pay(self,bill):
        if bill.get_bill_amount() > 0:
            self.__payment_status="Paid"
        else:
            self.__payment_status="Unpaid"

class Bill:
    counter = 1000
    def __init__(self):
        self.__bill_id=None
        self.__bill_amount=0

    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount
    def generate_bill_amount(self,items_quantity,items):
        self.__bill_id="B"+str(Bill.counter)
        Bill.counter+=1

        total=0
        for item_id,quantity in items_quantity.items():
            for item in items:
                if item.get_item() == item_id:
                    total+=item.get_price_per_quantity()*quantity
                    break

        self.__bill_amount=total
        

class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity

    def get_item(self):
        return self.__item_id
    def get_description(self):
        return self.__description
    def get_price_per_quantity(self):
        return self.__price_per_quantity
    

item1 = Item("I101", "Milk", 30)
item2 = Item("I102", "Bread", 20)
items = [item1, item2]


item_quantity = {"I101": 2, "I102": 3}  # 2 Milk, 3 Bread

# Create Bill
bill = Bill()
bill.generate_bill_amount(item_quantity, items)

# Print Bill Info
print("Bill ID:", bill.get_bill_id())              # B1001
print("Bill Amount:", bill.get_bill_amount())      # 2*30 + 3*20 = 60 + 60 = 120

# Customer Pays
customer = Customer("Sathwik")
customer.pay(bill)
print("Customer Payment Status:", customer.get_payment_status())  # Paid


        