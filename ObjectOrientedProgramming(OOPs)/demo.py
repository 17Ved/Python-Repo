# Raw String ---
# Python raw string is created by prefixing a string literal with 'r' or 'R'.
# Python raw string treats backslash (\) as a literal character.
# This is useful when we want to have a string that contains backslash and don't want it to be treated as an escape character.

a_string = "This is\na string split\t\t and tabbed"
print(a_string)

raw_string = r"This is\na string split\t\t and tabbed"
print(raw_string)

b_string = "this is " + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

error_string = r"this string ends with \\"

