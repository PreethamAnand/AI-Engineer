# def maa(a):
#     m = a[0]
#     for i in a:
#         if i > m:
#             m = i
#     return m

# a = list(map(int,input("Enter the list of numbers:").split()))
# m = maa(a)
# a.remove(m)
# m = maa(a)
# print("The second largest number is:", m)

# method 2
def maa(a):
    b = list(set(a))
    if len(b) < 2:
        return "No second largest number"
    b.sort(reverse = True)
    return b[1]

a = list(map(int,input("Enter the list of numbers:").split()))
m = maa(a)
print("The second largest number is:", m)