# class Enemy:              # Here both declaration for declaring classes does the same thing
# Benefits of using inheritance --
# 1. when creating classes first our subclasses gets all the attributes that's the data and methods that are defined in their base class, also known as a superclass, so that we don't have to write same code again and again
# 2. we can also extend or alter the behavior of the class by creating a subclass that adds extra methods or changes the behavior of an existing method.
# All python objects inherit from a base class called object, which defines '__str__' method.
import random  # for generating random numbers


class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit Points: {0._hit_points}".format(self)


class Troll(Enemy):             # subclass is a class that inherits from another class. Here Troll class is extending / inheriting Enemy class, which have all properties of Enemy class
    # pass
    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

# Subclasses can have additional attributes to extend their behaviour and allow them to do things that their base class doesn't do.

    def grunt(self):
        print("Me {0._name}, {0._name} stomp your".format(self))


class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):                   # random module for this line
        if random.randint(1, 3) == 3:
            print("******* {0._name} dodges *******".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampyreKing (Vampyre):            # extending 'Vampyre' class

    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)
















































































