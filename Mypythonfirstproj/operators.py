
a = 12                          # NOte -->> you can't have an expression on the left of an assignment
b = 3                           # the expression on the right of the equals sign is evaluated & the variable on the left is bound to the result
print(a + b)    #15
print(a - b)    #9
print(a * b)    #36
print(a / b)    #4.0
print(a // b)   #4 integer division, rounded down towards minus infinity
print(a % b)    #0 modulo: the remainder after integer division

print()

for i in range (1, a // b):              #   this will create error  (a / b)
    print(i)                             #    TypeError: 'float' object cannot be interpreted as an integer


print(a + b / 3 - 4  * 12)
print(a + (b/3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4)*12)


c = a + b
d = c / 3
e = d - 4
print(e *12)


# Operator precedence  acronyms  ----->
# PEDMAS  Paranthses, Exponents, MUltiplication/Division, Add/Sub
# BEDMAS  Brackets, Exponents, Division/Multi, Add/Sub
# BODMAS  Brackets, Order, Division/Multi, Add/Sub
# BIDMAS  Brackets, Index, Division/Multi, Add/Sub

print()

print(a / (b * a) / b)



















