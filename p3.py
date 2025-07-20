# print value using global variable 
a=1
def increment():
    global a
    a+=1
print("A inside function:",a)
increment()
print("A outside function:",a)
