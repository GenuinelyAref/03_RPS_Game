# Get user input for number of games(rounds) to play

# To do
# Get input
# Check that input is an integer, between 1 and 100


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


# Main routine
game_input = intcheck("How many games do you wish to play? (Max 100 games) ", 1, 100)
print("\x1B[3mNumber of games chosen: {}\x1B[23m".format(game_input))
