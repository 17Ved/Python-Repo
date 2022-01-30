#the str string data type
         #012345678901234   (+) plus
parrot = "Norwegian Blue"
         #43210987654321    - (minus)

print(parrot)

print(parrot[3])  #printing individual charachters from string
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

# Negative indexing in python ---->

print()

print(parrot[-1])
print(parrot[-14])


print(parrot[-11])    #printing individual charachters from string using (-) negative string
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

        # another way to do that  (- negative string)
print()
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])



# slicing concept        #Note -->  if u don't provide start value u still need a colon (:)
print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[0:9])  #same result  --> Norwegian
print(parrot[:9])   #same result  --> Norwegian

print(parrot[10:14])    #same result
print(parrot[10:])      #same result

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])    # slice will start from beginning and extend right up to the end


# slicing with -ve numbers

print(parrot[-4:2])      # u can't go backwards from the starting position

print(parrot[-4:-2])   #Bl
print(parrot[-4: 12])  #Bl

print(parrot[-14:-8])

# use step in slice
print(parrot[0:6:2])   #Nre
print(parrot[0:6:3])   #Nw

number = "9,223;372:036 854,775;807"
             #starts at position 1 & then slicing every fourth character

seperators = number[1::4]
print(seperators)


values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])





