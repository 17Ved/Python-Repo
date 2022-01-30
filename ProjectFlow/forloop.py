# python provides ways to repeat a block of code like:
# for loop, while loops, list comprehensions and generators
# a for loop works by iterating over some set of values
# it assigns each of values one by one to one or more varibles


# parrot = "Norwegian Blue"
#
# for character in parrot:                 # it loop around until there's no more values
#     print(character)



                                        # for loops extracting form user input

number = input("please enter a series of numbers using any separators you like: ")                       #in this program we're printing separators
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

#print(separators)

values = "".join(char if char not in separators else " " for char in number).split()       #ignore these lines for now
print(sum([int(val) for val in values]))                                                        # ignore these lines for now
