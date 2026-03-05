#Demonstrate string methods
sen="This is a complete sentence"
print(sen)
word=sen.split()
print(word)
sen2="_".join(word)
print(sen2)
finding=sen.find("e") #return index if find, otherwise -1 on not founding
print(finding)
counting=sen.count("i")#count characters in data
print(counting)