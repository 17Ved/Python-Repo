# Reading & Writing Binary files in Python -----
# Reasons to use Binary files --
#   1. Either we're processing binary data, such as an image file...
#   2. Or we might want to store the variables in our program, so we can load then back in later...
# The basic principles of reading & writing text files can be applied here, in principle, in both cases.
# Creating a binary file is just as easy as writing a text file.
# Just specify the mode as 'b' for binary.
# IMP -- Strings and Integers cannot be directly written to a binary file.
# They need to be converted to a format called 'Bytes' first.
# We can do this by using 'bytes()' built in function.
# And then the to_bytes method of integer objects
# We need to put the 'b' as well as 'w' for write mode, for binary files
# Bytes work little strangely, if you pass an integer to it, it creates a sequence with that many bytes, all set to zero.

# with open("binary", 'bw') as bin_file:              # 'bw'-- for binary writing & 'br'-- for binary reading
#     for i in range(17):
#         bin_file.write(bytes([i]))                # so, we're converting the number 'i' to a bytes format, & then writing that to our binary file.
#         # bin_file.write(bytes(range(17)))                # so, we're converting the number 'i' to a bytes format, & then writing that to our binary file.
#
# with open("binary", 'br') as binFile:
#     for b in binFile:                               # we're using bin_file & binFile as an identifier & then .write method to write our bytes our in that order.
#         print(b)


a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 10 00 00
x = 2998302     # 00 2D C0 1E

with open("binary2", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))


# Parameters for using to_bytes() method --- first one number of bytes we want, & second is whether to return the result as big endian or little endian
# endian --- In computing, endianness is the order or sequence of bytes of a word of digital data in computer memory. Endian ness is primarily expressed as 'big-endian' or 'little-endian'.
# 'Little' and 'Big' endian are two ways of storing multibyte data-types ( int, float, etc). In little endian machines,
# last byte of binary representation of the multibyte data-type is stored first. On the other hand, in big endian machines,
# first byte of binary representation of the multibyte data-type is stored first
# Big endian stores the most significant byte first with the remaining bytes of the number following the order
# Little endian is the reverse of this, it shows the least significant byte being stored first
#

with open("binary2", 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print(i)

































































