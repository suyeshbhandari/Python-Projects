a = 15 # --> global variable
def hello():
    global a
    print(a) #--> prints global variable 
    a =  8 #--> local variable
    print(a)# --> prints local variable


hello()
print(a) # --> prints global variable   