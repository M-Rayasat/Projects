#palindrome Checker
tex=input("Enter the number: ")
if tex==tex[::-1]:
	print(f"This Is palindrome Text")
else:
	print("Text is not palindrome")