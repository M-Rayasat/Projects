#Fibonacci Sequence Generator
	 # Step 1: Take input from the user
n = int(input("Enter how many Fibonacci terms you want: "))

# Step 2: Initialize the first two numbers
a, b = 0, 1

# Step 3: Create an empty list to store sequence
fibonacci = []

# Step 4: Generate the sequence using a loop
for i in range(n):
    fibonacci.append(a)  # Add current term to list
    a, b = b, a + b      # Update values for next term

# Step 5: Print the results
print("\nNumber of terms:", n)
print("Fibonacci Sequence:", fibonacci)