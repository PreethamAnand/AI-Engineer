def fibo(n):
    a,b = 0,1
    for i in range(n):
        print(a,end=',')
        a,b = b,a+b
    return a

a = int(input("Enter a number: "))
print("The Fibonacci sequence up to", a, "is:")
fibo(a)