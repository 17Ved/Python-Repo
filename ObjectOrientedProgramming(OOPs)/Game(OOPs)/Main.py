# from Player import Player
#
# ved = Player("Ved")
# print(ved.name)
# print(ved.lives)
#
# ved.lives -= 1
# print(ved)
#
# # print(ved.get_name())
# # ved.set_lives(300)
#
#
# ved.lives -= 1
# print(ved)
#
#
# ved.lives -= 1
# print(ved)
#
#
# ved.lives -= 1
# print(ved)
#
# # ved._lives = 9
# print(ved)
#
# ved.lives = 9
# print(ved)
#
# ved.level = 2
# print(ved)
#
#
# ved.level += 5
# print(ved)
#
# ved.score(500)
# print(ved)

# ------------------------------------------------------------------------------------------------------------------------------------------------------ #

from enemy import Enemy, Troll, Vampyre, VampyreKing

# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(8)
# print(random_monster)
#
# random_monster.take_damage(9)
# print(random_monster)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Method Overloading in Python -                 # python doesn't have the concept of overloaded methods, the last method you defined in the code will be only one that exists
# Like other languages (for example, method overloading in C++) do, python does not support method overloading by default.
# The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method.

# Method overriding in Python --
# overriding means replacing it with another one
# Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes.
# When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

#
# ugly_troll = Troll("PUG")                                # when we don't specify any arguments on line 59 the default that we specified in enemy's init method are used.
# print("ugly_troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll), end="")
# another_troll.take_damage(18)
# print(another_troll)
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# # monster = Enemy("Basic enemy")      # this line should give an error -- AttributeError: 'Enemy' object has no attribute 'grunt'
# # monster.grunt()
#
# vamp = Vampyre("Vlad")
# print(vamp)
# vamp.take_damage(5)
# print(vamp)
#
# print("-" * 40)
# another_troll.take_damage(30)
# print(another_troll)
#
# # while vamp.alive:
#     # if not vamp.dodges():
#     #     vamp.take_damage(1)
#         # print(vamp)
#
# vamp._lives = 0
# vamp._hit_points = 1
# print(vamp)

# dracula = VampyreKing("Dracula")
# print(dracula)
# dracula.take_damage(12)
# print(dracula)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- #



a = 3
b = "ved"
c = 1, 2, 3
print(a, b, c)





