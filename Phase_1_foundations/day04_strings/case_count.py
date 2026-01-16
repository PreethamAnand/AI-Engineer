a = input("Enter string: ")
l,u = 0,0
for i in a:
    if i.islower():
        l += 1
    elif i.upper():
        u += 1
print("Lowercase letters count: ",l)
print("Uppercase letters count: ",u)