# A method is the same as a function,except that it's bound to an object
# that means we need an object, in order to call the method
# when we call a method, we tell it which object it's called on
# in other words, which object it should be using when it's performs its function
# for ex. .append()  method can be used to add new item to the list



# current_choice ="-"
# computer_parts = []   # create an empty list
#
# while current_choice != '0':                            # so, here we're using .append method to add the items to the list
#     if current_choice in "123456":
#         print("adding {}".format(current_choice))
#         if current_choice == '1':
#             computer_parts.append("Computer")
#         elif current_choice == '2':
#             computer_parts.append("Monitor")
#         elif current_choice == '3':
#             computer_parts.append("keyboard")
#         elif current_choice == '4':
#             computer_parts.append("Mouse")                      # overall this code is so lengthy
#         elif current_choice == '5':
#             computer_parts.append("Mouse mat")
#         elif current_choice == '6':
#             computer_parts.append("HDMI cable")
#
#
#     else:
#         print("Please add options from the list below: ")
#         print("1:computer")
#         print("2:monitor")
#         print("3:keyboard")
#         print("4:mouse")
#         print("5:mouse mat")
#         print("6:HDMI cable")
#         print("0:Finish it")
#
#
#     current_choice = input()
# print(computer_parts)






# so we'll use the following code to improve our program and other things

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "HDMI cable",
                   "DVD Drive"
                    ]

#valid_choices = [str(i) for i in range (1,len(available_parts) + 1 )]       # -- this is comprehension


valid_choices = []
for i in range(1, len(available_parts) + 1 ):
    valid_choices.append(str(i))

print(valid_choices)
current_choice = "-"
computer_parts = []   # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int (current_choice ) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            #it's already in list
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append (chosen_part)

        print("your list now contains: {}".format(computer_parts))

    else:
        print("Please add options from the list below: ")
                                                                                # we could get index of each part and add one to it, to make our code easy

        for parts in available_parts:                                               # here we've used string fotmatting and replacement fields there, to display
            print("{0}: {1}".format(available_parts.index(parts) + 1, parts ))          #index no. and the part, & we're adding one to the index
                                                                                    # we want the 1st no. to be no. one(1) on the screen
    current_choice = input()
print(computer_parts)


# enumerate function:--
# Enumerate function returns each item, with its index position

# for number, parts in enumerate (available_parts):       # here (number) is the index position, and the (parts) is item name
#     print("{0}: {1}".format(number + 1, parts))


# for loop starts with word for, and then names of one or more variables. If the object that's iterated over contains more than one value,
# you can use more than one variable in the for loop, that's we're doing in tha above code (enumerate)

# enumerate returns pairs of values, we get index postition and the item, as a pair of values.
# enumerate function is very efficient way to get indexes as well as the value in a loop.




