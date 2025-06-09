import random


def gamestart():
    introplayer_input = input("Do you want to play? ").lower()
    if introplayer_input != ("yes"):
        quit()
    print("Welcome to Rock, paper, scissors by Y1NK4")

    
def computer_choice():
    choices = ["rock", "paper" , "scissors"]
    return random.choice (choices)


def player_choice():
    valid_choices = ["rock", "paper" , "scissors"]
    human_input = input("Rock,paper or scissors? ").lower()
    if human_input not in valid_choices:
        print("That isn't an option.")
    else:
        return human_input
        


def judgement(player_answer,computer_answer):
    global player_score, computer_score
    player_score = 0
    computer_score = 0

    if  computer_answer==player_answer:
        print("Tie!")
    elif computer_answer == "rock" and player_answer == 'scissors' or computer_answer == 'scissors' and player_answer == "paper" or computer_answer == "paper" and player_answer =='rock':
        print("Computer wins")
        computer_score += 1
    else:
        print("You win!")
        player_score += 1
    return player_score, computer_score

    
gamestart()
while True:
    player_answer = player_choice()
    computer_answer = computer_choice()
    judgement(player_answer,computer_answer)
    print(f"You chose {player_answer}")
    print(f"Computer chose {computer_answer}")
    print(f"Your score: {player_score}")
    print(f"Computer's score: {computer_score}")
    if player_score == 5 or computer_score == 5:
        print("Game over!!!")
        break
    
    
    
    
   


    

    



