#Write a program that converts between different data types:
'''
String to integer
Integer to string
String to float
Print the results and their types
'''
Str="29"
print(f'{Str} is {type(Str)}')
num=int(Str)
print(f'{num} is {type(num)}')
Str=str(num)
print(f'{Str} is {type(Str)}')
flt=float(Str)
print(f'{flt} is {type(flt)}')
