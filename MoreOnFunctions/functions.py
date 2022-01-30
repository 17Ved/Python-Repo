# Functions in Python ---
# Python Functions is a block of related statements designed to perform a computational, logical, or evaluative task.
# The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
# Python functions are created with the word 'def' following by the function name and a pair of parentheses.
# Because the function introduces block of code that def statement must be followed by a colon(:).
# All python functions returns a result
# So if you don't tell the function what result to return then it's going to return 'None'.
# If one of the argument is a function call then the function is executed and its result is used as the argument to print
# 'Arguments' refers to the actual values used when the function is called
# 'Parameter' is the variables defined in the function definition.
# Signature is a way of referring to a set of parameters in a function definitions, so two functions that take exactly the same parameters are said to be have the same signature.

def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def centre_text(text):
def centre_text(*args, sep=' ', end_char='\n', centered_file=None, flush_me=False):
    # text = str(text)            # Here, we are explicitly calling STR function to convert the argument that was passed to a string
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end=end_char, file=centered_file, flush=flush_me)
    return " " * left_margin + text


# with open("centered", mode='w') as centred_file:
#
#     # Calling the function --
#     python_food()
#     centre_text("Spam and eggs", centred_file)                        # We are now calling the function that we've created three times with a different parameter
#     centre_text("spam, spam and eggs", centred_file)
#     centre_text(17, centred_file)
#     centre_text("spam, spam, spam, spam", centred_file)
#
# print("first", "second", 3, 4, "fifth", sep=":")
# print()

# ------------------------------------------------------------        OR      ---------------------------------------------------
# print(centre_text("Spam and eggs",))
# print(centre_text("spam, spam and eggs"))
# print(centre_text(17))
# print(centre_text("spam, spam, spam, spam"))
#
# print("=" + str(12 * 3))
# print(sorted(["b", "d", "c", "a"]))


# ------------------------------------------------------------        OR      ---------------------------------------------------

# s1 = (centre_text("Spam and eggs",))
# print(s1)
# s2 = (centre_text("spam, spam and eggs"))
# print(s2)
# s3 = centre_text(17)
# print(s3)
# s4 = (centre_text("spam, spam, spam, spam"))
# print(s4)
#
# print("=" + str(12 * 3))
# print(sorted(["b", "d", "c", "a"]))

# ------------------------------------------------------------        OR      ---------------------------------------------------


with open("menu", "w") as menu:

    s1 = (centre_text("Spam and eggs",))
    print(s1, file=menu)
    s2 = (centre_text("spam, spam and eggs"))
    print(s2, file=menu)
    print(centre_text(17), file=menu)
    print(centre_text("spam, spam, spam, spam"), file=menu)

    print("=" + str(12 * 3))
    print(sorted(["b", "d", "c", "a"]))











































































