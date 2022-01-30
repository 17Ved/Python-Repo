# A set is an unordered collection with no duplicate entries. Python sets work the same way as they do in set theory.
# there's no way to access individual elements of a set.
# there are several ways to create set in python just like lists and dictionaries
# a python set is enclosed in curly braces- just like a dictionary.
# python can tell this is a set, rather than dictionary, because we don't have key/value pairs.
# each time you'll run your program you'll get output in different order, 'cause items in sets are unordered.
# set's aren't a sequence type - sequence types are ordered, so set can't be one- but we can still iterate over a set.
# Set uses hashes to store the items, anything that you want to put into a set must be hashable.
# if u try to put list into a set, you'll get an error
# NOTE - you can't index into a set. If items in a set don't have a fixed position, then it just doesn't make sense to
#   try to get an item at a certain position.
# 'set' object is not subscriptable- is another way to say that you can't index sets,that also means you can't slice it.
# you can compare 2 different sets
# if you're working with large data, checking for memberships will be a lot faster with a set, compared to list.


farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("Indexing a sequence")
animal_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animal_list[3]
print(goat)

# print("indexing a set is not possible")
# goat = farm_animals[3]

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
if more_animals == farm_animals:
    print('the sets are equal')
else:
    print('the sets are different ')






















