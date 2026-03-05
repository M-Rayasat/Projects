#BMI Calculator with Categories

# Step 1: Input from user
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Step 2: Calculate BMI
bmi = weight / (height ** 2)

# Step 3: Determine BMI Category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

# Step 4: Display Result
print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")