import tkinter as tk
import random

# Constants for players and empty spots
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Initialize the game board
board = [[EMPTY for _ in range(3)] for _ in range(3)]

# Function to check if the game is over
def is_game_over(board):
    return check_winner(board, PLAYER_X) or check_winner(board, PLAYER_O) or not any(EMPTY in row for row in board)

# Check if a player has won
def check_winner(board, player):
    for row in range(3):
        if all([board[row][col] == player for col in range(3)]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Get available moves
def get_available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == EMPTY]

# Minimax algorithm to evaluate the best move
def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_O):
        return 1
    elif check_winner(board, PLAYER_X):
        return -1
    elif not any(EMPTY in row for row in board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for (row, col) in get_available_moves(board):
            board[row][col] = PLAYER_O
            eval = minimax(board, depth + 1, False)
            board[row][col] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for (row, col) in get_available_moves(board):
            board[row][col] = PLAYER_X
            eval = minimax(board, depth + 1, True)
            board[row][col] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the AI using Minimax
def find_best_move(board):
    best_move = None
    best_value = float('-inf')

    for (row, col) in get_available_moves(board):
        board[row][col] = PLAYER_O
        move_value = minimax(board, 0, False)
        board[row][col] = EMPTY
        if move_value > best_value:
            best_value = move_value
            best_move = (row, col)
    
    return best_move

# Update the board and UI
def update_board(row, col, player):
    if board[row][col] == EMPTY:
        board[row][col] = player
        buttons[row][col].config(text=player, state="disabled")
        if is_game_over(board):
            if check_winner(board, PLAYER_X):
                result_label.config(text="You win!")
            elif check_winner(board, PLAYER_O):
                result_label.config(text="AI wins!")
            else:
                result_label.config(text="It's a draw!")
            disable_buttons()
        return True
    return False

# Disable all buttons after the game is over
def disable_buttons():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(state="disabled")

# Handle human move and AI move
def human_move(row, col):
    if update_board(row, col, PLAYER_X):
        if not is_game_over(board):
            ai_move()

def ai_move():
    row, col = find_best_move(board)
    update_board(row, col, PLAYER_O)

# Create the GUI
def create_game_window():
    window = tk.Tk()
    window.title("Tic-Tac-Toe")

    global buttons, result_label
    buttons = [[None for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(window, text=EMPTY, font=('normal', 40), width=5, height=2, 
                                          command=lambda r=row, c=col: human_move(r, c))
            buttons[row][col].grid(row=row, column=col)

    result_label = tk.Label(window, text="", font=('normal', 20))
    result_label.grid(row=3, column=0, columnspan=3)

    window.mainloop()

# Start the game
if __name__ == "__main__":
    create_game_window()
