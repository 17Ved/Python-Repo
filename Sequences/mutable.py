# Mutable objects in python:-
# list, dict, set, Bytearray
# we can change value of mutable objects, without the object being destroyed and recreated


shopping_list = ["milk",
                 "eggs",
                 "pasta",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]         # here we're adding/mutating "cookies" to the shopping_list
print(shopping_list)
print(id(shopping_list))            #here id will remain unchanged, because lists are mutable & python was able to add a new item to the end of the list,
                                    # without creating a new list


                            # Imp Points --->
                                # strings are immutable. When we tried to change a string, python created a new object- a new string and re attached the name to it.
                                # Lists are mutable- they can be changed. When we appended a new item, python was able to change the contents of the list, without creating a new one.

a = b = c = d = e = f = another_list            # chain assignments

print(a)

print("Adding cream")
c.append("cream")           # here we'll get cream added to another_list, no matter which of the names we use to refer to it, we've got cream
print(b)                    # here we use 'c' to append 'cream' to the list
print(d)












