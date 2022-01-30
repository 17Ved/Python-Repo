# split() method ---> so the split method splits a string up into words.

pangram = """The quick 
brown fox jumps\tover
the lazy dog"""

words = pangram.split()         # we use this, we'll get a list containing all the words in the sting
print(words)

numbers = "9, 223,372, 036, 854, 775, 807"          # remember that when you split a sting, you get list of strings
print(numbers.split(","))

generated_list = [
    '9', ' ',
    '2', '2','3 ', ' ',
    '3', '7','2 ', ' ',
    '0', '3','6 ', ' ',
    '8', '5','4 ', ' ',
    '7', '7','5 ', ' ',
    '8', '0','7 ']


values = "".join(generated_list)
print(values)


values_list = values.split()
print(values_list)


#replace the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)


# create new list

integer_value = []
for value in values_list:
    integer_value.append(int(value))

print(integer_value)

# ********************************************************************************************************************
# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)




























