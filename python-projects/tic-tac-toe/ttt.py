def find_winner(board):
    # 1. Validation Logic
    if len(board) != 3:
        raise ValueError("Board must be 3x3")
    
    for row in board:
        if len(row) != 3:
            raise ValueError("Each row must have 3 columns")
        for char in row:
            # Added a check for space " " in case the board isn't full
            if char not in ["X", "O", " "]:
                raise ValueError("Only 'X', 'O', or ' ' are permitted")

    #  Check Rows and Columns using a loop (Cleaner than manual indexing)
    for i in range(3):
        # Check Row i: board[i][0], board[i][1], board[i][2]
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        
        # Check Column i: board[0][i], board[1][i], board[2][i]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    # Check Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    #  No winner found
    return None

board = [
    ['X', 'X', 'X'],
    ['O', 'O', 'X'],
    ['O', 'X', 'O']
]

print(f"The winner is: {find_winner(board)}")