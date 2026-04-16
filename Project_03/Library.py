class Library:
    def __init__(self, listOfmangas):
        self.mangas = listOfmangas

    def displayAvailablemanga(self):
        print("Mangas present in this library are: ")
        for manga in self.mangas: 
            print(" *" + manga)
    
    def borrowmanga(self, mangaName):
        if mangaName in self.mangas:
            print(f"You have been issued {mangaName}. Please keep it safe and return it within 30 days")
            self.mangas.remove(mangaName)
            return True
        else:
            print("Sorry! the manga is not available at the moment. please tryagain later ")
            return False

    def returnmanga(self, mangaName):
        self.mangas.append(mangaName)
        print("Thanks for using our service. have a great day!! ")

class Student: 
    def requestmanga(self):
        self.manga = input("Enter the name of the manga you want to borrow: ")
        return self.manga

    def returnmanga(self):
        self.manga = input("Enter the name of the manga you want to return: ")
        return self.manga
         

if __name__ == "__main__":
    sevenmangacafe = Library(["Boruto", "One piece", "Jujutsu Kaisen", "Jojo's Bizzare Adventure"])
    student = Student()
    sevenmangacafe.displayAvailablemanga()
    while(True):
        welcomeMsg = '''\n Welcome to Seven mangacafe ======
        Please choose an option:
        1. List all the available manga
        2. Request a manga
        3. Add/Return a manga
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            sevenmangacafe.displayAvailablemanga()
        elif a == 2:
            sevenmangacafe.borrowmanga(student.requestmanga())
        elif a == 3:
            sevenmangacafe.returnmanga(student.returnmanga())
        elif a == 4:
            print("Thanks for choosing Seven mangacafe. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

        

