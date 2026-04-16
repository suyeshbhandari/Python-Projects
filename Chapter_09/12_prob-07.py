

a = True
i = 1
with open("log.txt") as f:   
    while a:
       a = f.readline()
       if "Python"  in a:
          print(a)
          print(f"python is present in line no {i}")
       i+=1
