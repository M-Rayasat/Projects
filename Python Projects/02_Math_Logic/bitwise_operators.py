# Take two example numbers
a = 12   # binary: 1100
b = 5    # binary: 0101

print("a =", a, "->", bin(a))
print("b =", b, "->", bin(b))

# 1. Bitwise AND
and_result = a & b
print("\n1. AND (a & b):", and_result, "->", bin(and_result))

# 2. Bitwise OR
or_result = a | b
print("2. OR (a | b):", or_result, "->", bin(or_result))

# 3. Bitwise XOR
xor_result = a ^ b
print("3. XOR (a ^ b):", xor_result, "->", bin(xor_result))

# 4. Bitwise NOT
not_a = ~a
not_b = ~b
print("4. NOT (~a):", not_a, "->", bin(not_a))
print("   NOT (~b):", not_b, "->", bin(not_b))

# 5. Left Shift
left_shift = a << 2  # shift a left by 2 bits
print("5. Left Shift (a << 2):", left_shift, "->", bin(left_shift)) #a×2^n

# 6. Right Shift
right_shift = a >> 2  # shift a right by 2 bits
print("6. Right Shift (a >> 2):", right_shift, "->", bin(right_shift))  #a//2^2