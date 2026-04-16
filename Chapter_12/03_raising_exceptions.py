def increment(num):
    try:
       return int(num) +1 
    except :
         raise ValueError ("Enter a number not a character") 


increment(input("Enter the number: "))         