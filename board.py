def get_empty_board():
    empty_board = [['.', '.', '.'],
                   ['.', '.', '.'],
                   ['.', '.', '.']]
    return empty_board

def display_board(board):
    print("    1   2   3")
    print("A"," ", board[0][0], "|", board[0][1], "|", board[0][2])
    print("  ","---+---+---")
    print("B"," ", board[1][0], "|", board[1][1], "|", board[1][2])
    print("  ","---+---+---")
    print("C"," ", board[2][0], "|", board[2][1], "|", board[2][2])
    print("  ","---+---+---")

def is_board_full(board):
    for dots in board:
        for dot in dots:
            if dot==".":
                return False
    return True

def get_winning_player(board):
    for sign in range(0,3):
        if board[sign][0] == board[sign][1] == board[sign][2] !=".":
            return board[sign][0]
    for sign in range(0,3):
        if board[0][sign] == board[1][sign] == board[2][sign] !=".":
            return board[0][sign]
    
    if board[0][0] == board[1][1] == board[2][2] !=".":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] !=".":
        return board[0][2]
    
    return None