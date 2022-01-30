# python sets have a clear method. It removes all the items in the set, leaving an empty set.

small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

# to delete individual items u can use the remove or discard method - both do the same thing, they remove an item from set.
# the difference is that remove() will raise an exception if the item isn't present.

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99)
print(small_ints)


small_ints.remove(99)
print(small_ints)





























