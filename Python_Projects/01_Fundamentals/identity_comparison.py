# -------------------------------------
# Difference between "is" and "=="
# -------------------------------------

# Example 1: Numbers
a = 1000
b = 1000

print("a == b:", a == b)   # ✅ True → values equal hain
print("a is b:", a is b)   # ❌ False → memory me alag objects hain

# Example 2: Small numbers (Python optimization)
x = 10
y = 10

print("\nx == y:", x == y) # ✅ True → values equal
print("x is y:", x is y)   # ✅ True → Python small integers ko cache karta hai

# Example 3: Strings
s1 = "Rayasat"
s2 = "Rayasat"

print("\ns1 == s2:", s1 == s2) # ✅ True → values same
print("s1 is s2:", s1 is s2)   # ✅ True → Python same string literal ko reuse karta hai

# Example 4: New string object
s3 = str("Rayasat")
s4 = str("Rayasat")

print("\ns3 == s4:", s3 == s4) # ✅ True → values same
print("s3 is s4:", s3 is s4)   # ❌ False → alag memory objects banaye gaye

# -------------------------------------
# Explanation:
# "=="  → values compare karta hai (content same hai ya nahi)
# "is" → memory address (object identity) compare karta hai
#agr integer ki range -5 se 256 tak ho to same address ata ha
# -------------------------------------