age = int(input("how old are you"))

#if age >= 16 and age <=65:              # the complete expression will only be true with both parts true  ---> and
#if 16 <= age <=65:                       # here, age is in the range of 16 to 65, this condition is same as the previous one but it's phrased in a more understandable way
if age in range(16,65):
    print("Have a good at work")                  #if age >= 16 and age <=65:  or
                                                    # if 16 <= age <=65:  or
else:                                                  # if age in range(16,65):
    print("Enjoy your free time")
print("-" * 80)

if age < 16 or age > 65:
    print("enjoy your free time")

else:
    print("have a good day at work")


                # simply chained comparisions...
            # when comparing conditions using (and) python will stop checking as soon as it finds a condition that is False.
            # when comparing conditions using (or), it will stop as soon as it finds one that is True.



