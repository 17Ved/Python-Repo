# sequence types in python ---> list, tuple, ranges
# A sequence is an ordered collection of items
# the word "ordered" is important here
# All sequence types can be iterated over. i.e --> strings, list, tuples, ranges
# Not all iterables are sequences
# lists are enclosed in [].

computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
#
# for parts in computer_parts:
#     print(parts)
# print()
# print(computer_parts[2])
#
#
# print(computer_parts[0:3])              # this code will print out output in [] brackes
# print(computer_parts[-1])               # Note: that slicing a list produces another list

print(computer_parts)

# computer_parts[3] = "trackball"         # here we are replacing computer_parts list's (mouse) with 'trackball'
print(computer_parts)                   # using index no. computer_parts[3] = "" trackball, in short index no. [3] is replaced by "trackball"


# replacing string using slice ---->

print(computer_parts[3:])           # so here we're printing out the items starting at position 3, extending up to the end of the list

computer_parts[3:] = ["trackball"]           # here, each character of the trackball, will add to the list individually
print(computer_parts)                   # so, we have to add ["trackball"] this to get trackball in the list -- computer_parts


































