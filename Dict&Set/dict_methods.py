d = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}


pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

v = d.values()
print(v)

d[10] = "ten"
print(v)

print("Four" in v)
print("Eleven" in v)

keys = list(d.keys())
values = list(v)        # --> list(d.values())
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print()
for key, value in d.items():
    if values == "four":
        print(f"{d[key]} was found with the key {key}")

# code for "the dict `update` method" lecture
# d2 = {                              # here the value is changed for key 7,10,3 but value of these keys remained same
#     7: "Lucky seven",
#     10: "Ten",
#     3: "This is the new three"
# }
#
# d.update(d2)
# for key, value in d.items():
#     print(key, value)
#
# print()
#
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)


# Code for "The remaining `dict' methods" lecture.
# new_dict = dict.fromkeys(pantry_items, 0)      # here we use dict.fromkeys to call the method
# print(new_dict)                             # the dictionary class is called dict, and we're using that class to call the fromkeys method
#                                             # passing iterable to method (pantry_items)
# keys = d.keys()
# print(keys)
#
#
# for item in d:          # or u can use d.keys()
#     print(item)

























