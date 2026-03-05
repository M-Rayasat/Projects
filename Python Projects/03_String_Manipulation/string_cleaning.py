#Create a program that strips extra spaces from a string entered by the user and shows the cleaned result.
string= input("Enter your string to remove extra spaces: ")
print(f'After removing space from your string "{string}" is "{string.strip()}"')