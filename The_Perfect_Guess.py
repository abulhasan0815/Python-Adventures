import random

num = random.randint(1, 100)
a = 0
guesses = 0
while (a != num):
    a = int(input("Guess the number between 1 and 100: "))
    if(a > num):
        print("Lower number please")
        guesses += 1
    elif(a < num):
        print("Higher number please")        
        guesses += 1
        
print(f"You have guessed the number corrctly in {guesses} attempt")

