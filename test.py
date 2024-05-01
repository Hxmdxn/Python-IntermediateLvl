class Hamdan:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfn(self):
        print("my name is",self.name,"and I'm ",self.age,"years old.")
        
p=Hamdan("Hamdan",25)
p.myfn()

class Ali(Hamdan):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def myfn(self):
        print("my name is", self.name, "and I'm ", self.age, "years old.")

p2 = Ali("Ali", 30)  # Corrected quotation marks around "Ali"

        