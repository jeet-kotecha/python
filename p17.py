# check student's class according to their percentage
per=float(input("Enter your percentage:"))

if per>=70 and per<=100:
    print("first class")
elif per>=50 and per<=69:
    print("seconde class") 
elif per>=40 and per<=49:
    print("pass class")
elif per<=39:
    print("fail")
else:
    print("please enter valid percentage")               