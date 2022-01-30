# sorted functioin can be used to sort any iterable object
pangram = "the quick brown fox jumps over the lazy dog"

letter = sorted(pangram)            # this will produce a list. Python sorted() function will take any iterable but will always return a list
print(letter)

numbers = [2.3, 4.5, 7.9, 1.2, 6.9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)



# difference between .sort()  &  sorted()  method
# .sort()  --->   sort method sorts the list in place, that means we don't assigns the return value to another variable
# sorted()  --->  because sorted returns a new list, we assigned its return value to another variable ' sorted_numbers'


missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key= str.casefold)
print(missing_letter)


# case insensitive sorting --->
# whenever you want to perform a case insensitive sort, just add key= str.casefold as an argument to sort or sorted


names = ["Graham",
         "John",
         "terry",                   # here if we don't use (key=str.casefold) then, we'll get output in order --- Capitalized letter first order
         "eric",                    # so, if we use (key=str.casefold) then, we'll get output in alphabetical order without that
         "Terry",                   # capitalized letter first format...
         "michael"
         ]


names.sort(key=str.casefold)
print(names)
names.sort()
print(names)






