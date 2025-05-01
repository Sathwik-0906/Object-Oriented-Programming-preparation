# Problem Statement
# Animal Welfare Trust is on a visit to the circus camp to have a look at the four talking parrots added to the camp.
# A parrot is identified by its name and color. Apart from this, the trust has asked to assign a unique number for each parrot. The unique number should begin with 7001 and should be auto-incremented by 1 for every new parrot added to the camp.

# Identify the class name and attributes so as to represent parrots from the list given.

# beak_color

# __init__(name,color)

# name

# Parrot

# counter->static

# color

# Parrots

# unique_number

# Write a Python program to implement the class chosen with its attributes and methods. Represent few parrots, display their names, color and unique number.

# Note: Consider all the attributes to be private and methods to be public. Include getter methods for all the instance variables.

class Parrot:
    parrot_id=7001
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
        self.__unquie_id=Parrot.parrot_id
        Parrot.parrot_id+=1
    
    def get_name(self):
        return self.__name
    def get_color(self):
        return self.__color
    def get_unquie_no(self):
        return self.__unquie_id
    
    def set__name(self,name):
        self.__name=name
    def set_color(self,color):
        self.__color=color

    def display(self):
        print(f"The parrot name :{self.get_name()}")
        print(f"color :{self.get_color()}")
        print(f"The Unigue :{self.get_unquie_no()}\n")

