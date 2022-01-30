# not in

activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():         # casefold() --> converts a string to lowercase, but it handels different character sets better than just converting to lower case
    print("But I want to go to cinema")                 # as we know these strings are case sensitive so we'll use ---- string to lowercase funtions


                # write a program to ask for a name & age  age between 18-34, if they are , then welcome them to holiday otherwise not
name = (input("Enter your name please: "))
age = int(input("Enter your age please: "))

if age >= 18 and age <= 34:                     # we can also write this condition as (if 18 <= age <=34)
    print("You are ready to go on holiday")
else:
    print("Stay at home")






