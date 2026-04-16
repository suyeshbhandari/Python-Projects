



file1 = "Naruto.txt"
file2 = "Jujutsu Kaisen.txt"

with open(file1) as f:
    a = f.read()

with open(file2) as f:
    b = f.read()

if a in b:
    print("it matches the content of the other file")
else:
    print("it doenot matches the content of the other files")            





























































