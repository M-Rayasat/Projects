# Simple ATM Simulation Program
pin="1234"
balance=20000
atmp=0
while True:
	P=input("Enter your PIN: ")
	if pin==P:
		while True:
			print("1. Show balance\n2. Request for withdrawal\n3. Request for deposit\n4. Get Your Card")
			ch=int(input("\nEnter the choice: "))
			if ch==1:
				print(f'\nYour Balance is {balance}')
			if ch==2:
					w=int(input("\nEnter amount for Withdrawal: "))
					if w<=balance:
						balance-=w
						print(f"\nYou have successfully Withdraw {w} and Your new Balance is {balance}")
					else:
						print("\nInsufficient Balance ")
			if ch==3:
				d=int(input("\nEnter the Amount for Deposit: "))
				if d>=1:
					balance+=d
					print(f"\nYou have successfully Deposited {d}")
				else:
					print("\nEnter the Correct Amount")
			if ch==4:
				print("\nThanks For using ATM")
				break
			else:
				print("\nEnter the correct Choice")
	else:
		print("\nYou have entered incorrect PIN")
	atmp+=1
	if atmp>=3:
		break
print("Your Card Has been Locked ")
