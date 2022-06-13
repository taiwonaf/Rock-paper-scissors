import random

hands = ["R", "P", "S"]

user = str(input("Pick between 'R', 'P' or 'S': ").upper())
computer = random.choice(hands)

while user not in hands:
    print("You inputed an invalid option")
    user = str(input("Pick between 'R', 'P' or 'S': ").upper())
    print("Player (" + user +")" + ": CPU (" + computer +")")

while user == computer:
    print("Tie")
    user = str(input("Enter choice: ").upper())
    computer = random.choice(hands)

    while user not in hands:
        print("error")
        user = str(input("Enter choice: ").upper())
        print("Player (" + user +")" + ": CPU (" + computer +")")

print("Player (" + user +")" + ": CPU (" + computer +")")
if (user == "R" and computer =="S") or (user == "S" and computer == "P") or (user == "P" and computer == "R"):
    print("User won")
else:
    print("Computer won")