s = input("Enter a string: ")
s.lower()
v = 'aeiou'
c = 0
for i in s:
    if i in v:
        c += 1
print("Number of vowels: ",c)