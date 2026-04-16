s = set()
s.add(20)
s.add(20.0)
s.add("20")
print("The Length of the set is :"), print(len(s))


"the reason behind it is that the float 20.0 is equal to the twenty"
# if you remove the .0 or add some num in the float element it will be 3  