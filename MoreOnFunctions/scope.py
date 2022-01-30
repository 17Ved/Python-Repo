# Namespace and more on Scope and Recursion
# python allows function to be nested on another functions
# Recursive function is a function that calls itself abd they're very useful in dealing with structures that contain themselves

def fact(n):
    """ calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):               # range starts from no.2 and stops at n + 1 to include the value 'n' so remember that last value on our rang includes is one less than the stock value
            result *= f
        return result


def factorial(n):                                   #'n' can also be defined as n * (n-1)
    """" calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    """ F(n) = F(n-1) + F(n-2) """
    if n <= 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus + n_minus2
            n_minus2 = n_minus
            n_minus = result
    return result


for i in range(10):
    print(i, fib(i), "\t", fibonacci(i))













