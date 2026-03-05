#Text Analyzer

text = "Hello World! This is a sample text for analysis."

# Total characters (including spaces)
total_chars = len(text)

# Total words
words = text.split()
total_words = len(words)

# Total sentences (. ! ? se end hone wale)
sentences = text.count('.') + text.count('!') + text.count('?')

# Count vowels and consonants
vowels = "aeiouAEIOU"
vowel_count = sum(1 for ch in text if ch in vowels)
consonant_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)

# Print all statistics
print("Original Text:", text)
print("Total Characters:", total_chars)
print("Total Words:", total_words)
print("Total Sentences:", sentences)
print("Total Vowels:", vowel_count)
print("Total Consonants:", consonant_count)