name = "tim"
age = 10

print(name, age, "python", 2020)



print(name, age, "python", 2020, sep=", ")      # Here, print functions is allowing us to print multiple arguments...
                                                # if we use this (seperators)'sep=' keyword, each line will be seperated by '(comma) , '
                                                # the seperators only used when you print several things at once,
                                                # if u print single value and that includes an f-string or a string produced
                                                # using .format(), then the seperator won't be printed
                                                # Remember that the seperators only used between the values we print, when we pass more than one value
                                                # to the print function

# * objects ---> that means we can provide several values
# sep = if we want to provide a value for sep, we have to specify its name, that's why they are also called as "named arguments"
# sep is a keyword argument
# other keyword argument is " end "
# " end " is very useful in loops
