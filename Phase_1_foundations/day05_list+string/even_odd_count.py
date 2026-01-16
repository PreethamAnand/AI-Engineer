a = list(map(int,input("Enter the list elements: ").split()))
ec = 0
oc = 0
for i in a:
    if i%2 == 0:
        ec += 1
    elif i%2 != 0:
        oc += 1
print("Even count:", ec )
print("Odd count:", oc)