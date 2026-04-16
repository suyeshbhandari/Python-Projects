class attribute:
    a = "Google"

obj = attribute()
obj.a = "Youtube" # --> it does not changes the class attribute instead it creates instance of the object
# attribute.a = "Youtube" --> it changes the class attribute

print(obj.a)