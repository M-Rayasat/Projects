#chracter frequency counter
text = input("Enter a word or sentence: ")

text = text.replace(" ", "").lower()

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char in sorted(freq.keys()) is:
    print(f"'{char}': {freq[char]}")