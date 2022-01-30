x = 23
                            # augmented assignment are easier to type and as they're more efficient
x += 1      #24             # concatenation & repition can also be performed using aa
print(x)

x -= 4      #20
print(x)

x *= 5      #100
print(x)

x //= 4     # 25
print(x)

x /= 5      #5.0- note conversion from int to float
print(x)

x **= 2     # 25.0 - x still represents a float
print(x)

x %= 5      # 0.0 - 25 is exactly divisible by 5
print(x)

greeting = "Good "

greeting += "Morning "
print(greeting)

greeting *= 5
print(greeting)

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(8):
    answer += 5

print(answer)

