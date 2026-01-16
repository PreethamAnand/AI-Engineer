s = input("Enter a string: ")
s = s.lower()
v = 'aeiou'
c = 0
for i in s:
    if i not in v :
        if i.isalpha():
            c += 1
print("Number of consonants: ",c)