class Car:
    name:None
    model:None
    color:None

    def __init__(self,name,model,color) :
        self.name=name 
        self.model=model 
        self.color=color

    def drive(self):
        print(f"{self.name} is driving now")

    def start(self):
        print(f"{self.name} has started ")

    def stop(self):
        print(f"{self.name} is stopped")