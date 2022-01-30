from nested_data import albums          # so that'll include the definition of our albums list, into our jukebox_menu program
                                        # the list is defined in nested_data, but we've now made it available in this program as well.

# NOTE :- When you import another file, python executes all the code in that file


SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    #print("Please choose your album(invalid choice exits)")
    # for index, title, artist, year, songs in enumerate(albums):       # so we're using for loop to iterate over the albums.
    #     print("{}, {}, {}, {}, {}"                                      # we also want the index numbers.
    #           .format(index + 1, title, artist, year, songs))

    # for index, value in enumerate(albums):          # if enumerate only returns two items, then we can only unpack two items in the for loop.
    #     print(index, value)                         # here there index position will printed first, then each tuple...
    # break

    print("Please choose your album(invalid choice exits)")
    for index, (title, artist, year, songs) in enumerate(albums):       # so we're using for loop to iterate over the albums.
        print("{}, {}".format(index + 1, title))                             # we also want the index numbers.

    choice = int(input())
    if 1 <= choice <= len(albums):                                # this line is checking whether the entered value is within the required range.
        songs_list = albums[choice -1][3]                            # our valid choice is from 1 to length of the albums list.
        #songs_list = albums[choice - 1][SONGS_LIST_INDEX]                 # we got 4 albums, so any value greater than 4 is invalid
    else:                                                                     # line no.22 is binding a variable called songs_list to the list of songs for the selected albums.
        break

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):           # we're putting parentheses around track number and song, because
        print("{}: {}" .format(index + 1, song))                        # these are the values that are being unpacked from the tuple



    song_choice = int (input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))

    print("=" * 40)


    # print(albums[choice -1])
    # print(songs_list)
    # print()










    #
    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value              # here this line is unpacking the value tuple into our four variables
    #     print(index, title, artist, year, songs)
    # break










# Constants - A constant is a value that doesn't change
# mathematical and the physical sciences use lots of constants
# ex - pi = 3.14
# constants must not be changed
# In python there's a convention that constants should have names that are all in capitals








































