a = int(input("Enter a number: "))
rev = 0
while a != 0:
    d = a % 10
    rev = rev *10 + d
    a = a//10
print("Reversed number is: ",rev)
