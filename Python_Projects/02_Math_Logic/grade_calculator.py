#Grade Calculator
scr=[85, 92, 78, 96, 88]
wgh= [0.2, 0.2, 0.2, 0.2, 0.2]
sumw=0
for x,y in zip(scr,wgh):
	sumw+=x*y
if sumw>=90:
	gra="A"
elif sumw>=80:
	gra="B"		
elif sumw>=70:
	gra="C"		
elif sumw>=60:
	gra="D"		
else:
	gra="F"
print(f"Your Score is {scr}\nYour Weight is {wgh}\n Weighted Average: {sumw:.2f}\nYour Grade: {gra}")