Post = input("Enter the Post to check harry is present or not\n")
Harry = False

if("harry" in Post):
    Harry = True
elif("Harry" in Post):
    Harry = True
elif("HArry" in Post):
    Harry = True
elif("HarrY" in Post):
    Harry = True
elif("HARRY" in Post):
    Harry = True
elif("haRRy" in Post):
    Harry = True
elif("HarRy" in Post):
    Harry = True
elif("HArRY" in Post):
    Harry = True
elif("HARRy" in Post):
    Harry = True                    
else:
     Harry= False  

if(Harry):
    print("Harry is present in the post")
else:
    print("Harry is not present in the post")













