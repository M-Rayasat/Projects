sen=input("Sentence: ").lower()
vowels="aeiou"
vowel_l=0
con=0
space=0
digit=0
for x in sen:
	if x in vowels:
		vowel_l+=1
	elif x.isalpha():
		con+=1
	elif x.isdigit():
		digit+=1
	elif x.isspace():
		space+=1
print("Vowels: ",vowel_l)
print("Consonant: ",con)
print("Spaces: ",space)
print("Digits: ",digit)