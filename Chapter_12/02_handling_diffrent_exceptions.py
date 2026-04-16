while(True):
    try:
       a = int(input("Enter the number: "))
       b =   1/a 
       print(b)
    except ValueError as e:
        print("Enter a number not a character")
    except ZeroDivisionError as e:
        print("number cannot be zero")

                
        