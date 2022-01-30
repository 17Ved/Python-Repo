# *args --->
# you can use (*) to unpack any sequence type
#
# numbers = (0, 1, 2, 3, 4, 5)
# print(numbers, sep=";")
#
# print(*numbers, sep=";")        # here, *numbers is unpacked, and then the unpacked values passed to print function


def test_star(*args):          # here, we're providing *args as a parameter, which means it represents an unpacked tuple
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()








