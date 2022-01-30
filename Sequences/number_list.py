# only list is built in mutable sequence in python, there are others in standard library
#
# even = [2,4,6,8]
# odd = [1,3,5,7,9]

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# # len returns no. of items in the sequence
# # for string that would be no. of characters in the string
# # for list it's no. of items
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("Mississippi".count("s"))          #.count() ---> will return how many times leter "s" is in the string "Mississippi"

empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
#                                     # we use .extend() method to combine lists
# even.extend(odd)
# print(even)             # here we'll get the list in combined format, but not in sorted foramt, so we'll use sort method to sort lists
# another_even = even
# print(another_even)
#
# even.sort()
# print(even)                             # this will sort the lists
# even.sort(reverse=True)
# print(even)                 # & if we use .sort(reverse=True) then it will sort the list in reverse order
# print(another_even)



# The sort method dosen't create a copy of the list- it rearranges the items in the list

numbers = even + odd        # concatenating list
print(numbers)

numbers = [even , odd]      #this will produce list containing two lists
print(numbers)

for number_list in numbers:         # for loop to print each list, then an inner for loop to print the contents of each inner list.
    print(number_list)                  # it means we have inner for loop here

    for value in number_list:
        print(value)





# digits = sorted("4329876517")       # here we'll get list of strings
# print(digits)                       # so each string is a single character- a digit
#
# digits = list("4329876517")         # here we'll get list in the same order as they appeared in the string
# print(digits)
#
#
# # more_numbers = list(numbers)
# #more_numbers = numbers[:]
# more_numbers = numbers.copy()
# print(more_numbers)
#
# print(numbers is more_numbers)  # output is false, meaning they're not the same list, they're equal though because they contains same items in the same order
#
# print(numbers == more_numbers)  # the lists are equal meaning they both contain the same items


# here --  == will return True if the lists contain the same items, in the same order
#        'is'  operator will return True if two variables are referring to the same list
# ways to copy a list


