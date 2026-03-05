#Email Validator
email=input("Enter your Email: ").strip()
valid=True
mistake=[]
if email.count('@')!=1: #No @ more then one
	valid=False
	mistake.append("Email Must have 1 '@'")
if "@" in email: #Check dot for after @
	at_index=email.index("@")
	if '.' not in (email[at_index:]):
		valid=False 
		mistake.append("Your Email must have '.' after @")
else:
	mistake.append("Email Must contiain @")
	valid=False
if email[0] in ["@",".","#"] or email[-1] in ["@",".","#"]:
	valid=False
	mistake.append("Email Must not start or end with special Characters")
if valid==True:
	print("Your Email is Valid")
else:
	print("Your Email is not Valid")
	for x in mistake:
		print(x)