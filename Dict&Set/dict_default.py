from contents import pantry

# .setdefault() method returns the value of a key, if the key exists in the dictionary


chicken_quantity = pantry.setdefault("chicken", 0)
print(f"Chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)          # on this line because beans wasn't in the dictionary,
print(f"beans: {beans_quantity}")                # setdefault returned the default value that we specified on line 6 (0)


ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup : {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")     # here (zucchini is key, and eight is value)
print(f"zucchini: {z_quantity}")

# here the difference between .get() and .setdefault() method is
# .setdefault() method doesn't just return the default value- it adds the key to the dictionary as well.
# when it adds the key, it uses the default value as the value to store in the dictionary.
# the default value doesn't have to be a number - u can use anything that can be stored in the dictionary.
# .get() on the other hand returns the item with the default value. it doesn't add it to the dictionary.

print()
print("`pantry` now contains")

for key, value in sorted(pantry.items()):
    print(key, value)

































