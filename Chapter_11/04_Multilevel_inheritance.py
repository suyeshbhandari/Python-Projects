class Person:
    country = "Nepal"
    def salary(self):
        print("My salary is...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    # def salary(self):
    #     print("My salary is 2...")

class Programmer(Employee):
    company = "Fiverr"
    
    # def getSalary(self):
    #     print(f"No salary to programmers")
    
    def salry(self):
        print("My salary is 2++..")

p = Person()
p.salary()
# print(p.company) # throws an error

e = Employee()
e.salary()
print(e.company)

pr = Programmer()
pr.salary()
print(pr.company)
print(pr.country)
