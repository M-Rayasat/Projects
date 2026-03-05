#Number Reverser 
num1 = input("Enter a number: ")
#  Reverse using slicing
rev_str = num1[::-1]
print(f"Original Number: {num1}")
print(f"Reversed (String Method): {rev_str}")
#Reverse using Mathematics
num=int(num1)
org=num
rev_num=0
while num>0:
	digit=num%10 #Get Last Digit
	rev_num=rev_num*10+digit #Change place of digit to higher one
	num=num//10#Removed last digit of original number
print(f"Original Number: {org}")
print(f"Reversed (Integer): {rev_num}")