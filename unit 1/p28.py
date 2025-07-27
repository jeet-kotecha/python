# types of udf in python (with argument and with return type)
def simple(p,r,n):
    si=(p*r*n)/100
    return(si)
p=float(input("Enter Principal amount:"))
r=float(input("Enter Rate of interest:"))
n=float(input("Enter Time of years:"))
interest=simple(p,r,n)
print("simple interest is:",interest)