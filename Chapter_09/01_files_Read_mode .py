 # this is for changing directory



# READ MODE
# To read the contents of the file

f = open('file_for_read.txt','r') # --> the r is default if you want us another mode you have to specify

data =f.read(2) # --> you can spicify the number of characters it reads by writing the number in between brackets
print(data)
f.close()

# Other methods to read the contents of the file

f = open('file_for_read.txt','r')
data = f.readline() # --> it reads the first line of the file
print(data)
data = f.readline() # --> it reads the second line of the file
print(data)
f.close()






























































































# STRUGGLE

# # import os
# # # # # os.chdir(C:\Users\97798\Desktop\python\Chapter_09)

# import os

# # directory = os.getcwd()
# # print("The current working directory of the file is : ", directory)
# os.chdir('C:/Users/97798/Desktop/Course/Chapter_09')
# print("The current working directory of the file is : ", directory)

# mydir = "C:/Users/97798/Desktop/python/Chapter_09"
# myfile = 'buddy.txt'

# training_images_labels_path = "C:/Users/97798/Desktop/python/Chapter_09/buddy.txt"
# open(training_images_labels_path,'r') as a file
# print(read())
# close()

# fName = 'buddy.txt'
# try:
#     with open(fName, 'w+') as f:     
#      except OSError:
# print ("Could not create/open file:", fName)

