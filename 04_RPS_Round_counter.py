# Round counter

# To do
# Add variables to count rounds
# Show Round # at the beginning of each game
# Give reminder when there's one round left

TOTAL_ROUNDS = 1
ROUND = 0
for item in range(0, TOTAL_ROUNDS):
    ROUND += 1
    print("\nRound {} of {}".format(ROUND, TOTAL_ROUNDS))
    if ROUND == TOTAL_ROUNDS and TOTAL_ROUNDS != 1:
        print("\033[44;46m This is the last round! \033[m")
    print("\n\x1B[3mGameplay to go here when components are joined together\x1B[23m\n")
