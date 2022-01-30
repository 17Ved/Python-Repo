import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}
# perform d
# print(animals)
things = animals.copy()     # on this line we use, copy method to create a copy of the original dictionary
#                             # any changes we make to animals isn't reflected in the things dictionary, and that's because now, things is a new dictionary created by copying animals
# animals["teddy"] = "toy"

# perform a deep copy
# things = copy.deepcopy(animals)     # this time, we'll see that toy is only added to the list in the things dictionary.


print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

# if we want to separate dictionaries, we should create a copy.

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])


# A deep copy will also copy any object that are contained in whatever you're copying.
# A shallow copy only copies references= - it doesn't make copies of contained objects.


# hashable value - an object is hashable if it has a hash value which never changes during its lifetime
# a hash function produces fixed size hash values from its input. The hashes are usually integers,but don't have to be.
# there are many ways to implement a hash function.
# a hash function produces values that can be used to index a fixed sized data structure called hash table.
# a hash doesn't have to be unique, two different strings can have the same hash. that's known as COLLISION.




























