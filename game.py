from random import randint


#create a list of playable hands
hands = ["Rock", "Paper", "Scissors"]

#Get Player hand
player = input(f'Please select what to play {hands} :')

#Get Computer hand
computer = hands[randint(0,2)]

#output Player and Computer hands
print("Player hand was:", player)
print("Computer hand was:", computer)
