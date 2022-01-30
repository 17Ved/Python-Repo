shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "ved"                   # here we want to know (spam) its position in the list & we're going to store that in found_at

found_at = None             # None is a constant that's used to show that is something dosen't have a value

# for index in range (len(shopping_list)):                # len = length
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
#or
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found" .format(item_to_find))


# initialising variables and none










