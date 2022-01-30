# IMP POINTS about " functions "  ----->
# python includes a lot of function as standard, and we can also import others
#
# If there isn't a function that does what you want, you can write your own.
#
#
# function is great way to avoid duplicating code.
#
# putting code in a function allows you to use it over and over again, without rewriting it
#
#
# not all functions returns a value, ex- print and .sort method of lists, perform a action
#
# other function returns a value and return it for your main code to use.
#
#
#
# *Methods -
# A function that bounds to an variable is called a method
#
# you use methods in the same way as u use function, but specify the object that they will act on, before the dot.

# a python function starts with a keyword -- "def"
# they are written in lowercase
# function names follow the same name as variable names
# they mustn't start with a digit
# you can use underscore
# all function definitions have parentheses () after the function name

# Parameters --->
# Parameters are like placeholders for the real value that you'll pass to your function
# They're just variables, but they're given a value when you call the function
# you may also seem them referred as 'formal parameters'
# whatever values we provide to those parameters, will be used when we call the function
# when a function has parameters , you must provide suitable values when you call the function


# Arguments ---->
# Arguments are the values that will be used by formal parameters, when we call a function
# Each parameter must be given a value, by providing an argument in the function call.
# Providing values as arguments is called passing the arguments.
# If a function defines two parameters, we pass two arguments to it when we call it.
# Remember that some function can have default values.


# Positional Arguments ---->
# positional arguments are assigned to the parameters in the order they appear.


def multiply(x: float, y: float) -> float:             # passing parameters here (x,y) & below that we're passing arguments (10.5,4)
    """
    Get an integer from Standard Input (stdin).
    :param x: 
    :param y:
    :return:
    """
    result = x * y
    return result
                                # our first argument is 10.5 and that gets assigned to the first parameter 'x'
                                # for that reason, these arguments are positional arguments


answer = multiply(10.5, 4)      # on this line we're calling multiply() function, because our functions returns a value,
print(answer)                   # we can bind the variable 'answer' to the return value


forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)


# Fibonacci number series --
# Fibonacci sequence is the sum of two preceding ones, starting from 0 and 1
# 0 + 1 = 1, 1 + 1 = 2, 2 + 1 = 3, 3 + 2 = 5

def fibonacci(n: int) -> int:      # single parameter (n)           # by using int) -> int, we can understand that our function takes int and returns int
    """Return the `n` th fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):                  # so here, loop goes around n_minus1 times
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))


"""
 Function Annotation -
 function annotations are basically a special case of type hints, applied to function parameters and return values.
    Function annotation - they make it clearer what kinds of values your functions can accept, and what they return
"""







































































