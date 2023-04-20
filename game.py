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

#compare hands to determine who wins
if player == computer:
    print("It is a Tie!")
elif player == "Rock":
    if computer == "Paper":
        print("You lose!")
    else:
        print("You win!")
elif player == "Paper":
    if computer == "Scissors":
        print("You lose")
    else:
        print("You win!")
elif player == "Scissors":
    if computer == "Rock":
        print("You lose")
    else:
        print("You win!")
else:
    print("I dont beleive that is a valid hand!")