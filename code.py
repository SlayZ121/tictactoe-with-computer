import math


def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-----')


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def check_winner(board, player):

    for row in board:
        if all(cell == player for cell in row):
            return True

 
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

 
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 10 - depth
    elif check_winner(board, 'X'):
        return -10 + depth
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval


def find_best_move(board):
    best_move = None
    best_eval = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                eval = minimax(board, 0, False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def play_game():
    board = initialize_board()

    
    player_name = input("Enter your name: ")
    player_symbol = input("Choose your symbol (X or O): ").upper()
    if player_symbol != 'X' and player_symbol != 'O':
        print("Invalid symbol! Please choose either X or O.")
        return

    
    computer_symbol = 'O' if player_symbol == 'X' else 'X'

    current_player = 'X'

    while not is_board_full(board) and not check_winner(board, 'X') and not check_winner(board, 'O'):
        print_board(board)
        if current_player == player_symbol:
            print(f"{player_name}'s turn ({player_symbol})")
            row, col = map(int, input("Enter row and column (0-2): ").split())
            if board[row][col] == ' ':
                board[row][col] = player_symbol
                current_player = computer_symbol
            else:
                print("Invalid move! Try again.")
                continue
        else:
            print("Computer's turn ({})".format(computer_symbol))
            row, col = find_best_move(board)
            board[row][col] = computer_symbol
            current_player = player_symbol

    print_board(board)
    if check_winner(board, player_symbol):
        print(f"Congratulations {player_name}! You win!")
    elif check_winner(board, computer_symbol):
        print("Computer wins!")
    else:
        print("It's a draw!")


play_game()
