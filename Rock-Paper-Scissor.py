import random

def get_choices():
    player_choice = input("Enter your choice ( rock,paper,scissor) : ")
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices
def check_win(player,computer):
    print(f"The player chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie. "
    elif player == "rock":
        if computer == "paper":
            return "Paper beats rock. You lose. "
        else : 
            return "Rock beats scissor. You win. "
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock. You win. "
        else:
            return "Scissor cuts paper. You lose. "
    elif player == "scissor":
        if computer == "rock":
            return "Rock beats scissor. You lose. "
        else: 
            return "Scissor cuts paper. You win. "
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
