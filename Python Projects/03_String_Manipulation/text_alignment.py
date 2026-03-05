#Write a program using the format() function to align text:
text="Muhammad Rayasat"
left="{:<20}".format(text) #left
right="{:>20}".format(text) #right
cen="{:^20}".format(text) #center
print(f"{left}\n{right}\n{cen}")