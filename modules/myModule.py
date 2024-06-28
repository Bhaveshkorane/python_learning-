def greating(name):
    print(f"Hello {name}")

class student:
    def __init__(self,name):
        self.name=name
        print(f"constructor is called and name is set to {self.name}")
    def setinfo(self,clas,div,roll):
        self.clas=clas
        self.div=div
        self.roll=roll
    
    def getinfo(self):
        print(f"The student name is {self.name} and he is in {self.div} and his roll no is {self.roll}")
