# Score mechanics

# Build upon prior code
# Add variables to count for wins/losses/draws
# Scoring points:
# Win = 3 points
# Draw = 1 point
# Loss = 0 points
# Show score at the end of each round
# Show total number of wins/losses/draws at the end of the game

import random

draws = 0
wins = 0
losses = 0
item_chosen = ""
tokens = ["Rock", "Paper", "Scissors"]

keep_going = ""
while keep_going == "":
    # Generate random computer token
    computer_token = random.choice(tokens)

    # Let user choose token
    user_token = input("\nRock (r), paper (p) or scissors (s)? ")

    # If input does not equal (case of lettering does not matter) any of the list items or their first letters ask again
    #   and clarify that spelling matters.
    while user_token.lower() != "rock" and user_token.lower() != "paper" and user_token.lower() != "scissors" and \
            user_token.lower() != "r" and user_token.lower() != "p" and user_token.lower() != "s":
        user_token = input("\033[44;41m Sorry, that was an invalid answer \033[m\n\n"
                           "Please choose rock, paper or scissors. Spelling matters! Token: ")
    if user_token[0].lower() == "r":
        item_chosen = "Rock"
    elif user_token[0].lower() == "p":
        item_chosen = "Paper"
    else:
        item_chosen = "Scissors"

    # Give feedback to user
    print("----------------------------------------------")
    print("\x1B[3mYou have chosen: {}\x1B[23m".format(item_chosen))
    print("The computer chose: {}\n".format(computer_token))

    # Draw
    if computer_token == item_chosen:
        round_result = "Draw"
        draws += 1
    # Wins/losses
    elif item_chosen == "Rock":
        if computer_token == "Paper":
            round_result = "Loss"
            losses += 1
        else:
            round_result = "Win"
            wins += 1
    elif item_chosen == "Paper":
        if computer_token == "Scissors":
            round_result = "Loss"
            losses += 1
        else:
            round_result = "Win"
            wins += 1
    else:
        if computer_token == "Rock":
            round_result = "Loss"
            losses += 1
        else:
            round_result = "Win"
            wins += 1

    score = wins*3 + draws*1

    # Results with corresponding coloured highlighting
    if round_result == "Win":
        print("\033[44;42m The result of this round is a {} \033[m".format(round_result))
    elif round_result == "Loss":
        print("\033[44;41m The result of this round is a {} \033[m".format(round_result))
    else:
        print("\033[44;43m The result of this round is a {} \033[m".format(round_result))
    print("\nYour score is:\033[44;47m {} \033[m".format(score))
    keep_going = input("Keep going? ")

print("\nLosses: {} | Wins: {} | Draws: {}".format(losses, wins, draws))
print("Final score: {}".format(score))
print("\n\033[44;45m Thank you for playing RPS Game! \033[m")
