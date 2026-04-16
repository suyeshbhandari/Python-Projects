
with open('prob_01_poem.txt','r') as f:
         data = f.read() 
if 'twinkle' or 'Twinkle' in data:
    print("yes Twinkle is present")
else:
    print("No Twinkle is not present")    
 