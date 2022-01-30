
# palindrome --
# a palindrome is a word that reads the same backwards as forwards


def multiply(x, y):
    result = x * y
    # return result


def is_palindrome(string: str) -> bool:             # here we're indicating the return type with that arrow - a minus - followed by the greater than, after that we have return type bool
                                                    # we can seee what type of parameter is, and that the function returns a bool.
    backwards = string[::-1].casefold()          # here slice [::-1] is reversing the original string
    return backwards == string.casefold()         #and here we check if the reverse string is the same as the original, if it is we return True, otherwise False
                                                  # the expression 'backwards == string'  will evaluate to either True or False

# or u can write this code in one line
    # return string[::-1] == string


def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # backwards = string[::-1].casefold()
    # return backwards == string.casefold()
    return is_palindrome(string)        # here we're calling function itself instead of writing those above statements

#
# word = input("please enter word to check")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
#
# else:
#     print("'{}' is not a palindrome".format(word))



answer = multiply(18, 3)                # if you want your function to return value, you have to explicitly return it, using 'return' keyword
print(answer)

                        # Note ;-- it's often for a function to return a value, but sometimes they don't have anything to return
                        # for ex - sort() method, the sort function didn't return anything useful, but did perform a useful function






















