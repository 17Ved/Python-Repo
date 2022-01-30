# .join method() ---> it's useful for producing output from a list, and can be used with iterable
# the join method actually takes care of iterating for us, we give it iterables and it joins all the items in the iterable.

flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",

]

# for flower in flowers:
#     print(flower)

seperator = " | "
output = seperator.join(flowers)        # here .join will iterate over the flowers list and create sting containing each flower sepearated by space bar( | ) space
print(output)                           # we don't have to use for loop here, join method() iterates over the list for us
                                        # it creates a string from a list, and separates each item with the string that it's called on.

print(", ".join(flowers))               # all the items in the iterable must be strings, if u want to join the items
                                        # for.ex--> u can't provide int value in the list "flowers" ,, the code will crash












