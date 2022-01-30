# Deleting items from the list

data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
#
# del data[0:2]           # deleting items from index 0 to 1 using slice
# print(data)
# del data[14:]      # this won't delete items from position 16...Reason --> we've already deleted two items i.e (4,5)
# print(data)         # so, that means the index position of each item will be changed & will start from item (104)

#

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):   # this code won't work
#         del data[index]
#
# print(data)




# process the low values in th list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)


# process the high values from the list
start = 0

for index in range(len(data) - 1, -1, -1):          # here we want to work backwards, which means we'll start at the index position 1 less
    if data [index] <= max_valid:                                 # than the length of the list
        # we have the index of the last item to keep
        # set 'start' to the position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1                                     #(-1, -1, -1)  ---> we can't use '0' as the stop value, remember that the last value in a range
        break                                     # or slice isn't included, so if we use '0' first item in the list won't ve included
                                                    # that's why we're using (-1) as the stop value
                                                    # and finally to work backwards, we use step (-1)
print(start)

del data [start:]
print(data)



# IMP POINTS:-
# we looked at indexing and slicing in lists, also common sequence opeerations such as min, max, index, count, len
# append is a method that can only be used with a mutable sequence type such as list- to add new values

# a for loop that iterates ove the items in a list, is a convenient way to process the data in your lists
# if u want to use index positions of items, enumerate fuction is an efficient way of getting the index positions, when iterating

# sort() method can be used to sort the contents, in place without creating a copy of a list
# sorted() function sorts a sequence, and returns a list
# also the sorted function will sort any iterable or literal object and return a new list, leaving the original list unchanged
# a keyword argument can be added to specify how otems in a list should be compared, such as making them case- sensitive....



# there are several ways of creating a list include a list literal, slice, concatenation and list comprehensions


# then moved on to removing items from sorted and unsorted lists, by iterating backwards.
# the reversed function is one of the ways of doing this, with the advantage that we can use enumerate...


# we compared three methods for removing items from a list, and saw that deleting a slice is more efficient than deleting the individual items


