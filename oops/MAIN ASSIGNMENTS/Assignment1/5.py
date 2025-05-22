# Problem Statement
# An IT major wants to automate their process of employee laptop verification. A laptop allocated to an employee has a QR code and allocation expiry status. There will be only one laptop allocated to each employee.
# Write a python program to implement the class diagram given below.

                               

# Class description:
# Laptop:

# qrcode: Unique identity code of a laptop
# expiry: Boolean value which indicates the allocation expiry status of the laptop. True – allocation has expired, False – allocation has not expired
# Scanner:

# emp_laptop_dict: Dictionary which stores employee id as key and corresponding laptop object as value
# scan(empid,laptop): Accept the employee id and laptop that needs to be scanned.
# Check if the given employee is allocated the given laptop
# If the laptop allocation has not expired, return true. Else return false
# Else return false
# Perform case sensitive string comparison.
# Create few objects of Laptop class, use it to initialize emp_laptop_dict and create an object of Scanner class using the emp_laptop_dict.
# Invoke scan(empid, laptop) on Scanner object by passing different empid and laptops and test your program.

class Laptop:
    def __init__(self, qrcode, expiry):
        self.qrcode = qrcode  
        self.expiry = expiry  


class Scanner:
    def __init__(self, emp_laptop_dict):
        self.emp_laptop_dict = emp_laptop_dict 

    def scan(self, empid, laptop):
       
        if empid in self.emp_laptop_dict:
            allocated_laptop = self.emp_laptop_dict[empid]
            
            if allocated_laptop.qrcode == laptop.qrcode:
            
                if not allocated_laptop.expiry:
                    return True
        return False


laptop1 = Laptop("QR123", False)
laptop2 = Laptop("QR456", True)
laptop3 = Laptop("QR789", False)


emp_laptop_dict = {
    "EMP001": laptop1,
    "EMP002": laptop2,
    "EMP003": laptop3
}


scanner = Scanner(emp_laptop_dict)


print(scanner.scan("EMP001", laptop1))  
print(scanner.scan("EMP002", laptop2))  
print(scanner.scan("EMP003", laptop1))  
print(scanner.scan("EMP004", laptop3))  