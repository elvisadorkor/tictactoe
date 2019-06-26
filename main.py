
#game variables
game_over = False

curr_player = "X"

game_winner = None

game_board = ["-","-","-",
              "-","-","-",
              "-","-","-"]
def display_game_board():
    #prints out board
    print("|" + game_board[0] + "|" + game_board[1] + "|" + game_board[2] + "|")
    print("|" + game_board[3] + "|" + game_board[4] + "|" + game_board[5] + "|")
    print("|" + game_board[6] + "|" + game_board[7] + "|" + game_board[8] + "|")

def play_game():
    #display starting game board
    display_game_board()
    #while game is not over
    while game_over == False:
        player_turn(curr_player)
        check_game_over()
        change_player_turn()
    #check for winner
    if winner == "X":
        print("X won the game!")

    elif winner == "O":
        print("O won the game")

    elif winner == None:
        print("The game ended in a tie")
#player's move during their turn
def player_turn(player):
    print(player + "'s turn.")
    player_move = int(input("Choose a position from 1-9: "))
    #check if player makes correct move
    correct_move = False
    #while player has not made valid move
    while correct_move == False:
        #while player has not entered number in defined range on board
        while player_move not in [1,2,3,4,5,6,7,8,9]:
            #keep asking player to enter correct input
            player_move = int(input("Choose a position from 1-9: "))
        #make player move correspond with position on board. list indexing starts from 0
        position_on_board = player_move - 1
        #if position on board already
        if game_board[position_on_board] != "-":
            print('Position already taken on board. Please play again')
            player_move = int(input("Choose a position from 1-9: "))
        else:
            game_board[position_on_board] = player
            correct_move = True
    #display board after player's move
    display_game_board()

#check rows to see if player has won
def check_rows():
    global game_over
    first_row = game_board[0] == game_board[1] == game_board[2] != "-"
    second_row = game_board[3] == game_board[4] == game_board[5] != "-"
    third_row = game_board[6] == game_board[7] == game_board[8] != "-"
    if first_row:
        game_over = True
        return game_board[0]
    elif second_row:
        game_over = True
        return game_board[3]
    elif third_row:
        game_over = True
        return game_board[6]
    else:
        return None

#check columns to see if player has won
def check_columns():
    global game_over
    first_column = game_board[0] == game_board[3] == game_board[6] != "-"
    second_column = game_board[1] == game_board[4] == game_board[7] != "-"
    third_column = game_board[2] == game_board[5] == game_board[8] != "-"
    if first_column:
        game_over = True
        return game_board[0]
    elif second_column:
        game_over = True
        return game_board[1]
    elif third_column:
        game_over = True
        return game_board[2]
    else:
        return None

#check diagonals to see if player has won
def check_diagonals():
    global game_over
    first_diagonal = game_board[0] == game_board[4] == game_board[8] != "-"
    second_diagonal = game_board[2] == game_board[4] == game_board[6] != "-"
    if first_diagonal:
        game_over = True
        return game_board[0]
    elif second_diagonal:
        game_over = True
        return game_board[2]
    else:
        return None
#switch player turn
def change_player_turn():
    global curr_player
    if curr_player == "X":
        curr_player = "O"
    elif curr_player == "O":
        curr_player = "X"
    else:
        return None
#check if some player has won or game has ended in tie
def check_game_over():
    check_game_winner()
    tie_check()

#check for tie in game
def tie_check():
    global game_over
    if "-" not in game_board:
        game_over = True
        return True
    else:
        return False
#check rows, columns and diagonals to see if any player has won game
def check_game_winner():
    global winner
    winner_by_row = check_rows()
    winner_by_column = check_columns()
    winner_by_diagonal = check_diagonals()
    if winner_by_diagonal:
        winner = winner_by_diagonal
    elif winner_by_column:
        winner = winner_by_column
    elif winner_by_row:
        winner = winner_by_row
    else:
        winner = None

play_game()
