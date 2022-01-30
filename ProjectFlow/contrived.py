# contrived --> hard to believe, not natural or realistic
numbers = [1, 45, 31, 16, 60]
for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")

    # here u should give attention to indentation for (else)
    # Here, else is associated with the for loop and not with the if statement.
    # it's called contrived example...




            # when our loop finds a value that's not acceptable, our code breaks out of the loop
            # that means the loop will only terminate normally if all the values are acceptable



















