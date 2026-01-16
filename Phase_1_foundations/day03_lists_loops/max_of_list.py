l = list(map(int, input("Enter the list elements: ").split()))
m = l[0]
for i in l:
    if i>m:
        m = i
print("Maximum element is:", m)