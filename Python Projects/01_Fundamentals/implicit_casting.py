#Write a program that demonstrates implicit type casting
my_int=256
my_float=190.728
new_num=my_int+my_float #implicit Typecasting 
print(f"Result: {new_num} & Type: {type(new_num)}")
my_complex=198+27j
new_num=my_int+my_complex #implicit Typecasting
print(f"Result: {new_num} & Type: {type(new_num)}")