#Example of multiple inheritance
class emp:
    def __init__(self,name):
        self.nm=name
class job:
    def __init__(self,sal):
        self.salary=sal

class empdata(emp,job):
    def __init__(self, name,sal):
        emp.__init__(self,name)
        emp.__init__(self,sal)
    def printdata(self):
        print(self.nm,self.salary)

ed=empdata("rakesh",60000)
ed.printdata()