# escape characters in python

split_string = "This string has been\nsplit over\nseveral\nlines"   #\n --> inserts new line in our code
print(split_string)

tabbed_string = "1\t2\t3\t4\t5\t6"             #  give tab between two letters/words
print(tabbed_string)


# different types to print string --->
print('The Pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
#or
print("The Pet shop owner said \"No, no, 'e's uh,...he's resting\".")
#or
print("""The pet shop owner said "No, no,'e's uh,... he's resting".  """)
#or
print("""The pet shop owner said "No, no,\
'e's uh,... he's resting".  """)
                            #what if u want to include '\' in your strings
#print("C:\users\vedant\notes.txt")        -->> solution to this   --->  use "Raw string"  or "double \\"
print("C:\\users\\vedant\\notes.txt")
print(r"C:\users\vedant\notes.txt")





another_split_string = """This stirng has been 
split over 
several 
lines"""

print(another_split_string)
                                 #if you want to lay out a string with breaks,but don't want every one to start with new line when printed put \
anothersplitstring = """This stirng has been \   
split over \
several \
lines"""
print(anothersplitstring)



                    # Refracting code means changing its structure, without changing its bhehaviour
                    # Refractoring might change how the code does things, but doesn't change what it does