from animal import Animal
class fish(Animal):
    
    def swim(self):
        print(f"The {self.name} is swimming ")

    def lives(self):
        print(f"The {self.name} lives in water")






fish1=fish("katla")

fish1.eat()
fish1.sleep()
fish1.swim()
fish1.lives()


import animal


humamm=animal.Mamel("man")#this object is of mamel inherited form the animal so contains the properties of both animals and mamels 


humamm.baby()
