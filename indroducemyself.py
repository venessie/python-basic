def intro(name,age):
    print("My name is",name +",and I am",age)
n = input("Enter your name")
a = int(input("Enter your age"))
intro(n,a)







def factorial(f):
    if f ==1:
        return f
    else:
        return f*factorial(f-1)
a = int(input("Enter a Postive, Whole number"))
print(factorial(a))





def add(a,b):
    return a + b
3
def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

num1 = int(input("Enter a positive, whole number."))
num2 = int(input("Enter another positive, whole number."))
print(add(num1,num2))
print(sub(num1,num2))
print(mul(num1,num2))
print(div(num1,num2))

 