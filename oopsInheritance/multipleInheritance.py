class GrandFather:
    def __init__(self):
        print("This is your grand father")

    def prop(self):
        print("you are getting your grand fathers property ")


class GrandMother:
    def __init__(self):
        print("this is your grand mother ")

    def prop(self):
        print("you are geetting your grandmothers properties")

class Father(GrandMother,GrandFather):
    def __init__(self):
        #this will call only the grand fathers constructor 
        #super().__init__()
        # super().__init__()


        #to make sure that both constructors to be called we should call it as 
        GrandMother.__init__(self)
        GrandFather.__init__(self)
        
        print("This is your father")

    # def prop(self):
    #     print("You are getting your fathers properties ")




me=Father()

me.prop()#which ever class we pass first in multiple inheritance first its methods will be called 