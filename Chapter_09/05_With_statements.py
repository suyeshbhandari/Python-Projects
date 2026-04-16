

with open('file_for_with_statement.txt','r') as f:
    data = f.read()
print(data) 
# with statement automatically closes the file   

with open('file_for_with_statement.txt','w') as f:
    Lazy = f.write(" With statements")
print(Lazy)    