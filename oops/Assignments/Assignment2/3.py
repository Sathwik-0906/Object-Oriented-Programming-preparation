# Problem Statement
# Informatica, a consultancy services company has planned to offer cashless transaction service to its employees. The employees can use their smart cards any transaction (credit/debit).
# Write a python program to implement the class diagram given below.



# Class description
# SmartCard class:
#     set_account_balance(account_balance): Initialize account_balance to 500.

# Employee class:

# validate_employee_id(): Employee id should be in the range of 1000 (not inclusive) to 700000(inclusive). If valid return true. Else return false
# validate_card_no(): Validate employee's smart card number.
# Smart card number should have 9 characters
# It should begin with "INF" and
# It should not contain alphabets in any other positions
#     If the above rules are satisfied, return true. Else return false

# Transaction class:

# top_up_card(employee, amount): Accept the object of the employee whose smart card should be topped up with given amount.
# If the given amount is between 500 and 10000 (both inclusive),
# If employee.employee_id and employee.smart_card.card_no are valid, add the given amount to employee.smart_card.account_balance
# Else, return -1
# Else, return -1
# make_payment(employee,amount): Debit the given amount from the employee’s smart card and auto-generate attribute transaction_id starting with "T" followed by first digit of the employee id and first two numeric values of the card number, if the below rules are satisfied
# Enough balance should be present in employee's smart card
# employee.employee_id and employee.smart_card.account_balance should be valid
# It should be possible to maintain minimum balance of Rs.500 in the smart card even after the transaction is made
#       If any of the above rules are not satisfied, return -1

# Perform case sensitive string comparison.
# Create an object of SmartCard class, create an object of Employee using the SmartCard object.
# Create objects of Transaction class for the Employee object, invoke make_payment() and top_up_card() methods and display the details.

class SmartCard:
    def __init__(self):
        self.account_balance = 0
        self.card_no = ""

    def set_account_balance(self, account_balance):
        self.account_balance = 500


class Employee:
    def __init__(self, employee_id, card_no):
        self.employee_id = employee_id
        self.smart_card = SmartCard()
        self.smart_card.card_no = card_no
        self.smart_card.set_account_balance(500)

    def validate_employee_id(self):
        return 1000 < self.employee_id <= 700000

    def validate_card_no(self):
        if len(self.smart_card.card_no) != 9:
            return False
        if not self.smart_card.card_no.startswith("INF"):
            return False
        if not self.smart_card.card_no[3:].isdigit():
            return False
        return True


class Transaction:
    def __init__(self):
        self.transaction_id = ""

    def top_up_card(self, employee, amount):
        if 500 <= amount <= 10000:
            if employee.validate_employee_id() and employee.validate_card_no():
                employee.smart_card.account_balance += amount
            else:
                return -1
        else:
            return -1

    def make_payment(self, employee, amount):
        if employee.validate_employee_id() and employee.validate_card_no():
            if employee.smart_card.account_balance - amount >= 500:
                self.transaction_id = "T" + str(employee.employee_id)[0] + employee.smart_card.card_no[3:5]
                employee.smart_card.account_balance -= amount
            else:
                return -1
        else:
            return -1


e = Employee(12345, "INF123456")
t = Transaction()

print("Initial balance:", e.smart_card.account_balance)
result = t.top_up_card(e, 1000)
if result == -1:
    print("Top up failed")
else:
    print("Balance after top up:", e.smart_card.account_balance)

result = t.make_payment(e, 700)
if result == -1:
    print("Payment failed")
else:
    print("Payment successful")
    print("Transaction ID:", t.transaction_id)
    print("Balance after payment:", e.smart_card.account_balance)
