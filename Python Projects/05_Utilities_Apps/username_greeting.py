#Create a list of usernames. Print a special greeting if the username is admin, otherwise greet normally
List=["Rayasat","Ahmad","admin","Tayyab","Ali"]
for x in List:
	if x=='admin':
		print(f'Welcome  Sir! {x} You have full Access')
	else:
		print(f'{x} Welcome to our journey')
