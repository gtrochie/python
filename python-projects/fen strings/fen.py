fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
def chess(fen):
    """separate FEN string into its components."""

    fields = fen.split(" ")
    board, to_move, castling_rights, en_passant, halfmove, fullmove = fields

    # print("Board:", board)
    # print("Active color:", to_move)
    # print("Castling:", castling_rights)
    # print("En passant:", en_passant)
    # print("Halfmove clock:", halfmove)
    # print("Fullmove number:", fullmove)
    
    """we now have to convert the board part into a 2D list"""
    rows = board.split("/")
    # print(rows)
    board_matrix = []
    for row in rows:
        board_row = []
        for char in row:
            if char.isdigit():
                board_row.extend(["."] * int(char)) # char is 8
            else:
                board_row.append(char)
        board_matrix.append(board_row)
         # append the row to the board matrix

    board_matrix = [" ".join(row) for row in board_matrix] 
    # removes inner lists
    final_board = "\n".join(board_matrix)
    #removes outer list
    white_castle = castling_rights[0:2]
    black_castle = castling_rights[2:]
    # print(f"to_move: {to_move}")
    # print(f"white_castle: {white_castle}")
    # print(f"black_castle: {black_castle}")
    # print(f"en_passant: {en_passant}")  
    # print(f"halfmove: {halfmove}")
    # print(f"fullmove: {fullmove}")  
    return final_board
#done
print(chess(fen))