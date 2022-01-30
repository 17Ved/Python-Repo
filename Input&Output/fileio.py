# File Input & Output in Python ---
# we're going to learn how to read and write text files and also how to look read and write binary files using pickle &
# shelve which are tools that are part of python.
# so, input and output just means getting data into a program and getting it out again.

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Reading Text Files -
# 1st we have to open the file using --function called Open()
# 2nd is to read in the file which we can do either on, line at a time or we can actually try and read in the entire file in one go.
# 3rd is to close the file when we're done with it is the final step.


# jabber = open("C:/Users/vedan/Desktop/sample.txt", 'r')     # path to open the file     # we need to provide mode as well  --- when you're opening a text file or file on your computer you need to
#                                                                                    # tell it what type of input output you want.     # specify full path if you're on windows machine
#
# for line in jabber:             # cycling through each line in the document, then we're printing it at the same time...
#     if "jabberwock" in line.lower():
#         print(line, end="")
#
# jabber.close()              # and then we closed the file when we're done...


# Python has 'with' statement
# 'with' will tidy everything up automatically once the object's no longer needed.

#
# with open("C:/Users/vedan/Desktop/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():                               # now , there's no need to explicitly close the folder this time because the 'with' takes care of that for us.
#             print(line, end='')


# read, read line, read lines ---

with open("C:/Users/vedan/Desktop/sample.txt", 'r') as jabber:      # Readline -- method returns one line from the file.
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()


# Read Lines ---            # reads the entire file in one go.
with open("C:/Users/vedan/Desktop/sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end='')


with open("C:/Users/vedan/Desktop/sample.txt", 'r') as jabber:      # Readlines -- also reads the entire file, but gines a list of strings rather than just a single string.
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')


with open("C:/Users/vedan/Desktop/sample.txt", 'r') as jabber:      # read -- is more useful dealing with binary files.
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')































