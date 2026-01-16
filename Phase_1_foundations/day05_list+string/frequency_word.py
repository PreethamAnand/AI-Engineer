# a = list(input("Enter a string: ").split())
# b = {}
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1

# print("Word frequencies:")
# for k, v in b.items():
#     print(f"{k}: {v}")        

a = input("Enter a string: ")
b = {}   

for ch in a:
    if ch in b:
        b[ch] += 1
    else:
        b[ch] = 1

print("Character frequencies:")
for k, v in b.items():
    print(f"{k} - {v}")