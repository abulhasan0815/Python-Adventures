#import modules
from random import randrange as r
from time import time as t
# ask how many questions user wants
numQuestions = int(input("How many questions would you like to practice: "))
maxNum = int(input("Highest number you want in practice: "))
#set score start at zero
score = 0
answerList = []
#loop through number of questions
start = t()
for q in range(numQuestions):
# create two random numbers and calc answer
    num1, num2 = r(1, maxNum + 1), r(1, maxNum + 1)
    ans = num1 * num2
# show user the question
    userAns = int(input(f'{num1} * {num2} = '))
    answerList.append(f'{num1} * {num2} = {ans} YOU: {userAns}')
# capture answer and modify user score
    if userAns == ans:
        score += 1
    end = t()
# output final score 
print(f'Thank you for playing \nYou got {score} out of {numQuestions} \nYour percentage {round(score/numQuestions*100)}% You got it done in {round(end-start, 1)} seconds')
print("Review and feedback")
for a in answerList:
    print(a)
