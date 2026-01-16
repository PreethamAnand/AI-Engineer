a = input("Enter string: ")
c = 0
for i in a:
    if i.isalpha():
        c += 1

print("Number of words: ",c)