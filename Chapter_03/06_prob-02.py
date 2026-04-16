letter = '''Dear, <|NAME|> 
 Greetings from A-ONE-Computer. We are happy to tell you that   
    You are selected!


    <|DATE|>
'''
name = input("Enter your Name\n")
date = input("Enter Date\n")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)