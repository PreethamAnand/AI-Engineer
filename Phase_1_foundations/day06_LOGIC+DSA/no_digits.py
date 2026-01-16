a = int(input("Enter a number: "))
c = 0
while a>0:
    d = a % 10
    c += 1
    a = a//10
print("Number of digits:", c)