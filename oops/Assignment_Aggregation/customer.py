class Freight:
    counter = 198

    def __init__(self, from_customer, recipient_customer, weight, distance):
        self.__freight_id = None
        self.__recipient_customer = recipient_customer
        self.__from_customer = from_customer
        self.__weight = weight
        self.__distance = distance
        self.__freight_charge = 0

    def get_freight_id(self):
        return self.__freight_id

    def get_recipient_customer(self):
        return self.__recipient_customer

    def get_from_customer(self):
        return self.__from_customer

    def get_weight(self):
        return self.__weight

    def get_distance(self):
        return self.__distance

    def get_freight_charge(self):
        return self.__freight_charge

    def validate_weight(self):
        return (self.__weight % 5) == 0

    def validate_distance(self):
        return 500 <= self.__distance <= 5000

    def forward_cargo(self):
        valid_from = self.__from_customer.validate_customer_id()
        valid_to = self.__recipient_customer.validate_customer_id()
        valid_wt = self.validate_weight()
        valid_dist = self.validate_distance()

        if not valid_from:
            print(f"Error: from_customer ID '{self.__from_customer.get_customer_id()}' invalid.")
        if not valid_to:
            print(f"Error: recipient_customer ID '{self.__recipient_customer.get_customer_id()}' invalid.")
        if not valid_wt:
            print(f"Error: weight {self.__weight} is not a multiple of 5.")
        if not valid_dist:
            print(f"Error: distance {self.__distance} not in [500, 5000].")

        if valid_from and valid_to and valid_wt and valid_dist:
            Freight.counter += 2
            self.__freight_id = Freight.counter
            self.__freight_charge = (self.__weight * 150) + (self.__distance * 60)
        else:
            print("Forwarding failed due to invalid data.")


class Customer:
    def __init__(self, customer_id, customer_name, address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__address = address

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_address(self):
        return self.__address

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def set_address(self, address):
        self.__address = address

    def validate_customer_id(self):
        cid = self.get_customer_id()
        if len(cid) == 6 and cid[0] == "1" and cid.isdigit():
            return True
        else:
            print("NOT a valid customer ID.")
            return False


# ==== TEST ====
if __name__ == "__main__":
    # Valid example
    cust1 = Customer("123456", "Alice", "123 Apple St")
    cust2 = Customer("198765", "Bob", "456 Banana Ave")
    fre1 = Freight(from_customer=cust1, recipient_customer=cust2, weight=25, distance=1000)
    fre1.forward_cargo()
    print("Freight ID:", fre1.get_freight_id())             # Expected: 200
    print("Freight Charge:", fre1.get_freight_charge())     # Expected: 25*150 + 1000*60 = 63750

    print("\n--- Now an invalid example ---")
    cust_bad = Customer("23456", "Eve", "789 Cherry Blvd")  # Invalid ID
    fre2 = Freight(from_customer=cust_bad, recipient_customer=cust2, weight=27, distance=6000)
    fre2.forward_cargo()
    print("Freight ID:", fre2.get_freight_id())             # Expected: None
    print("Freight Charge:", fre2.get_freight_charge())     # Expected: 0
