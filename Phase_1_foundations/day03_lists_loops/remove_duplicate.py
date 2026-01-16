l = list(map(int, input("Enter the list elements: ").split()))
m = []
print("List without duplicates: ", end="")

for i in l:              
    if i not in m:       
        m.append(i)      
        print(i, end=" ")