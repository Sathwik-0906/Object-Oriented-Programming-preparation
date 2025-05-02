# Single inheritance enables a derived class to inherit properties and behavior from a single parent class.

# Run the below code and observe the output.

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class SmartPhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()


# If a class is derived from another derived class then it is called multilevel inheritance.

# Run the below code and observe the output.
class Product:
    def review(self):
        print ("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()


# When several classes are derived from common base class it is called hierarchical inheritance.

# Run the below code and observe the output.

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()


# If a class is derived from two or more base classes then it is called multiple inheritance.

# Run the below code and observe the output.

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class Product:
    def review(self):
        print ("Customer review")

class SmartPhone(Phone, Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()


# When a child is inheriting from multiple parents, and if there is a common behavior to be inherited, it inherits the method in Parent class which is first in the list. In our example, the buy() of Product is inherited as it appears first in the list.

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class Product:
    def buy(self):
        print ("Product buy method")

class SmartPhone(Product, Phone):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
