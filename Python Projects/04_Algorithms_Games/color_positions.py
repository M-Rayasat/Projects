#Define a tuple of 5 colors. Loop through the tuple and print each color with its position.
color=('Red','Green','Yellow','White','Blue')
print(color)
L=range(len(color))
for x in L:
	print(f"Position {x+1}: {color[x]}")