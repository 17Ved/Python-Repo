# a boolean value is a value that can either be true of false
# those are the only 2 values that a boolean can have.
# we can also test a string value using boolean
# we can use ' not ' to reverse a boolean value
# not True is False
# not False is True

# day = "Saturday"
# temperature = 30                                # Note:-- all 3 parts of the condition must evaluate true in order for the entire condition to be true
# raining = True
#
# if (day == "Saturday" and temperature > 27) or not raining:         # and has higher precedence than or
#     print("Go swimming")                                            # here ()  make the code much easier to read
#                                                             # always use (parentheses) when you mix 'and' 'or' in the same condition
# else:
#     print("Learn python")



if 0:
    print("true")                   # This code is unreachable     # 0 won't evaluate to True, so line 2 can't be executed

else:
    print("false")

name = input("Please enter your name: ")
if name != "":
    print("hello, {}" .format(name))
else:
    print("Are you the man with same name?")


































