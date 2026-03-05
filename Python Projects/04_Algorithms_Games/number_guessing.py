#Number Guessing Game
import random as Rd
scr=Rd.randint(1,1000)
atp=0
while True:
	ch=int(input("Guess the Number: "))
	if ch>scr:
		r="Too High"
		atp+=1
	elif ch<scr:
		r="Too Low"
		atp+=1
	else:
		r=f"Congratulations you have won {scr} after {atp} Attempts"
	print(r)

	