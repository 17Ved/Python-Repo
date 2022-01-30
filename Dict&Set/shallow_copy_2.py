lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]
animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

print(animals)
things = animals.copy()     # on this line we use, copy method to create a copy of the original dictionary
                            # any changes we make to animals isn't reflected in the things dictionary, and that's because now, things is a new dictionary created by copying animals
# animals["teddy"] = "toy"
print(things["teddy"])
print(animals["teddy"])
# if we want to separate dictionaries, we should create a copy.

print()

# things["teddy"].append("toy")
things = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}
teddy_list.append("toy")
animals["teddy"].append("added via`animals`")
things["teddy"].append("added via`things`")
print(things["teddy"])
print(animals["teddy"])
print(teddy_list)


# a shallow copy copies the references. It doesn't make a copy of the things that are being referred to
# if you need to create a deep copy of an object. Python has a copy module that you can use
# the copy module provides a deep copy function




























