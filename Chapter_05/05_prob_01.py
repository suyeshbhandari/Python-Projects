
myDict = {
    "Dhoka" : "Door",
    "Chiya" : "Tea",
    "kal"   : "Tap",
    "Bahini": "Sister",
    "Aama"  : "Mother"
}
print("Options are ", myDict.keys())
a = input("Enter the Nepali Word\n")
# print("The meaning of your word is:", myDict[a]) --> this throws an error

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))


mydict = {
    "Door"   : "Dhoka",
    "Tea"    : "Chiya", 
    "Tap"    : "kal",
    "Sister" : "Bahini",
    "Mother" : "Aama" 
}
print("Options are ", myDict.keys())
a = input("Enter the English Word\n")


# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))