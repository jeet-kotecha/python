# use exception handling for zerdivisionerror and value error
a=input("Enter value1:")
b=input("Enter value2:")

try:
    a1=int(a)
    b1=int(b)
    d=a1/b1
    print("div=",d)
except ValueError:
    print("can't divided string to int")
except ZeroDivisionError:
    print("can't divided by zero")
else:
    print("code run successfully")
finally:
    print("execution completed")