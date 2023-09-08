class Car:
    def __init__ (self,name,color, model):
        self.name=name
        self.color=color
        self.model=model
        self.e=Engine("four-stroke")
        self.c=Clutch("friction clutch")
    def printcardetails(self):
        print(f'car name is {self.name}')
        print(f'car color is {self.color}')
        print(f'car model{self.model}')
        self.e.printenginetype()
        self.c.printclutchdetails()



class Engine:
    def __init__ (self,enginetype):
        self.enginetype=enginetype
    def printenginetype(self):
        print(f'engine type is {self.enginetype}')



class Clutch:
     def __init__(self,clutchtype):
         self.clutchtype=clutchtype
     def printclutchdetails(self):
         print(f'clutch type is {self.clutchtype}')

c=Car('thar','black',' AXOPT ')
c.printcardetails()
