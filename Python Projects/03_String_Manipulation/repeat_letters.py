#Repeat Letters
sen=list(input("Enter the sentence: ")) 
dup=[]
for x in sen:
	dup.append(x*2)
sent="".join(dup)
print(sent)