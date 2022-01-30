
# The rules for parameters ---
# Any positional or keyword arguments that we define, MUST come first in the parameter list.
# If we have a var positional parameter that's a parameter that starts with (*) then it must come after any positional argument
# Any parameters defined after a var positional paramter must be keyword- only arguments (which includes var-keyword arguments)
# Finally, any var keyword arguments appear last....
# kwargs -- keyword arguments


def func(p1, p2, *args, k, **kwargs):
    print("positional-or- keyword:...{}, {}".format(p1, p2))                     # here we have defined 2 positional parameters p1 & p2.
    print("var-positional (*args):...{}".format(args))                           # after we have 'var' positional parameter called args -- it accepts variable number of arguments
    print("Keyword:.............{}".format(k))                                   # 'k' is a keyword parameter --- the argument has to be passed with a keyword, because otherwise, it would
    print("var-keyword:................{}".format(kwargs))                       # be included the *args arguments
                                                                                 # and then we finish with the a var keyword parameter, the convention is to call var keyword parameters kwargs, short for keyword arguments


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)




