


#UPDATING MODE
# You can read and write the contents of the file using Updating mode

f = open('file_for_update.txt','r+') # to open in read in text mode
suyesh =f.read()
print(suyesh)
f.close()



f = open('file_for_update.txt','w+') # to open in read in text mode
suyesh =f.write("updating")
f.close()