low = 1
high = 1000

print("Please think number between {} and {}".format(low, high))
input("Press Enter to start")

guesses = 1
while low != high:
    print("\tGuessing in the range of {} to {}" .format(low,high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. should I guess higher or lower?"
                     "Enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The lower wnd of the range becomes 1 greater than the guess.
        #pass
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range between one less than the guess.
        #pass
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break

    else:
        print("Please enter h, l or c")                 # NOTE: you should have valid code inside blocks, the only comment won't count...

    # guesses = guesses + 1

    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))









# NOTE ---> pass keyword - it makes the code syntactically correct, it works like dummy code

#python dosen't have case or switch statements


# augmented assignment sounds really fancy but it's just a shorthand way of assigning values to a variable
