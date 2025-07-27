# first code of exception handling in python
a=int(input("Enter no1:"))
b=int(input("Enter no2:"))

try:
    d=a/b
    print("div=",d)
except:
    print("can't divided by zero")
else:
    print(f"you can divide {a} by {b} and also")
finally:
    print("sum=",(a+b))
    print("sub=",(a-b))
    print("mul=",(a*b))