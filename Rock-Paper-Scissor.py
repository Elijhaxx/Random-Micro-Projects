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


# Algorithm : 
# 1. A function called - get_choices
# 2. variable called - player_choice that takes input from the user
# 3. list variable called - options with options of the computer
# 4. variable called computer choices - that prints random from variable options
# 5. dictionary called choices - key value pair of player w player choice and computer with computer choice
# 6. return choices
# 7. function called - check_win that passes player and computer
# 8. print with string concatination - player chose player computer chose ( f string)
# 9. if statement - player = computer return tie 
# 10. elif and if statements for the reamining cases
# 11. variable choices - get_choices 
# 12. result - checkwin function that passes choices of player and variable.