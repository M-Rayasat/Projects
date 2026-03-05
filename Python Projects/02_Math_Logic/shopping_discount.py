# Shopping Discount Calculator

#  Input
original_price = float(input("Enter Original Price: "))
discount_percent = float(input("Enter Discount Percentage: "))

#  Step 1: Calculate discount amount
discount_amount = (original_price * discount_percent) / 100

#  Step 2: Calculate final price after first discount
final_price = original_price - discount_amount

#  Step 3: Apply extra 5% discount if final price > 1000
extra_discount = 0
if final_price > 1000:
    extra_discount = (final_price * 5) / 100
    final_price -= extra_discount

#  Step 4: Total amount saved
total_saved = discount_amount + extra_discount

#  Step 5: Output
print("\n --- BILL SUMMARY ---")
print(f"Original Price: Rs {original_price}")
print(f"Discount Amount: Rs {discount_amount}")
if extra_discount > 0:
    print(f"Extra 5% Discount: Rs {extra_discount}")
print(f"Final Price to Pay: Rs {final_price}")
print(f"Total Amount Saved: Rs {total_saved}")