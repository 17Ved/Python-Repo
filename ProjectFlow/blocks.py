                                        #introduction to blocks and statements
        # python doesn't use braces { } to indicate begin or end of program, but instead uses indentation to indicate when a new block starts.
        # python works in blocks of code



#for i in range (1, 13):
 #   print("No. {} squared is {} and cubed is {:4}" .format(i, i ** 2, i **3))
  #  print("*" * 80)



name = input ("enter your name:")
age = int(input("how old are you {0} ?" .format(name)))  #age = int (input("how old are you {0} ?" .format(name)))  ---> this is very common way
print(age)                                                                                                            # to get input from user


# if age >= 18:                               # here (:) indicates that we're about to start new code block
#     print("you are old enough to vote")
#     print("Please put an X in the box")
# else:                                                                               # shortcut key: ( win + ctrl + / )  ---> to comment out multiple lines of code
#     print("Plese come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))

elif age == 900:                                                  # to check more than two cases ---> elif
    print("sorry, Yoda, you die in return of the Jedi")

else:
    print("you are old enough to vote")
    print("Please put an X in the box")














