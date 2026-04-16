class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

suyesh = Employee()
suyesh.salary = 100000
suyesh.getSalary("Thanks!") # Employee.getSalary(suyesh)
suyesh.greet() # Employee.greet()
suyesh.time()

