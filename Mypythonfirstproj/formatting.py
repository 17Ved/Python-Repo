                # string formatting

for i in range(1,13):
    print("No. {0:2} sqaured is {1:4} and cubed is {2:4}" .format(i, i ** 2, i ** 3))
                                                        # we're using 0:2 for the first replacement field
                                                        # 2 is the field width & it's seperated from the index with a colon,
                                                        #everything in that first column prints in a width of two characters, so it's reserving
                                                        # 2 spaces on the screen
print()
for i in range(1,13):
    print("No. {0:2} sqaured is {1:<3} and cubed is {2:<4}" .format(i, i ** 2, i ** 3))     # to align these spaces at the left side use ( < )
                                                                                            # (<) left align, (>) right align, (^) caret centers

for i in range(1,13):
    print("No. {0:2} sqaured is {1:4} and cubed is {2:^4}" .format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12}".format(22 / 7))                          # general format defaults to print 15 decimals
print("Pi is approximately {0:12f}".format(22 / 7))                         # when we specify floating point (f) we get the defaults of 6 digits after decimal point
print("Pi is approximately {0:12.50f}".format(22 / 7))                      # from line 19 to 22 we also add precision of 50, that gives (50) points
print("Pi is approximately {0:52.50f}".format(22 / 7))                      # after decimal point
print("Pi is approximately {0:62.50f}".format(22 / 7))                      # here python will ignore value (12 -- specified for width) on line 19
print("Pi is approximately {0:72.50f}".format(22 / 7))                      # python won't truncate a no. we can't put value that got 50 decimals in
print("Pi is approximately {0:<72.50f}".format(22 / 7))                       # a field width 12



for i in range(1,13):
    print("No. {} sqaured is {} and cubed is {:4}" .format(i, i ** 2, i ** 3))          # :4 shows that you can still use a colon to control the layout
                                                                                        # even you haven't sepecified field no.

