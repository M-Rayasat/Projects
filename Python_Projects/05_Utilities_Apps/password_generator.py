import random
import string   # 📌 String module me ready-made character sets milte hain

# 📝 Step 1: User se desired length lena
length = int(input("Enter desired password length (minimum 8): "))

# ⚠️ Step 2: Length check
if length < 8:
    print("❌ Password length must be at least 8 characters.")
else:
    # ✅ Step 3: Character sets banayein
    lowercase = string.ascii_lowercase   # abcdef...
    uppercase = string.ascii_uppercase   # ABCDEF...
    digits = string.digits               # 0123456789

    # ✅ Step 4: Sab sets ko combine karna
    all_chars = lowercase + uppercase + digits

    # ✅ Step 5: Random password generate karna
    password = ''.join(random.choice(all_chars) for _ in range(length))

    # ✅ Step 6: Print password
    print(f"🔐 Your generated password is: {password}")