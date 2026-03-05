#Write a program that stores a messy sentence with random spaces and prints a cleaned version.
sen=input("Enter the sentence: ")
new_sen_list=sen.split()
new_sen_str=" ".join(new_sen_list)
print(new_sen_str)