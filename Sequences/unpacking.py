a = b = c = d = e = f = 42
print(c)
x, y, z = 1, 2, 17
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 1, 2, 17             # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

# you can unpack any sequence types
print("Unpacking a list")

data_list = [12, 13, 14]        # here we have list containing 3 items, & we can unpack them into 3 variables...
# data_list.append(15)           # this will give error

p, q, r = data_list
print(p)
print(q)
print(r)

# you can always unpack tuples successfully






















