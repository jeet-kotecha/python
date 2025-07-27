# use exception handling for zerdivisionerror and value error
a=int(input("Enter value1:"))
b=input("Enter value2:")

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