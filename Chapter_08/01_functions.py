def percent(marks):
   return (sum(marks)/1100 )*100 # --> Return is used to do the task that is given using the value of wherever the function is called 
    

marks1 = [58, 69, 78, 66, 76, 98, 81, 85, 75, 77, 68]
percentage1 = percent(marks1)

marks2 = [56, 58, 65, 94, 67, 75, 77, 75, 69, 81, 85]
percentage2 = percent(marks2)
print(percentage1, percentage2)