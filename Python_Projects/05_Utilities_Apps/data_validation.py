#Data Validation
# Ask for user inputs
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")

print("\n--- Validation Results ---")

# Validate name (non-empty)
if name.strip() != "":
    print("Name is valid")
else:
    print("Name cannot be empty")

# Validate age (integer between 0 and 120)
if age.isdigit() and 0 <= int(age) <= 120:
    print("Age is valid")
else:
    print("Invalid age (must be a number between 0 and 120)")

# Validate email (must contain '@' and '.')
if "@" in email and "." in email:
    print("Email is valid")
else:
    print("Invalid email (must contain '@' and '.')")

# Validate phone number (10 digits only)
if phone.isdigit() and len(phone) == 10:
    print("Phone number is valid")
else:
    print("Invalid phone number (must contain 10 digits only)")