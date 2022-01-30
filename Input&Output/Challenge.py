# Appending to files
# We can append to a text file by using an 'A' as the mode for append. Now, opening a text file in append mode caused data to be written to the end of the file without overriding the existing contents.
# These three modes are short for RT, WT, AT.
# T stands for Text mode which is the default.
# The default is auto is set to 'RT' to open a file, a text file, for reading...
# But it's also possible to open a file for both reading writing by using plus, but that doesn't replace 'r' or 'w', so you have to use 'r' plus or 'w' plus

# Challenge ------>

# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6).

# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24
#  --------------------


# with open("C:/Users/vedan/Desktop/sample.txt", 'a') as tables:
#     for i in range(2,13):
#         for j in range(1,13):
#             print("{1:>2} times {0} is {2}.".format(i, j, i * j), file=tables)
#         print("_" * 20, file=tables)


with open("C:/Users/vedan/Desktop/sample2.txt", 'w') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}.".format(i, j, i * j), file=tables)
        print("_" * 20, file=tables)





