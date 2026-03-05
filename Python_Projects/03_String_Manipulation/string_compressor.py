#String Compressor
text=input("Enter text: ").lower()
compress=""
count=1
for x in range(1,len(text)):
	if text[x]==text[x-1]:
		count+=1
	else:
		compress+=text[x-1]+str(count)
		count=1
if text:
	compress+=text[-1]+str(count)
if len(compress)<len(text):
	print(f"Your compressed string: {compress}")
else:
	print("Your string is already shortest")