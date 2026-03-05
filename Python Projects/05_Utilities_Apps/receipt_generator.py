# Step 1: Define items with prices
items = [("Apple", 1.50), ("Banana", 0.75), ("Orange", 2.00)]

# Step 2: Define quantities of each item
quantities = [3, 5, 2]

# Step 3: Calculate subtotal for each item
subtotals = []
for i in range(len(items)):
    item_name = items[i][0]           # item ka naam
    item_price = items[i][1]          # item ki price
    qty = quantities[i]               # quantity
    subtotal = item_price * qty       # ek item ka total
    subtotals.append(subtotal)        # list me add karna
    print(f"{item_name}: {qty} x ${item_price:.2f} = ${subtotal:.2f}")

# Step 4: Calculate total before tax
total_before_tax = sum(subtotals)

# Step 5: Apply 10% tax
tax = total_before_tax * 0.10

# Step 6: Calculate final total
final_total = total_before_tax + tax

# Step 7: Print receipt
print("\n--- RECEIPT ---")
for i in range(len(items)):
    print(f"{items[i][0]}: ${subtotals[i]:.2f}")
print(f"Subtotal: ${total_before_tax:.2f}")
print(f"Tax (10%): ${tax:.2f}")
print(f"Final Total: ${final_total:.2f}")