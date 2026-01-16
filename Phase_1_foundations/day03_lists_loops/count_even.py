l = list(map(int, input("Enter the list elements: ").split()))
m = l[0]
print("Even numbers are: ", end="")
for i in l:
    if i%2==0:
        print(i,end=" " )
        