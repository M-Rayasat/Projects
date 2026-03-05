#Create a program that hides part of an email address for privacy.
email=input("Enter the email: ")
username , domain =email.split('@')
mask_us=username[0:2]+"***"
new_em=mask_us+"@"+domain
print(new_em)