# Polymorphism -- Poly -> Many, Morphe -> Form = Many forms

# an 'int' is not a 'float'
# a 'float' is not a 'list'
# a 'list' is not a 'tuple'
# a 'tuple' is not an 'int'

# IMP POINTS -
# All these objects are distinct types, but they can all be printed, because they all behave in the same way as fas as the "print" function is concerned.
# They all behave as "printable" objects in addition to their normal behavior as int, float, list, tuple, etc.
# The ability of objects to have different forms is called 'polymorphism' - which just means 'many forms'.
# inheritance is one way to implement polymorphism

class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Whee, This is fun!!")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):                     # on this line we've created a new wing object and assign it to the _wing attribute of the duck class,
        self._wing = Wing(1.8)              # any duck objects we create will have their own wing object and can use the attributes of the wing including this case of fly method
                                            # Now when a class contains another objects like this  that's called composition.

    def walk(self):                                     # so here "Duck" have 3 methods - walk, swim, quack
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack, quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):
    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this for south")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!!")


# def test_duck(duck):                        # As long as test_duck function is concerned 'Percy' is a 'Duck', so in other words Penguin's passing the duck test.
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # test_duck(donald)
    #
    # percy = Penguin()                                   # In short, here we saw how different objects can inherit similar behavior from a common base class
    # test_duck(percy)

# Composition and aggregation -
# Composition and aggregation are used when you have a 'has a' relationship, rather than a 'is a' relationship

# Composition --
# In composition, one of the classes is composed of one or more instance of other classes.
# In other words, one class is container and other class is content and if you delete the container object then all of its contents objects are also deleted.


# Aggregation -
# Aggregation is a weak form of composition.
# If you delete the container object contents objects can live without container object.










































































