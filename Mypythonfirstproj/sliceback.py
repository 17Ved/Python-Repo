            # slicing backwards
letters = "abcdefghijklmnopqrstuvwxyz"
                  # starts index at (25) , stop value is (0) , step of (-1)
backwards = letters[25::-1]                                               #backwards = letters[25:0:-1]
print(backwards)                                # NOTE :-- here start value must be greater than the stop value
                                            # our slice starts at index position (25), and it extends to the position to (0),
                                            # but doesn't include the character at that position(0). We're stepping by (-1),
                                         #which produces all the letters from (z) down to (b)

backwards = letters[::-1]

# create a slice that prosuces the characters (qpo)
backwards = letters[16:13:-1]
print(backwards)

# slice the string to produce (edbca)
backwards = letters[4::-1]
print(backwards)

# slice the string to produce the last 8 characters, in reverse order  (zyxwvuts)
backwards = letters[26:17:-1]    # or letters[-9:-1]
print(backwards)

  #What will this program print?

#days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
#print(days[::5])                                   # Idioms in python
                                                    # 1. ::-1  ----> reversing the sequence
    #output will be -- MTWTFSS                      #2.        ---->return the last n items in a sequence
                                                    # if [::5]    The slice starts at the first character, and includes every 5th character.


print(letters[-4:])
print(letters[-1:])
print(letters[1:])               # this will print letters except 1
print(letters[:1])              # this will print only letter No.(1) i.e --> a
print(letters[0])








