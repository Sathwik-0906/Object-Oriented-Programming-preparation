# Write a Python program to generate tickets for online bus booking, based on the class diagram given below.



# Method description:

# Initialize static variable counter to 0
# validate_source_destination(): Validate source and destination. source must always be Delhi and destination can be either Mumbai, Chennai, Pune or Kolkata. If both are valid, return true. Else return false
# generate_ticket():
# Validate source and destination
# If valid, generate ticket id and assign it to attribute, ticket_id.Ticket id should be generated with the first letter of source followed by first letter of destination and an auto-generated value starting from 01 (Ex: DM01, DP02,.. ,DK10,DC11)
# Else, set ticket_id as None
# Note: Perform case insensitive string comparison


# For testing:

# Create objects of Ticket class
# Invoke generate_ticket() method on Ticket object
# Display ticket id, passenger name, source, destination
# In case of error/invalid data, display appropriate error message

class Ticket:
    counter = 1  # Start from 1 as per the requirement

    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__source = source
        self.__destination = destination
        self.__ticket_id = None

    def get_passenger_name(self):
        return self.__passenger_name

    def get_ticket_id(self):
        return self.__ticket_id

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def set_passenger_name(self, passenger_name):
        self.__passenger_name = passenger_name

    def set_ticket_id(self, ticket_id):
        self.__ticket_id = ticket_id

    def set_source(self, source):
        self.__source = source

    def set_destination(self, destination):
        self.__destination = destination

    def validate_source_destination(self):
        allowed_destinations = ["mumbai", "chennai", "pune", "kolkata"]
        return self.__source.lower() == "delhi" and self.__destination.lower() in allowed_destinations

    def generate_ticket(self):
        if self.validate_source_destination():
            src_initial = self.__source[0].upper()
            dest_initial = self.__destination[0].upper()
            self.__ticket_id = src_initial + dest_initial + f"{Ticket.counter:02}"
            Ticket.counter += 1
        else:
            self.__ticket_id = None

    def display(self):
        if self.__ticket_id:
            print(f"Passenger Name: {self.__passenger_name}")
            print(f"Ticket ID: {self.__ticket_id}")
            print(f"From Source: {self.__source}")
            print(f"Destination: {self.__destination}")
        else:
            print("Invalid source or destination: Ticket can't be generated.")

# ----------- Testing -----------

# Valid
ticket1 = Ticket("Sathwik", "Delhi", "Pune")
print("\n")
ticket1.generate_ticket()
ticket1.display()


print("\n")
# Invalid
ticket2 = Ticket("Rahul", "Mumbai", "Chennai")
ticket2.generate_ticket()
ticket2.display()


ticket3 = Ticket("Amar", "Delhi", "Mumbai")
print("\n")
ticket3.generate_ticket()
ticket3.display()


    