                                            #    (sequence) string operators

# pyhton has 5 sequence types built in: the string type, list, tuple, range, bytes and bytearray
# sequence is defined as an ordered set of items
# range is an example of a sequence that can't be concatenated

string1 = "he's "
string2 = "probably "
string3 = "pinning "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably "  "pinning "  "for the "  "fjords ")
print("hello "  * 5)                                              # repeats a sequence no. of times (*)

print("Hello " * (5 + 4))                                   # can only concatenate str (not "int") to str

print("Hello " * 5 + "4")


                                            # to check if one string is a sub-string of another, we actually check if one thing is in another...

today = "friday"
print("day" in today)       #true                           # "in" operators evaluates to true if the first thing exists in the second
print("fri" in today)       #true
print("thur" in today)      #false
print("parrot" in "fjord")  #false











