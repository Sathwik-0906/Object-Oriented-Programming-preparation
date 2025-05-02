# We have a list of customer objects. Complete the code so that we have a dictionary of customer objects based on location.

class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location

    def __str__(self):
        return f"{self.cust_name} ({self.cust_id})"

list_of_customers = [
    Customer(101, 'Mark', 'US'),
    Customer(102, 'Jane', 'Japan'),
    Customer(103, 'Kumar', 'India'),
    Customer(104, 'Alice', 'US')
]

dict_of_customer = {}

for i in list_of_customers:
    if i.location not in dict_of_customer:
        dict_of_customer[i.location] = []
    dict_of_customer[i.location].append(i)

# Print customers grouped by location
for location, customers in dict_of_customer.items():
    print(location, ":", [str(c) for c in customers])
