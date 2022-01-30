choice = "-"    # initialize choice to something invalid
while choice != "0":
    # if choice in "12345":
    # if choice in list("12345"):
    # if choice in set("12345"):
    if choice in {"1", "2", "3", "4", "5"}:
        print("You choose {}".format(choice))

    else:
        print("Please choose your option from the list below")
        print("1:\tLearn python")
        print("2:\tLearn java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()


# linear search - you start at the beginning, and check each item until you either find the one you want, or reach end
#       of the list.

# tight loop - is one that iterates many times, and has a significant impact on the total execution time.


