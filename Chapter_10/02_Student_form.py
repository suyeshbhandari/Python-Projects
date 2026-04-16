import pandas as a

a.DataFrame()


class StudentForm:
      formtype = "StudentForm"
      def dataform(self):
        print(f'Name is {self.name}')
        print(f'Address is {self.address}')
        print(f'Age is {self.age}')

suyeshApplication = StudentForm()      
suyeshApplication.name  = "Suyesh Bhandari"
suyeshApplication.address  = "Attariya,Kailali"
suyeshApplication.age  = "15"
suyeshApplication.dataform()


