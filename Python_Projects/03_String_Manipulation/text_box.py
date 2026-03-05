#Take a string and print it in a box format using *
text=input("Enter the text: ")
Width=len(text)+2
print("*"*Width)
print(f'*{text.title()}*')
print("*"*Width)