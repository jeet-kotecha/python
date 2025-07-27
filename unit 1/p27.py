# types of udf in python (with argument and no return type)
def details(name,age):
    print("Hi",name,"you are",age,"years old")
    
name =input("Enter your name:")
age =int(input("Enter your age:"))

details(name,age)