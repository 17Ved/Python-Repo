# continue and break statements ---->  if u may need to interrupt the normal flow of a loop, to either jump out of it
# completely, or stop th current iteration and move on to the next one.

# list is an ordered sequence of values, enclosed in square brackets

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)


# for item in shopping_list:
#     if item == "spam":
#         continue
#
#     print("Buy " + item)



                        # break statement

for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)










