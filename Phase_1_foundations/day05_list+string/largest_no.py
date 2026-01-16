a = list(map(int,input("Enter the list of numbers:").split()))
m = a[0]
for i in a:
    if i > m:
        m = i
print("The largest number is:", m)