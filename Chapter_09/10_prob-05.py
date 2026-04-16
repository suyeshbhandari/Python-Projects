


Words = ["Donkey","donkey","DONKEY"]
with open("replace2.txt") as f:
    data = f.read()
for word in Words:
    data = data.replace(word, "$%^@$^#")
    with open("replace2.txt", "w") as f:
     f.write(data)