                        #string replacement feilds

age = 24
print("My age is {0} years ".format(age) )              # so the replacement fields is represented by the {0}
                                                        # which is then  replaced by the first value in the format list
print("There are  {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul","Aug", "Oct", "Dec"))                            # python allows u to split your lines into the code

print("There are {0} days in jan, feb, mar, april, may, jun, july" .format(31))

print("Jan {2}, Feb {0}, Mar {2}, Apr {1}, May {2}, Jun {1}, Jul {2}, Aug {0}, Sep {1}, Oct {2}, Nov{1}, Dec{2}"
      .format(28,30,31))                                        # replacement feild (0) it's replaced with the first value in the list (28), 1 with 30, 2 with 31

print()

print("""Jan {2}
Feb {0}
Mar {2}
Apr {1}
May {2}
Jun {1}
Jul {2}
Aug {0}
Sep {1}
Oct {2}
Nov{1}            
Dec{2} """.format(28,30,31))
                 #0  1  2    --- index numbers














