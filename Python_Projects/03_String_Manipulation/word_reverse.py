#Reverse Each Word in a Sentence
sen=input("Enter the sentence: ")
lis=sen.split()
rlis=[]
for x in lis:
	rlis.append(x[::-1])
nlis=" ".join(rlis)
print(f"Original:\n{sen}\n")
print(f"Reverse:\n{nlis}")