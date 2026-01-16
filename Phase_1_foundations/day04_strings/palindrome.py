s = input("Enter a string: ")
b = ""
for i in s:
    b = i + b

if s == b: 
    print("Palindrome")
else:
    print("Not a palindrome")