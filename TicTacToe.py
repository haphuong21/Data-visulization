
# display board
# play game
# check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player

# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# game is still going
game_still_going = True

# who won ? or tie ?
winner = None

# who turn is it
current_player = "X"

#display board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

#play tic tac toe
def play_game():
    # display intial board
    display_board()
    while game_still_going:
        #handle a single turn of an arbitrary player
        handle_turn(current_player)
        #check if the game has ended
        check_if_game_over()
        #flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

#handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position)-1

        if board[position] == "-":
            valid = True
        else:
            print("Warning. Go again !")
    board[position] = player
    display_board()

def check_if_game_over():
    check_if_winner()
    check_if_tie()

def check_if_winner():
    #set global winner
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagnoals
    diaginal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diaginal_winner:
        winner = diaginal_winner
    else:
        winner = None


def check_rows():
    # set up global variables
    global game_still_going
    # check if any of the rows have all the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():
    # set up global variables
    global game_still_going
    # check if any of the columns have all the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[6] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None

def check_diagonals():
    # set up global variables
    global game_still_going
    # check if any of the diagnoal have all the same value
    diagnoal_1 = board[0] == board[4] == board[8] != "-"
    diagnoal_2 = board[2] == board[4] == board[6] != "-"
    if diagnoal_1 or diagnoal_2:
        game_still_going = False
    if diagnoal_1:
        return board[0]
    elif diagnoal_2:
        return board[2]
    else:
        return None

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    #global variables we need
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()
