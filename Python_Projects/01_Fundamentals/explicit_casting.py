#Create a program that demonstrates explicit type casting
fl_num=637.822
int_num=int(fl_num)
print(f"Result: {int_num} & {type(int_num)}") #Truncation: Removed Decimal without Round-off
my_str="1234"
int_num=int(my_str)
print(f"Result: {int_num} & {type(int_num)}") #Change Type String to Integer
my_str="2627.8282"
fl_num=float(my_str)
print(f"Result: {fl_num} & {type(fl_num)}") #Change Type String to Float
my_int=7337
my_str=str(my_int)
print(f"Result: {my_str} & {type(my_str)}") #Change Type Integer to String
comp_num=78+18j
my_bool=comp_num.real #Imaginary is not convertable to int (Real don't need brackets ⚠️)
int_num=int(my_bool)
print(f"Result: {int_num} & {type(int_num)}") #Change Type Boolean to Integer