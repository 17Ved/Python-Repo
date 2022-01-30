# Serialization - Process that allows objects to be saved to a file, so that they can be stored or restored


# Pickling - Python pickle module is used for serializing and de-serializing a Python object structure. ... Pickling is a way to convert a python object (list, dict, etc.) into a character stream.
# The idea is that this character stream contains all the information necessary to reconstruct the object in another python script
# Pickling is fun for storing your program's data but shouldn't be used when dealing with data from untrusted sources such as over the internet...
# Pickling is useful when storing and retrieving your own data
# Drawback of Pickling -
# The object all have to be loaded back into memory into the computer's memory...if you're dealing with large amount of objects for ex. dictionary then loading that in entire thing to memory may not be a ralistic option.
# Python has an alternative for the above problem that's the 'Shelve Module'.

# Python provides a mechanism for serializing objects called pickling(Pickle)
# So when the object is pickled, and it's written to a file & format that contains the object's data together with sufficient information to allow that object to be created when it's loaded back in.

import pickle
#
# imelda = ("More Mayhem",
#           "Imelda May",
#           "2011",
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
#
# with open("imelda.pickle", 'wb') as pickle_file:            # we 1st have to import the pickle module to be able to use it. So, it can be saved with a single call as you saw using the pickel.dump() method.
#     pickle.dump(imelda, pickle_file)

# We can load our abject back easily with pickle.load() method


# with open("imelda.pickle", 'rb') as imelda_pickled:         # so, that's now reading the data out of the imelda.pickle file
#     imelda2 = pickle.load(imelda_pickled)
#
# print(imelda2)
#
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
#
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)


# Once you can open the file for writing, we can literally pick as many objects as we want to in that one file.


imelda = ("More Mayhem",
          "Imelda May",
          "2011",
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)        # that's protocol (0), but there's always protocol version (1)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(299302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

with open("imelda.pickle", 'rb') as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)


print(imelda2)

album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)

for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print('=' * 40)

for i in even_list:
    print(i)

print('=' * 40)

for i in odd_list:
    print(i)

print('=' * 40)

print(x)

# The objects themselves must be read back in the same order that they're written.


# 'Protocols' in Python -
# There's few objects in python that can't be saved by pickling them. When you're pickling objects to save to a file, you can choose from one which (different) protocols that python is going to use
# when serialising the data.
# The protocol used to pickle objects can be determined by python automatically.
# So, it's not necessary to specify a protocol when using pickle.load() method.
# In fact, you can use different protocols in the same file...





















































