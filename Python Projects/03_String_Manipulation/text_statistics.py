# Text Statistics Analyzer
text = input("Enter your text:\n")

# 1. Total Characters
total_chars = len(text)

# 2. Total Words
words = text.lower().split()
total_words = len(words)

# 3. Total Sentences
total_sentences = text.count(".") + text.count("?") + text.count("!")

# 4. Character Frequency
char_freq = {} #e.g "R" : 2
for ch in text:
    if ch != " ":
        char_freq[ch] = char_freq.get(ch, 0) + 1

most_freq_char = max(char_freq, key=char_freq.get)

# 5. Word Frequency
word_freq = {}
for w in words:
    word_freq[w] = word_freq.get(w, 0) + 1

most_freq_word = max(word_freq, key=word_freq.get) if word_freq else None

# 6. Average Word Length
total_word_length = sum(len(w) for w in words)
avg_word_length = total_word_length / total_words if total_words > 0 else 0

# 7. Output
print("\n--- Text Statistics ---")
print("Total characters:", total_chars)
print("Total words:", total_words)
print("Total sentences:", total_sentences)
print("Most frequent character:", most_freq_char)
print("Most frequent word:", most_freq_word)
print("Average word length:", avg_word_length)