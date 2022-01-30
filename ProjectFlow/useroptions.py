
            # Program to take input from user, give options to user from 1 to 5, if user enters 0 program should terminate...
# 1ST Way to do this program

# print("Please choose option from the menu (below):")

# print("1: go for football")
# print("2: go for badminton")
# print("3: go for running")
# print("4: go for tennis")
# print("5: go for cricket")
# print("0: exit your events")
#
# while True:
#     choice = input()
#
#     if choice == "0":
#         print("You choose 0")
#         break
#
#     elif choice in "12345":
#         print("you choose {}" .format(choice))
#
#
#     else:
#          print("Go to home")



# 2nd way to do this program.....
# choice = "-"
# while True:
#     if choice == "0":
#         print("You choose 0")
#         break
#
#     elif choice in "12345":
#         print("you choose {}" .format(choice))
#
#     else:
#         print("Please choose option from the menu (below):")
#
#         print("1: go for football")
#         print("2: go for badminton")
#         print("3: go for running")
#         print("4: go for tennis")
#         print("5: go for cricket")
#         print("0: exit your events")
#     choice = input()





# 3rd way to do this program ....

choice = "-"
while choice != "0":

    if choice in "12345":
        print("you choose {}" .format(choice))

    else:
        print("Please choose option from the menu (below):")

        print("1: go for football")
        print("2: go for badminton")
        print("3: go for running")
        print("4: go for tennis")
        print("5: go for cricket")
        print("0: exit your events")
    choice = input()





