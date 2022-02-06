# Object-Oriented Programming aims to combine data and the processes that act on that data into objects which is called encapsulation.
# In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming.
# It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming.
# The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.

# Main Concepts of Object-Oriented Programming (OOPs) -
# Class
# Objects
# Polymorphism
# Encapsulation
# Inheritance
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Class -
# A class is a collection of objects.
# A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods.

# Objects -
# The object is an entity that has a state and behavior associated with it.
# It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.
# More specifically, any single integer or any single string is an object.

# Polymorphism -
# Polymorphism simply means having many forms.
# For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.

# Encapsulation -
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
# It describes the idea of wrapping data and the methods that work on data within one unit.
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
# To prevent accidental change, an object’s variable can only be changed by an object’s method.
# Those types of variables are known as private variables.

# Inheritance -
# Inheritance is the capability of one class to derive or inherit the properties from another class.
# The class that derives properties is called the derived class or base class and the class from which the properties are being derived is called the base class or parent class.

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Some other IMP Points to be noted -
# Everything in python is an object...
# OOP uses classes and methods to provide object that encapsulates both dat and the functions that operate on that data...

# 'Method' is just another word for "function"...
# When function is a part of 'class' we call it Method...
# There is slight difference in function and method
# But writing the method is same as writing the function...

# The "self" keyword is used to represent an instance (object) of the given class. ...
# However, since the class is just a blueprint, 'self' allows access to the attributes and methods of each object in python.
# This allows each object to have its own attributes and methods.
# 'self' is just the name of a parameter, the imp thing is the presence of the parameter not what its called...

# Once class is created, we can then create as many instances of that class as we want.
# once the instance have been created you can then call their methods and access their variables
# ---------------------------------------------------------------------------------------------------------------------------------------
# "__init__" Method - The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach.
# The __init__ function is called every time an object is created from a class.
# The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.


# a = 10
# b = 78
#
# print(a + b)
# print(a.__add__(b))


class Kettle(object):                       # "__init__" is a method inside 'Kettle' class.

    power_source = "electricity"

    def __init__(self, make, price):        # when we create objects of this "Kettle" class they all have name and a price. They will not have same name or same price,
        self.make = make                    # each instance of the class will have its own values for name and price, 'name' & 'price' are attributes here...
        self.price = price                  # so class from which objects can be created and all the objects created from the same class will share the same characteristics
        self.on = False                     # Now an INSTANCE is just another name for an object created from a class definition...

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.999)          # Now on this line we created an instance / object of the "Kettle" class & we've given it the name "kenwood"
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.344
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)        # Same here on line '73'----        So each instance has its own values for naming and price and their access by using . annotations
print(hamilton.price)                        # So, we type in kenwood.price or Hamilton.make for argument's sake to access that information...


print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models : {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class : templater for creating objects. All objects created using the same class will have the same characteristics.
Object : an instance of a class.
Instantiate : create an instance of a class.
Method : a function defined in a class.
Attribute : a variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)


Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

kenwood.power = 1.2
print(kenwood.power)
# print(hamilton.power)       # we should get an error on this line, 'cause hamilton don't have attribute-'power'


print("Switch to atomic power")             # A class attribute is a Python variable that 'belongs to a class' rather than a particular object.
Kettle.power_source = "atomic"              # It is shared between all the objects of this class, and it is 'defined outside' the constructor function, __init__(self,...) , of the class.
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)















































