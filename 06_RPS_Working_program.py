# RPS Game

# To do
# Combine all components correctly
# Implement text_decorator function more often
# Add option to restart game
# Add thorough comments in the code

# Import library(ies)
import random

item_chosen = ""

# List of possible game tokens
tokens = ["Rock", "Paper", "Scissors"]


# Integer checking function below
def intcheck(question, low, high):
    valid = False
    error = "\033[44;41m Please enter an integer between {} and {} \033[m".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)
            print()


# Statement generator function (to decorate text)
#  Number of extra unprinted characters in any statement (\033 formatting)
TEXT_LENGTH = 11


# Text decorator function definition
def decorate_text(statement, char):
    x_variable = int("{}".format(len(statement)-TEXT_LENGTH))
    print()
    print(char*x_variable)
    print(statement)
    print(char*x_variable)


# Option to restart game after finishing all rounds
keep_going = ""
while keep_going == "":

    # Define all used variables where possible
    score = 0
    draws = 0
    wins = 0
    losses = 0

    ROUND = 0
    # Input for rounds
    total_rounds = intcheck("\nHow many games do you want to play? (Max 100) ", 1, 100)
    print("\x1B[3mNumber of games chosen: {}\x1B[23m\n".format(total_rounds))

    # Repeat game for however many rounds the user chose (max. 100)
    for item in range(0, total_rounds):

        # Increase current round value by one
        ROUND += 1
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

        # Declare round number and remind user on their last round that this is the last round
        print("\n\033[1mRound {} of {}\033[0m".format(ROUND, total_rounds))
        if ROUND == total_rounds and total_rounds != 1:
            print("\033[44;45m This is the last round! \033[m")

        # Generate random computer token
        computer_token = random.choice(tokens)

        # Let user choose token
        user_token = input("\nRock (r), paper (p) or scissors (s)? ")

        # If input does not equal (case of lettering does not matter) any of the list items or
        #   their first letters ask again and clarify that spelling matters.
        while user_token.lower() != "rock" and user_token.lower() != "paper" and user_token.lower() != "scissors" and \
                user_token.lower() != "r" and user_token.lower() != "p" and user_token.lower() != "s":
            user_token = input("\033[44;41m Sorry, that was an invalid answer \033[m\n\n"
                               "Please choose rock, paper or scissors. Spelling matters! Token: ")

        # Sets back-end item names - different than user input (ie. "RoCk" and "ROcK" and "r" all turn into ==> Rock)
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
        # Wins/losses for Rock
        elif item_chosen == "Rock":
            if computer_token == "Paper":
                round_result = "Loss"
                losses += 1
            else:
                round_result = "Win"
                wins += 1
        # Wins/losses for Paper
        elif item_chosen == "Paper":
            if computer_token == "Scissors":
                round_result = "Loss"
                losses += 1
            else:
                round_result = "Win"
                wins += 1
        # Wins/losses for Scissors
        else:
            if computer_token == "Rock":
                round_result = "Loss"
                losses += 1
            else:
                round_result = "Win"
                wins += 1

        # Formula for finding score. Win = 3 points, Draw = 1 point & Loss = 0 points
        score = wins*3 + draws*1

        # Results with corresponding coloured highlighting
        # Win feedback message
        if round_result == "Win":
            win_message = decorate_text("*** \033[44;42m The result of this round is"
                                        " a {} \033[m ***".format(round_result), "*")
        # Loss feedback message
        elif round_result == "Loss":
            win_message = decorate_text("!!! \033[44;41m The result of this round is"
                                        " a {} \033[m !!!".format(round_result), "!")
        # Draw feedback message
        else:
            win_message = decorate_text("=== \033[44;43m The result of this round is"
                                        " a {} \033[m ===".format(round_result), "=")
        print("\nYour score is:\033[44;47m {} \033[m".format(score))

    print("____________________________________________________")

    # Manual text decoration - as function would not read some of the text's
    #   contents and therefore malfunction. Inconvenient in terms of storage
    #   space/efficiency of code, but only this exception has been made throughout the code
    # End of game Statistics
    print("\nGame Statistics:\n")
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
          "^^^ Losses: {} | Wins: {} | Draws: {} ^^^\n"
          "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n".format(losses, wins, draws))

    # Average Ghost score is the # of points that the user would receive having had an equal # of wins/losses/draws
    print("\033[1;31;40m Average Ghost score: {} \033[m".format(total_rounds * 1))

    # Final score = score from last round
    print("\033[1mFinal score: {}\033[0m".format(score))

    # Loop game (ie. restart from round choosing but skip introduction)
    keep_going = input("\n\x1B[3mPush <enter> to play again or any key to quit. \x1B[23m")

# Farewell message
Farewell_message = decorate_text("### \033[44;46m Thank you for playing RPS Game! \033[m ###", "#")
