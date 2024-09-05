# Tic-Tac-Toe Game
def print_board(board):
    """Function to print the Tic-Tac-Toe board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Function to check if the current player has won."""
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([spot == player for spot in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:  # Check main diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:  # Check anti-diagonal
        return True
    return False

def is_board_full(board):
    """Check if the board is full (draw)."""
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    """Main function to control the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 grid
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get user input
        row, col = map(int, input("Enter row and column (0-2, space separated): ").split())
        
        # Check if the input is valid
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        
        # Place the player's mark on the board
        board[row][col] = current_player
        
        # Check if the current player wins
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (draw)
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
