a = input("Enter string: ")
for i in a:
    if i == " ":
        a = a.replace(" ","")

print("String after removing spaces:",a)