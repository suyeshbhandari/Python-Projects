class Calculator:
    Company = "Microsoft"

    def __init__(self, num):
        self.num = num
        
    def square(self):
            print(f"The square of the number is  {self.num **2} ")

    def cube(self):
            print(f"The cube of the number is  {self.num **0.5} ")    

    def squareroot(self):
            print(f"The square of the number is  {self.num **3} ")            
            

Number = Calculator(int(input("enter the number: ")))
Number.square()
Number.cube()
Number.squareroot()




       
