


with open("log.txt") as f:
     a = f.read()

if "python " or "Python" in a:
    print("python is present")
else:
    print("python is not present")    
