a = list(input("Enter a sentence: ").split(" "))
l = ""
for i in a:
    if len(i) > len(l):
        l = i
print("Longest word is: ",l)