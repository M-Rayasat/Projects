# Name Formatter

# Step 1: Input full name (with possible extra spaces / wrong caps)
full_name = input("Enter your full name: ")

# Step 2: Remove extra spaces and split into words
words = full_name.strip().split()

# Step 3: Capitalize each part of the name properly
formatted_words = []
for w in words:
    formatted_words.append(w.capitalize())

# Step 4: Join back with a single space
formatted_name = " ".join(formatted_words)

#Step 5: Output
print(f"Formatted Name: {formatted_name}")