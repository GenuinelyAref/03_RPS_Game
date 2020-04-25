# Statement generator (decorate text)

#  Number of extra unprinted characters in any statement (\033 formatting)
TEXT_LENGTH = 11

# Text decorator function definition
def decorate_text(statement, char):
    x_variable = int("{}".format(len(statement)-TEXT_LENGTH))
    print()
    print(char*x_variable)
    print(statement)
    print(char*x_variable)

# Print decorated feedback/status messages
win_feedback = decorate_text("*** \033[44;42m  WIN  \033[m ***", "*")
lose_feedback = decorate_text("!!! \033[44;41m  LOSS  \033[m !!!", "!")
draw_feedback = decorate_text("=== \033[44;43m  DRAW  \033[m ===", "=")
farewell_message = decorate_text("### \033[44;46m  Thank you for playing RPS!  \033[m ###", "#")
