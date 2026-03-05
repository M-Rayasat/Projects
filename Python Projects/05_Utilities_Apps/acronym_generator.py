#Acronym Generator
sen=input("Enter Sentence: ")
up_sen=sen.upper().strip()
split=up_sen.split()
y=''
for x in split:
	y=y+x[0]
print(f"Acronym is ({y})")