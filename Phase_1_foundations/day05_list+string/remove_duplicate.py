a = list(input("Enter the list elements: ").split())
b = []
for i in a:
    if i not in b:
        b.append(i)
print("List after removing duplicates:", *b)