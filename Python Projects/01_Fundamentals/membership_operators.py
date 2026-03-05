#Write a program using membership operators (in, not in)
lis=list(range(1,16))
y=int(input("Enter the number :"))
if y in lis:
	print(f"Number {y} is in List: {lis}")
elif y not in lis:
	print(f"Number {y} is not in List: {lis}")
nam="Muhammad Rayasat"
if (w:="y") in nam:
	print(f"{w} in {nam}")
if (w:="z") not in nam:
	print(f"{w} is not in {nam}")
my_dic={"age":18, "nam":"Rayasat"}
print(f"Age is written in dictionary which is: {'age' in my_dic}")
print(f"Father Name is not written in dictionary which is: {'f_nam' not in my_dic}")