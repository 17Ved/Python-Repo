# So, the process for writing data to a text file is very similar to reading from it.
# when files opened this time the mode is 'w' for write instead of 'r' for right.
# Now the actual data is written using the print function exactly as you want to display on the screen, but this time we specify file object to send it to and goes to the file.
# It's very imp to close the file when you're finished
#

# cities = ["Adelaide", "Alice springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file, flush=True)         # don't give space before '=' sign on this line & after '=' also. Here '=' is used to provide a name document in place of the file parameter.

# Flush ----
# Data is actually written to buffer and then the contents of the buffer is transferred to the external device in the background...
# Closing the file causes the buffer to be flushed automatically.
# But if u want to ensure your data's written sooner, u can pass 'flush' = True to cause the data to be written immediately.
# What is flush in Python --- The flush() method in Python file handling clears the internal buffer of the file. In Python, files are automatically flushed while closing them.
# However, a programmer can flush a file before closing it by using the flush() method


# cities = []
#
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))         # in output additional new line characters can appear, so for that we can use strip() function, from a string to remove those characters from a string.
#                                                 # What strip does, it removes characters from the beginning or end of a string & only from the beginning or end.
# print(cities)
# for city in cities:
#     print(city)


# Anything that u can print out on screen can be written to a text file, However, it's not always possible to read it back in the original form.
#
# imelda = "More Mayhem", "Imelda day", "2011", (
#     (1, "Pulling the Rug"), (2,"Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)


with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)     # python have eval() to evaluate any expression to a string passed to it, we could get the contents back from the file into a tuple variable by using eval.

print(imelda)
title, artist, year, track = imelda
print(title)
print(artist)
print(year)


# Appending to files
# We can append to a text file by using an 'A' as the mode for append. Now, opening a text file in append mode caused data to be written to the end of the file without overriding the existing contents.
# These three modes are short for RT, WT, AT.
# T stands for Text mode which is the default.
# The default is auto is set to 'RT' to open a file, a text file, for reading...
# But it's also possible to open a file for both reading writing by using plus, but that doesn't replace 'r' or 'w', so you have to use 'r' plus or 'w' plus
#























