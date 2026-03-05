# Palindrome Number Checker

# Step 1: Take input from user
num = input("Enter a number: ")

#  Step 2: Reverse the string using slicing
rev_num = num[::-1]

#  Step 3: Compare original and reversed
if num == rev_num:
    print(f"{num} is a Palindrome ")
else:
    print(f"{num} is NOT a Palindrome ")