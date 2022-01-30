# nested loop it's just one block of code inside another block
for i in range (1,13):                                          #1st we got outer loop that goes around 12 times Inside that on line two, we've another
    for j in range(1,13):                                       # loop that goes 12 times
        print("{0} times {1} is {2}".format(j, i , i * j))
    print("----------------------------")               # here print statement is a part of outer for loop
                                                        # if we indent it by another 4 spaces then it'll be part of iner for loop
                                                        # and if we remove all indentation for print statement then we'll get (-----) at the end of program




















