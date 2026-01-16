a = list(map(int,input("Enter the list of numbers: ").split()))

for i in range(1,len(a)):
    for j in range(len(a)-i-1):
        if a[j+1] < a[j]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted list is:",*a)