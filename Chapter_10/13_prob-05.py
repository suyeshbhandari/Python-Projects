class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self ,a):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
         if(self.seats>0):
          print(f"Your ticket has been booked! Your seat number is {self.seats}")
          self.seats = self.seats - 1
         else:
            print("Sorry this train is full! Kindly tryagain in later")
           

    def cancelticket(self):
        pass 

Chennai = Train("Chennai Express: 14015", 600, 300)
Chennai.getStatus() 
Chennai.bookTicket()
Chennai.cancelticket()
Chennai.getStatus()
