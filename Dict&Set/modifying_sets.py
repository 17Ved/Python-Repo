numbers = {}            # in this line it will be dict
# numbers = {*""}       if we use this line type will be set
# numbers = {*{}}       this will also define type set

numbers = set()
print(numbers, type(numbers))


# to add items to the set, we use add() method
#
# numbers.add(1)
# print(numbers)


# while len(numbers) < 4:             # on this loop our set contains 4 unique values, duplicates will be ignored
#     next_value = int(input("Please enter your next value:  "))
#     numbers.add(next_value)
# print(numbers)                      # this is an easy way to remove duplicates values from data.

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# create a set from the list, to remove duplicates
# data is in unordered format in sets, but we can sort them

unique_data = sorted(set(data))
print(unique_data)


# create a list of unique colours, keeping the order they appeared.
unique_data = list(dict.fromkeys(data))     # here, fromkeys() creates a dictionary. It gets the keys from the iterable
print(unique_data)                       # we pass to it 'data' in our case
                                            # when a value already apperars in the dictionary the new one replaces the existing key. We then convert dictionary to list

print()
print(dict.fromkeys(data))
























