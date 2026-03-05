#Create a simple text-based menu system that allows users to
shop_list=[]
while True:
	print("\t Shopping List\n1. Add items in shopping List\n2. Remove Items from the List\n3. View the Current List\n4. Exit the program")
	ch=int(input("Choose the option: "))
	if ch==1:
		while True:
			item=input("Add Items to the List (Enter s for stop adding): ")
			if item!='S' and item!='s':
				shop_list.append(item.title())
				print(f"You have added '{item.title()}' in list successfuly")
			else:
				break
	elif ch==2:
		item=input("Enter the Item: ")
		a=item.title()
		if a in shop_list:
			shop_list.remove(a)
			print(f"Successfuly Removed this item '{a}' from the List")
		else:
			print("Item not found")
	elif ch==3:
		print("\n Your Current Shopping list: ")
		if shop_list:
			index=1
			for x in shop_list:
				print(f"{index}. {x}")
				index+=1
		else:
			print("Shop list is empty")
	elif ch==4:
		print("Stopped Successful")
		break
	else:
		print('Invalid Choice')