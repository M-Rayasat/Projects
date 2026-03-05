# Caesar Cipher - Simple Version

text = input("Enter a lowercase word: ")
shift = int(input("Enter shift number: "))

result = ""

for ch in text:
    if ch >= 'a' and ch <= 'z':
        # alphabet mein position nikalna
        pos = ord(ch) - ord('a')
        # shift karna
        new_pos = (pos + shift) % 26
        # wapas letter banana
        result += chr(ord('a') + new_pos)
    else:
        result += ch   # agar letter nahi to waise ka waise

print("Encrypted Text:", result)