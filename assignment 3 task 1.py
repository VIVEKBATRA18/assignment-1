a = int(input("enter the number"))

def factorial(n):

    if n < 2:
        return 1
    else:
        return n*(factorial(n-1))

result = factorial(a)
print("the factorial of",a ,"is :",result)









