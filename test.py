

class Shop:
    def __init__(self,name,number):
        self.name=name
        self.number = number
    def myfn(self):
        print("Nmae - ",self.name, "Number -",self.number)

pp=Shop("Hamdan",22)
pp.myfn()