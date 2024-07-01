class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating ")
    def sleep(self):
        print(f"{self.name} is sleeping")



class Mamel(Animal):
    def __init__(self,name):
        super().__init__(name)#this is used to call the parent constructor 
        print(f"These {self.name}are mammalas ")
    
    

    def baby(slef):
        print(f"{slef.name} gives birth to babies")

class Reptles(Animal):
    def __init__(self,name):
        super().__init__(name)#the parent constructor is called form this 
        print(f"the {self.name} is reptile")
    def baby(self):
        print(f"the {self.name} lays eggs")