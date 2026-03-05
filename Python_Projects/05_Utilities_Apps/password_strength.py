#Password Strength Checker
text=input("Enter the Password: ")

length=len(text)>=8
up=any(x.isupper() for x in text)
low=any(x.islower() for x in text)
dig=any(x.isdigit() for x in text )
special=any(x in "@#$_&-+()/*:;!?.':;?.,%={}" for x in text )

score=sum([length,up,low,dig, special])
if score==5:
	pwd="Strong"
elif score >=3:
	pwd="Medium"
else:
	pwd="weak"
print(f"Your Original Password is: {text}\nPassword Strength: {pwd}")