#Reverse the Sentance
a=input("Enter the sentence: ")
list1=a.split()
list2=[]
for x in list1:
	list2.append(x[::-1])
rev=" ".join(list2)
print(rev)