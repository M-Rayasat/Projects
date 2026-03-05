# Simple Interest vs Compound Interest Calculator

# Taking inputs
P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest (%): "))
T = float(input("Enter Time (in years): "))

# Calculating Simple Interest
simple_interest = (P * R * T) / 100

# Calculating Compound Interest
compound_interest = P * (1 + R / 100) ** T - P

# Calculating difference
difference = compound_interest - simple_interest

# Displaying the results
print(f"\nSimple Interest: {simple_interest:.2f}")
print(f"Compound Interest: {compound_interest:.2f}")
print(f"Difference: {difference:.2f}")