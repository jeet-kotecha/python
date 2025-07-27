# types of udf in python (no agrument and with return type)
def add():
    return a+b
def sub():
    return a-b
def mul():
    return a*b
def div():
    return a/b

    

a=float(input("Enter no.1:"))
b=float(input("Enter no.2:"))

print("sum of a nad b is: ",add())
print("subtraction of a and b is:",sub())
print("multiplication of a and b is:",mul())
print("division of a and b is:",div())