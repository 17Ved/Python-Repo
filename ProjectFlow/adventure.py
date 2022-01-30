available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction")
    if chosen_exit.casefold() == "quit":
        print("game over")
        break                           # here we don't want to display (aren't u glad) msg if player enters quit, that can be done using (else) statement
else:                                   #code in the else block will only be executed if the loop terminates normally. It won't be executed if we break out of the loop
    print("aren't you glad you got out of there")

            # imp feature of while loop ---> that they can be used when yu can't determine, in advance, how many times you will need to loop
            # with the while loop u don't need to know how many times the loop will execute.
            # a while loop can be used to keep reading, until there is no more data left



# break and continue statements
#to break out a while loop, or to stop the current iteration & test the condition again.





