#Create a program that simulates restaurant seating:

people = int(input("How many people are in your group? "))

if people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")