# User input for RPS

# To do
# Get user input for R/P/S
# Assign ".lowercase" extension to input
# Generate computer token (not used here but used in component "03b")

import random

item_chosen = ""
tokens = ["rock", "paper", "scissors"]
computer_token = random.choice(tokens)

# Loop input for testing
keep_going = ""
while keep_going == "":
    # Let user choose token
    user_token = input("Rock (r), paper (p) or scissors (s)? ")

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

    print("You have chosen: {}\n".format(item_chosen))
