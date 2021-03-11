def tic_tac_toe(player_1, player_2):
    """
    Main game
    """
    board = {1: ' ', 2:  ' ', 3: ' ',
             4: ' ', 5:  ' ', 6: ' ',
             7: ' ', 8:  ' ', 9: ' '}
    printboard(board)
    turn = ''
    for i in range(1, 10, 2):
        board[int(validation(board, player_1))] = 'X'
        turn = player1
        printboard(board)
        if winner(board, turn):
            return f'{player_1} WINS!!!'
        #if i == 9:
         #   break
        board[int(validation(board, player_2))] = 'O'
        turn = player2
        printboard(board)
        if winner(board, turn):
            return f'{player_2} WINS!!!'
    print("DRAW!")


def winner(board, turn):
    """
    Defining the winner
    """
    if (board[1] == board[2] == board[3] != ' ') \
     or (board[4] == board[5] == board[6] != ' ') \
     or (board[7] == board[8] == board[9] != ' ') \
     or (board[1] == board[4] == board[7] != ' ') \
     or (board[2] == board[5] == board[9] != ' ') \
     or (board[3] == board[6] == board[9] != ' ') \
     or (board[1] == board[5] == board[9] != ' ') \
     or (board[7] == board[5] == board[3] != ' '):
        print(f"{turn} WINS!!!")
        return True
    return False


def printboard(board):
    """
    Showing Game board
    """
    print(f"  {board[1]}  |  {board[2]}  | {board[3]}\n" 
          "_____|_____|_____\n"
          f"  {board[4]}  |  {board[5]}  | {board[6]}\n"
          "_____|_____|_____\n"
          f"  {board[7]}  |  {board[8]}  | {board[9]}\n")


def validation(board, player):
    while True:
        player_choice = input(f'{player}\'s turn')
        if player_choice.isdecimal() and int(player_choice) in range(1, 10)\
                and board[int(player_choice)] == ' ':
            return player_choice
        print("Invalid action!")




player1 = input("Input Player 1 Name: ")
player2 = input("Input Player 2 Name: ")
tic_tac_toe(player1, player2)