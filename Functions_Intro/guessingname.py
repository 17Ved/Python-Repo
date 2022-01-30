import random

#  more topics on if, elif, else
# answer = 5
#
# print("Please guess number betwee 1 and 10: ")
# guess = int(input())
#
# if guess == answer:
#     print("well done, you guessed it")
# else:
#
#     if guess < answer:
#         print("please guess higher")
#     else:       # guess must be higher than answer
#         print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print("sorry, you have not guessed correctly")



                    # OR below program will also work

# if guess == answer:
#     print("well done you guessed it")
#
# elif guess < answer:
#     print("please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("you got it ")
#     else:
#         print("you're totally wrong")
#
# elif guess > answer:
#     print("please guess lower")
#
#     guess = int(input())
#     if guess == answer:
#         print("you got it ")
#     else:
#         print("you're totally wrong")
# else:
#     print("you got it first time")











#
# if guess < answer:                          # if condition will always be evaluated
#     print("please guess higher")            # next, you can have 1 or more elif blocks, u don't have to include elif until it's needed,
#                                             # but, if u have any elif then they come after the if, elif also has to come before else
# elif guess > answer:                        # u don't have to use else, but if u do it must come after the if, also come after any elifs
#     print("Please guess lower")
#
# else:
#     print("you got it first time")




                        #  an if statement can contain many elif parts, but there can be olny one else part, elif = else if

       #*****************  The Random Module and import  ********************#


def get_integer(prompt):        # Adding documentation below
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string the user will see, when
        they're prompter to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

       # else:
        print("{0} is not a valid number".format(temp))


help(get_integer)

# print(input.__doc__)            # here, we're not calling the function- we're referring their attributes
# print("*" * 80)                 # that means we don't use parentheses after the function name
# print(get_integer.__doc__)
# print("*" * 80)
highest = 1000
answer = random.randint(1, highest)          # here we seperate the module name from the function name with a period or dot notation(.)
print(answer)     # TODO: Remove after testing
guess = 0                         # here initialize any number that doesn't equal to answer
print("Please guess number between 1 and {}".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break

    if guess == answer:
        print("well done, you guessed it")                 # intelliJ treats TODO in a special way, & also keeps track on them
        break
    else:

        if guess < answer:
            print("please guess higher")
        else:       # guess must be higher than answer
            print("please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("well done, you guessed it")
        # else:
        #     print("sorry, you have not guessed correctly")




                # Binary Search / Binary chop --->  when you have an ordered set of data to search through, you can split the data in half each time
                # that simplifies things slightly, but the basic steps are the same.




# Documentation in python ---
# you can access documentation in python by Ctrl + Q or Ctrl + right click



# Modules in python --->
    # A module is a file containing python definitions and statements
    # The file name is the module name with the suffix.py appended
    # Each .py file that you create becomes a new python module.
    # Modules can be imported into other modules, or executed














