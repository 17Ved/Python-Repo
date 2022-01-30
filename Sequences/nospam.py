menu = [
    ["egg", "bacon"],
    ["egg","sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# code for removing "spam" from the list and print remaining items present in the list
# 1st solution ---->


for meal in menu:
   for index in range (len(meal) -1, -1, -1):
       if meal [index] == "spam":
            del meal[index]


   print(" , " .join(meal))


# 2nd solution ---->
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item)
#             #print(item, end=" , ")        # here, setting end to a space, tells print to print a space after printing, instead of a new line
#
#     print()


# 3rd code --- it's more advanced soln ---->
# for meal in menu:
#     item = " , ".join((item for item in meal if item != "spam"))
#     print(item)

# function signatures
# the term function signatures means the definition of a function
# that includes the function's name, and the parameters that it defines
#Note -- not all functions have parameters, but the parantheses are still needed when defining and calling function

# .join method() ---> it's useful for producing output from a list, and can be used with iterable















