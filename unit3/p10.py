# single inheritence with parameterized constructor(fname,lname)
class person:
    def __init__(self,fname,lname):
        self.fn=fname
        self.ln=lname
    def display(self):
        print(self.fn,self.ln)
class stud(person):
    def __init__(self,fname,lname):
        super(). __init__(fname,lname)

s1=stud("sachin","Tendulker")
s1.display()