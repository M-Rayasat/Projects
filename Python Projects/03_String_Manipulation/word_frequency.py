#Word Frequency Counter
import string as tr
Input= "The quick brown fox, jumps over the lazy dog"
#Remove Punctuation
clean=''.join(x for x in Input if x not in tr.punctuation).lower()
dic={}
for x in clean:
	dic[x]=dic.get(x,0)+1
print("Original Sentance: ",Input)
print("Frequency: ",dic)
