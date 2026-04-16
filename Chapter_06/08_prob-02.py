sub1 = int(input("Enter Marks of the First  subject "))
sub2 = int(input("Enter Marks of the Second subject "))
sub3 = int(input("Enter Marks of the Third  subject "))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are failed")
elif(sub1+sub2+sub3)/3 <40:
    print("you are failed")    
else:
    print("Congratulation! You are passed")

       
       