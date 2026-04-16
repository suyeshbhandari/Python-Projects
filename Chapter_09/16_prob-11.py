import os


file1 = "Prob_11.txt"
file2 = "removed_by_python.txt"

with open(file1) as  f:
    a = f.read()

with open(file2,'w') as f:
    b = f.write(a)    


os.remove(file1)




# it will not rename the file but it makes it look like renamed