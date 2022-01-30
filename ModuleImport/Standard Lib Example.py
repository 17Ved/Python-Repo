# Standard Library in Python ---
# Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below.
# The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers,
# as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.
# Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.
# This library ships with Python 7 provides a wide range of modules that we can use
# so, it includes everything built into the language that we can use without explicitly importing anything
# & also other useful modules such as shelve and random...
# IMP Note - Anything whose name starts with an underscore (_) is something that we shouldn't change without a good reason :-)
# So, if name starts with 2 underscore then it can't be changed at all
# Underscore indicates that it's private to its module... so don't change it...
# dir() is a powerful inbuilt function in Python3, which returns list of the attributes and methods of any object (say functions , modules, strings, lists, dictionaries etc.)


# print(dir())
# print(dir(__builtins__))
#
# for m in dir(__builtins__):
#     print(m)
#
import random
import shelve
# print(dir())
# print()
# print(dir(shelve))

# for obj in dir(shelve.Shelf):
#     if obj[0] != '_':
#         print(obj)

# help(shelve)
help(random.randint)



















































