a = int(input("Enter a number: "))
f = 1
while a != 0:
    f *= a
    a -= 1
print("Factorial is:", f)