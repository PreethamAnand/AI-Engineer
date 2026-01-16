def add(a,b):
    print("Sum:", a+b)
    guidlines(add)
def subtract(a,b):
    print("Difference:", a-b)
    guidlines(subtract)
def multiply(a,b):
    print("Product:", a*b)
    guidlines(multiply)

def calculator():
    n = input("Enter the operation to be performed (+, -, *): ")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if n == '+':
        add(a, b)
    elif n == '-':
        subtract(a, b)
    elif n == '*':
        multiply(a, b)
    else:
        print("Invalid operation")

def guidlines(n):
    help(n)
if __name__ == "__main__":
    calculator()