# Dictionaries and sets are  built in data structures
# Dictionaries and sets aren't sequences. We can't access the items using index positions
# when dealing with items in a dictionary, we use a 'key' to get individual values from the dictionary
# Dictionaries store key/value pairs
# A set is an unordered collection of things. There's no way to retrieve a specific item from a set
# Dictionary is a collection of values, that are stored using a key
# Each value that's stored in the dictionary has a key. We use the key to get the values from the dictionary
# to create a dictionary literals we use curly braces, within the curly braces, we have keys and values separated by (:)
# we can get values from the dictionaries by providing the key
# we've got 2 ways to retrieve values from the dictionary, you can use the key as an index
# Or you can pass key to the '.get' method
# our keys are strings in this dictionary, & strings are case sensitive
# If the key doesn't exist, .get will return None, whereas indexing will crash with a KeyError.
# the .get method is useful when you're not sure if the key exists, or not.
# Indexing is faster than .get method that's why we don't use .get method in each dictionary
# when you know that the key is present then use indexing.
# Although they're not a sequence type, they are iterable. we can iterate over the keys in a dictionary
# we don't have to call enumerate() function with dictionaries, 'cause we have the dot .items method that we can use.
# changing values in a dictionary - you just assign a new value to the same key
# when you use the same key again, the new value replaces the old one.
# While deleting from a dictionary, we use the 'key' rather than an index position
# dictionary don't have .append() method
# update() method in dictionary -- this method is used to update one dictionary with the contents of another.
# note that dictionary keys are unique. the same key can't appear more than once in a dictionary
# values() method return a view of the dictionary's values, it's similar to key method, but instead of a list of a keys
# we get a list of values



vehicles = {                                # here we have a key like dream, virago etc. & after colon comes the value
    'dream': 'Honda 250T',
    'er5': 'Kawasaki Ninja',
    'can-am': 'Bombardier Can-am 250',
    'virago': 'yamaha Cv456',
    'tenere': 'yamaha ct575',
    'jimmy': 'suzuki900ff',
    'fiesta': 'ford fiesta 990.9',
    'roadster': 'Triumph street triple'

}

my_car = vehicles['fiesta']         # here we provide the key inside the square brackets and we get the value returned.
print(my_car)


commuter = vehicles['virago']
print(commuter)


learner = vehicles.get("er5")
print(learner)


vehicles["Star fighter"] = "Locked F-103"
vehicles["Lear jet"] = "Bombardier Learjet 3334"
vehicles["Toy"] = "glider"

# upgrade the virago --
vehicles["virago"] = "yamaha xv 373"


del vehicles["Star fighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "You wish! Sell the jet and you might afford racing car")        # .pop method removes an item from the dictionary, and returns the value
print(result)                                                                               # if the key doesn't exist, it returns whatever you pass for the default instead.
plane = vehicles.pop("Lear jet")
print(plane)

bike = vehicles.pop("tenere", "Not present")
print(bike)
print()


# for key in vehicles:                         # so, when you iterate over a dictionary, you're iterating over the keys.
#     print(key)                                 # if you want values, you might decide to index the dictionary.
#     print(key, vehicles[key], sep=",")               # using this line we can get the values also


for key, value in vehicles.items():
    print(key, value, sep=" , ")














