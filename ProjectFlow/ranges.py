# in other languages u provide a starting value and an ending value and increment a variable each time round the loop.
# python is different approach to for loops makes them incredibly powerful and also very flexible.

# while saving your file type ranges not range only ---- if you type range only it can conflict with range keyword in python

for i in range (10,16):                      # why we always use (i) in for loop---> i is taken to be short for index, and the convention is that it
    print("i is now{}".format(i))           # is acceptable in a for loop, as we're using it here

                                            # (1,20) will not print 1 to 20, it'll print only 1 to 19---'cause range works in the same way as slices
                                            # range produces a range of numbers - from the starting value , up to but not including the end value
                                            # to include 20 also we need to type (1,21)

    # more about ranges:

# if u want to repeat block of code certain no. of times, there's no need to provide a start value,
# if u don't provide a start value it defaults to zero(0)

for i in range (10):
    print("i is now{}".format(i))

# adding step values;

for i in range (0,10,2):                         # here 0 is start value, 10 is stop value, 2 is step value
    print("i is now{}".format(i))

# if we want to step backwards:

for i in range(10, 0, -2):              # -2 is stepping backwards, start value 10, stop value is 0
    print("i is now{}".format(i))









