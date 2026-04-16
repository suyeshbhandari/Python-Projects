a = [1,2,6,7,8,8,9,5,7,4,4,7,5,8,1,7,1,0,10,15,1,77777,55,9,2,4,1,4]
b =[]
# for i in a:
#     if i%2 == 0:
#      b.append (i)
# print(b)     


#shortcut method

b = [ i for i in a if i%2==0]
print(b)


# for set

s = {i for i in a if i%2==0}
print (s)