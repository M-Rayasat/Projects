#Vowel Counter
tex=input("Enter the text: ").lower()
vow={}
v="aeiou"
for x in tex:
	if x in v:
		vow[x]=vow.get(x,0)+1
print(f"Original Text:\n{tex}")
print("Vowels are:")
for x,y in vow.items():
	print(f"{x}:\t{y}")