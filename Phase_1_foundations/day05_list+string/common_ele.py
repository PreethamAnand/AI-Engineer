a = list(map(int, input("Enter the list of numbers: ").split()))
b = list(map(int, input("Enter the list of numbers: ").split()))
c = []
for i in a:
    if i in b and i not in c:
        c.append(i)
print("Common elements are:", *c)
