import math

# This is the board for Tic-Tac-Toe (3x3)
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check secondary diagonal
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return all([cell != '' for row in board for cell in row])

# Alpha-Beta pruning algorithm implementation
def minimax(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, 'X'):  # Maximizing player
        return 1
    if check_winner(board, 'O'):  # Minimizing player
        return -1
    if is_full(board):  # Draw
        return 0

    if is_maximizing:  # Maximizing player 'X'
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ''
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break  # Beta cut-off
        return best_score
    else:  # Minimizing player 'O'
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ''
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return best_score

# Function to make the best move for 'X'
def best_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'X'
                score = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Example of making a move
def make_move(i, j, player):
    if board[i][j] == '':
        board[i][j] = player

# Example game loop
if __name__ == "__main__":
    make_move(0, 0, 'O')  # Opponent's move
    move = best_move()    # AI's best move
    if move:
        make_move(move[0], move[1], 'X')
    
    for row in board:
        print(row)
