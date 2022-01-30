# Tuples :----
# a tuple is a mathematical name for an ordered set of data
# tuple is another sequence type, along with strings, list and ranges
# Tuples are different from lists because tuples are immutable. That means they can't be changed after they're created - just like strings


# t = "a", "b", "c",          # you can define tuple by putting parantheses t = ("a", "b", "c") ---optional
# print(t)                # this will print in (parantheses), instead of square brackets
#
# name = "tim"
# age = 10
# print((name, age, "python", 2020))       # NOte ---> parantheses must be used, when you pass a tuple literal as an argument to a function


# IMP Points ---> tuples are sequence type, which means we could use indexing, to access the individual items in the tuple.
# indexing a tuple works the same as indexing a string or a list

#
# albums = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# # print(metallica)
# # print(metallica[0])
# # print(metallica[1])
# # print(metallica[2])
# # # metallica [0] = "master puppets"          #you'll get error on this line, 'cause tuples are immutable
# #
# # metallica2 = list(metallica)            # here, the list function returns a list using the values in the iterable that's passed to it
# # print(metallica2)                       # so, now we can change the "metallica" title to "master puppets"
# # metallica2[0] = "master puppets"
# # print(metallica2)
#
#
# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
#
# table = ("Coffee table", 200, 100, 75, 34.60)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)


# remember that you can unpack values form a list, as long as you're sure that the size of the list won't be changed


albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning","Metallica", 1984),
          ]

print(len(albums))
#
# for album in albums:
#     print("Album: {}, Artist: {}, Year: {}"
#           .format(album[0], album[1], album[2]))

# Or

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
















