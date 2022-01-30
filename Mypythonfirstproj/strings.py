#string functions in python

print("Today is a good day to learn pyhton")
print('python is fun')
print("Pyhton's strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + "world")
greeting = "Hello"
name = input("Vedant")   #anything on the right hand of the equals symbol is evaluated first(input funcn called first)
print(greeting+name)
#if we want a space we can add that too
print(greeting +' ' +name)


# Variables in python
# variables in python is case sensitive
#greeting is bound to the word hello   (greeting = "Hello")

age = 24
print(age)

#how to know (data)type of variables
print(type(age))
print(type(greeting))

#in python you can rebind a name to different value
age = "2 years"      #now 'age' will be no longer int it'll be string after assigning string value to it...
print(age)
print(type(age))     # but this can create confusion while we using same variable name to assign different values ---so we'll use this-->

name2 = "jayesh"
age_in_words ="4 years"
print(name2 + " is " + age + " years old ")
print(type(age))


#Built in data-types in python, that can be classified as:---
# I. numeric
#II. iterator
#III. sequence  (which are also iterator)
#IV. mapping
#V. file
#VI. class
#VII. exception

# ****  numeric datatypes  1. int, 2. float, 3. complex
# float have fractional part  e.g 1.3,   3.456, 123.422
#NOTE --->> there's is no limit to the size of an interger that you can store in a python "int"

#  In python there is no data-type declaration (where you can specify the type of a variable)



                                        # f- strings        ----> to concatenate a string and an int     (python versions 3.6 & earlier versions)

name3 = "jayesh"
age_in_words ="4 years"
print(name3 + f" is {age} years old")

first_name = "John"
last_name = "Cleese"
age = 78

print(first_name + last_name + age)


print(f"pi is approximately {22 / 7:12.50f}")
pi = 22/7
print(f"pi is approximately {pi:12.50f}")






























