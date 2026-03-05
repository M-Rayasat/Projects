#Ask the user to enter pizza toppings until they type quit. Print a message for each topping added.
while True:
	top=input("Enter topping for pizza typed 'quite' for completion your order: ")
	if top.lower()=="quite":
		print("Your Pizza has completed")
		break
	else:
		print("Your toping {top} has added")