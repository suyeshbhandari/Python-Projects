Text = input("Enter the Text\n")
Spam = False

if("make a lot of money" in Text):
    Spam = True
elif("buy now" in Text):
    Spam = True
elif("subscribe this" in Text):
    Spam = True
elif("click this" in Text):
    Spam = True
else:
    Spam = False  

if(Spam):
    print("This is a spam text")
else:
    print("This is not a spam text")

