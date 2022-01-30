# Drawback of Pickling -
# The object all have to be loaded back into memory into the computer's memory...if you're dealing with large amount of objects for ex. dictionary then loading that in entire thing to memory may not be a ralistic option.
# Python has an alternative for the above problem that's the 'Shelve Module'.


# Shelve Module ---
# Shelve is a python module used to store objects in a file.
# The Shelve module implements persistent storage for arbitrary Python objects which can be pickled, using a dictionary-like API.


# Shelve module provides a shelves, and you can think of it like dictionary, but it's actually stored in a file rather than in memory...
# Now like a dictionary the shelves holds the key value pairs and the values can be anything they can be pickled which as you found out was just about everything.
# Now the keys themselves, must be strings unlike a dictionary where the keys can be immutable objects such as tuple...
# IMP Distinction --
# All the methods we use with dictionaries can also be used for shelve objects, so it can be really useful to think of them as a persistent dictionary...
# Shelve are read and write by nature so there's really no need to specify the mode for shelve.
# You can't initialize  a shelve using literal as we could with a dictionary
# Remember that it's your responsibility to close the shelve yourself manually...
# In dictionaries we pointed out that the keys themselves are unsorted and the actual order is undefined for dictionary now the same is true for a shelve,
# The good thing is that we can iterate through the keys of our fruit adn print them, they may be in alphabetical order
# IMP difference between shelve and dictionary ---
# Shelves a shelve key must be a string and dictionaries themselves can accept any immutable object as a key...


import shelve

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack+": " + fruit[snack])

#
# while True:
#     dict_key = input("Please enter a fruit:")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#
#     else:
#         print("We don't have a " + dict_key)


# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
#
# for f in ordered_keys:
#     print(f + "-" + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()

# print(fruit)


































































