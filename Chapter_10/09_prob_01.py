
class Programmer:
    Company = "Microsoft"

    def __init__(self, name, address, product):
        self.name = name
        self.address = address  
        self.product = product

    def info(self):
            print(f"The name of the employee is {self.name} ")
            print(f"The address of the employee is {self.address}")
            print(f"The produt that employee working on is {self.product}")
            print("----------------------------------------------------------------------------------------------------------------------------------")

Suyesh = Programmer("Suyesh","Attariya","Windows")
Jagdish = Programmer("Jagdish","Attariya","Xbox")
Bikram = Programmer("Bikram","Attariya","Mojang")
Naresh = Programmer("Naresh","Attariya","Activision")
Suyesh.info()
Jagdish.info()
Bikram.info()
Naresh.info()


       
