class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

suyesh = Employee()
suyesh.salary = 100000
suyesh.getSalary() # Employee.getSalary(suyesh)