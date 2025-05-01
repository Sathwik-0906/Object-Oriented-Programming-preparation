from Flower import Flower
print("\n")   
f1 = Flower("Orchid", 120, 30)
print("Valid Flower:", f1.validate_flower())  # True
print("Stock Available for 10kg:", f1.validate_stock(10))  # True
f1.sell_flower(10)
print("Stock after selling 10kg:", f1.get_stock_available())  # 20
print("Stock below reorder level:", f1.check_level())  # False (20 > 15)
print("\n")
f2 = Flower("Rose", 150, 20)
print("Valid Flower:", f2.validate_flower())  # True
print("Stock Available for 30kg:", f2.validate_stock(30))  # False
f2.sell_flower(30)  # Should not reduce stock
print("Stock after failed sale:", f2.get_stock_available())  # 20
print("Stock below reorder level:", f2.check_level())  # True (20 < 25)

print("\n")
f3 = Flower("Lily", 100, 25)
print("Valid Flower:", f3.validate_flower())  # False
f3.sell_flower(5)  # Should not proceed
print("Stock after invalid flower sale attempt:", f3.get_stock_available())  # 25

print("\n")

f4 = Flower("Jasmine", 90, 40)
print("Stock at reorder level:", f4.check_level())  # False (40 is not less than 40)
f4.sell_flower(1)
print("Stock now:", f4.get_stock_available())  # 39
print("Below reorder level?", f4.check_level())  # True (39 < 40)
print("\n")

