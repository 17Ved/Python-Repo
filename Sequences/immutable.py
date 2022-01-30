# IMP points-- list & strings are both sequence types
# strings are immutable, which means they can't be changed
# lists on the other hand, are mutable. You can change the contents of a list
# immuntable objects in python --->
# int, float, bool, str, tuple, frozenset, bytes



#
# result = True           # rememeber here that we're printing ID of True here, the varibles result & another_result are just name that we've bound to that value
# another_result = result
# print(id(result))
# print(id(another_result))
#
#
# result = False             # we'll get different value here
# print(id(result))           # because bools are immutable, we weren't able to change value of True. What python's done insted, is rebound result to a new value - False


result = "Correct"
another_result = result
print(id (result))
print(id(another_result))

result += "ish"
print(id(result))                   # id of result will change here
print(id(another_result))           #id of another_result will not change --- because strings are immutable, python couldn't change the sting correct
                                    # what it did instead was create a new strinf, and bind the name result to this new string




















