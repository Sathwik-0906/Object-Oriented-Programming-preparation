class CallDetail:
    def __init__(self, phoneno, called_no, duration, call_type):
        self.__phoneno = phoneno
        self.__called_no = called_no
        self.__duration = int(duration)
        self.__call_type = call_type

    # Getter methods
    def get_called_no(self):
        return self.__called_no

    def get_phone_no(self):
        return self.__phoneno

    def get_duration(self):
        return self.__duration

    def get_call_type(self):
        return self.__call_type

    # Setter methods
    def set_called_no(self, called_no):
        self.__called_no = called_no

    def set_phone_no(self, phone_no):
        self.__phoneno = phone_no

    def set_duration(self, duration):
        self.__duration = duration

    def set_call_type(self, call_type):
        self.__call_type = call_type

class Util:
    def __init__(self):
        self.list_of_call_objects = []  # Initialize as an empty list

    def parse_customer(self, list_of_call_string):
        for i in list_of_call_string:
            details = i.split(",") 
            call_obj = CallDetail(*details)  # Create a CallDetail object
            self.list_of_call_objects.append(call_obj)  # Add to the list
        return self

# Test data
call = '9990000001,9330000001,23,STD'
call2 = '9990000001,9330000002,54,Local'
call3 = '9990000001,9330000003,6,ISD'

list_of_call_string = [call, call2, call3]

# Test the functionality
util_obj = Util().parse_customer(list_of_call_string)

# Print the results
for call in util_obj.list_of_call_objects:
    print(f"Phone No: {call.get_phone_no()}, Called No: {call.get_called_no()}, Duration: {call.get_duration()} mins, Call Type: {call.get_call_type()}")
