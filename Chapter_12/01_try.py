while (True):
    try:
       a = int(input("Enter the number: "))
       if a > 6:
        print ("your num is greater than 6")
    except Exception as e:
        print("Enter a number not a character")