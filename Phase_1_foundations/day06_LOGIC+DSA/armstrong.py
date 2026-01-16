a = int(input("Enter a number: "))
b = 0
c = a
while a != 0:
    d= a%10
    b = b*10 + d
    a = a//10
if b == c:
    print(c, "is an Armstrong number")
else:   
    print(c, "is not an Armstrong number")