 # in and not in
parrot = "Norwegian Blue"

letter = input("Enter a character:")

if letter in parrot:                                # value 'a' and line 5 checks of the letter appeared in parrot sting
    print("{} is in {}".format(letter, parrot))         # note that string comparisons are case- sensitive  if u enter 'A' it won't be found on the string
else:                                               # you can also check sequence of characters like a word -- "blue"
    print("I don't need that letter")













