# Problem Statement
# Little Puppy Kennel sells dogs of different breeds. They want to automate their selling process.
# Write a python program to implement the class diagram given below.

                                                                                                                            

# Class Description:

# dog_breed_dict: Static dictionary which contains the breed of the dog as key and the number of dogs available as value. Initialize it with the sample data given.
# Initialize static variable counter to 100
# breed_list: List of dog breeds required by the customer. Initialize it in the constructor
# dog_id_list: List of dog ids. Initialize it to an empty list in the constructor
# price: Total price to be paid by the customer. Initialize it to 0 in the constructor
# accessories_required: Boolean value – True indicated accessories are required and False indicated accessories are not required.                          Initialize it in the constructor
# validate_breed(): Return true if all the breeds required by the customer are available. Else return false
# validate_quantity(): Return true if one dog/breed is available for all the breeds requested by the customer. Else return false
# generate_dog_id(breed): Accept the breed of the dog for which dog id should be generated.                                                                                Auto-generate dog id starting from 101 prefixed by the first character of the breed
# get_dog_price(breed): Return the price of the dog whose breed is passed to the method
# calculate_total_price(): Calculate the total price of all the dogs required by the customer.
# Validate breed and quantity of all the dogs required by the customer
# If valid,
# For every breed in breed_list,
# Update quantity in dog_breed_dict
# Auto-generate dog id and append it to attribute, dog_id_list
# Add price to attribute, price
# If accessories are required, add 350 to attribute, price
# If price is more than 1500, provide 5% discount on price
# If any breed is not available, return -1
# If quantity is not available for any breed, return -2
# Breed

# Price

# Labrador Retriever

# 800

# German Shepherd

# 1230

# Beagle

# 650

# Perform case sensitive string comparison 

# For testing:

# Create objects of Dog class
# Invoke calculate_total_price() on Dog objects
# Display the details

class Dog:
    counter = 100
    dog_breed_dict = {
        "Labrador Retriever": 5,
        "German Shepherd": 12,
        "Beagle": 10
    }

    def __init__(self, breed_list, accessories_required):
        self.breed_list = breed_list
        self.accessories_required = accessories_required
        self.dog_id_list = []
        self.price = 0

    def validate_breed(self):
        for breed in self.breed_list:
            if breed not in Dog.dog_breed_dict:
                return False
        return True

    def validate_quantity(self):
        temp_dict = Dog.dog_breed_dict.copy()
        for breed in self.breed_list:
            if temp_dict[breed] == 0:
                return False
            temp_dict[breed] -= 1
        return True

    def generate_dog_id(self, breed):
        Dog.counter += 1
        return breed[0] + str(Dog.counter)

    def get_dog_price(self, breed):
        price_chart = {
            "Labrador Retriever": 800,
            "German Shepherd": 1230,
            "Beagle": 650
        }
        return price_chart.get(breed, 0)

    def calculate_total_price(self):
        if not self.validate_breed():
            return -1
        if not self.validate_quantity():
            return -2

        for breed in self.breed_list:
            Dog.dog_breed_dict[breed] -= 1
            self.dog_id_list.append(self.generate_dog_id(breed))
            self.price += self.get_dog_price(breed)

        if self.accessories_required:
            self.price += 350

        if self.price > 1500:
            self.price *= 0.95  # 5% discount

        return self.price

    def display_details(self):
        print("Dog ID List:", self.dog_id_list)
        print("Total Price: {:.2f}".format(self.price))


# ---------- Testing ----------

# Test Case 1: Valid request, accessories required
dog1 = Dog(["Labrador Retriever", "Beagle"], True)
result1 = dog1.calculate_total_price()
if result1 == -1:
    print("Breed not available.")
elif result1 == -2:
    print("Quantity not available.")
else:
    dog1.display_details()

# Test Case 2: Breed not available
dog2 = Dog(["Poodle", "Beagle"], False)
result2 = dog2.calculate_total_price()
if result2 == -1:
    print("Breed not available.")
elif result2 == -2:
    print("Quantity not available.")
else:
    dog2.display_details()

# Test Case 3: Quantity not available (simulate depletion)
dog3 = Dog(["German Shepherd"] * 13, False)  # 13 but only 12 available
result3 = dog3.calculate_total_price()
if result3 == -1:
    print("Breed not available.")
elif result3 == -2:
    print("Quantity not available.")
else:
    dog3.display_details()

    


