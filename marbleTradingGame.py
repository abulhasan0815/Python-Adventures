import random
#create a bag with 10 marbles
bag = ('green', 'green', 'green', 'green', 'green', 'black', 'red', 'red', 'red', 'white',)
#starting amount of money
startWallet = 1000
# current money amount
wallet = startWallet
#result of last round
result = 0
#how many rounds
#last marble
marble = None
# welcome user to game
print(f"You start the game with {startWallet} gold pieces")
rounds = int(input("How many round would you like to play? "))
# loop drawing marbles
for draw in range(1, rounds+1):
    #how much was bet
    bet = int(input(f"Current Wallet: {wallet} Last draw: {marble} \nRound {draw}- How much do you wanna bet? "))
    #draw marble
    marble = random.choice(bag)
    # win or loss
    if marble == 'green':
        result = bet
    elif marble == 'black':
        result = 10 * bet
    elif marble == "white":
        result = -5 * bet
    else:
        result = -bet
    #calc win or loss/ result and new amount/purse
    wallet += result
    #lose game if lose half of money
    if wallet < 0.5 * startWallet:
        print(f'Game over! You lost to much gold!!!')
        break
#print results
print(f"Wallet: {wallet}, last result: {marble}: {result}\n")    
# print final results
print('starting / ending purse: ', startWallet, '/',wallet)
print('gain/loss: ', ((wallet-startWallet)/startWallet *100),'%')