#Matrix Operation
A= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B= [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result=[]
for x in range(len(A)):
	row=[]
	for y in range(len(A[x])):
		row.append(A[x][y]+B[x][y])
	result.append(row)
#print(result)
print("Matrix A:")
for x in A:
	print(x)
print("\nMatrix B:")
for x in B:
	print(x)
print("\nMatrix A+B:")
for x in result:
	print(x)