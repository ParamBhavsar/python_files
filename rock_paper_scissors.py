import random

def get_choices(user_input):
    #user_input = input("Enter your choice (rock, paper, or scissors): ")
    options = ["rock", "paper", "scissors"]
    comp_choice = random.choice(options)
    return {"player": user_input, "computer": comp_choice}

def win_condition(player, computer):
    print(f"You chose {player} and the computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! Computer wins"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut the paper! You win!"
        else:
            return "Rock smashes scissors! Computer wins"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut the paper! Computer wins"

user_input = input("Enter your choice (rock, paper, or scissors): ")
the_choices = get_choices(user_input)
result = win_condition(the_choices["player"], the_choices["computer"])
print(result)
    
