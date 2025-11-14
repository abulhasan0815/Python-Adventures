''' 1 for snake, -1 for water, 0 for gun'''

import random
computer = random.choice([-1, 0, 1])
you = input("Enter your Choice: ").capitalize().strip()

Dict = {"Snake": 1, "Water": -1,"Gun": 0}
reverseDict = {1: "Snake",-1: "Water",0: "Gun"}
youNum = Dict[you]


print(f"You chose {you} Computer chose {reverseDict[computer]}")

if computer == youNum:
    print("It's a Draw")
else:
    if computer == -1 and youNum == 1:
        print("You Win")
    elif computer == -1 and youNum == 0:
        print("You Lose")
    elif computer == 0 and youNum == 1:
        print("You Lose")
    elif computer == 0 and youNum == -1:
        print("You Win")
    elif computer == 1 and youNum == 0:
        print("You Win")
    elif computer == 1 and youNum == -1:
        print("You Lose")
    else:
        print("Something went wrong")
    
