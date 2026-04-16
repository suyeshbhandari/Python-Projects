



with open("replace1.txt") as f:
    data = f.read()

    data = data.replace("donkey", "$%^@$^#")
    
    with open("replace1.txt", "w") as f:
     f.write(data)