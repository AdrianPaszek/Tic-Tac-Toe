from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates


def main():
    board = get_empty_board()
    is_game_running = True
    current_player = 'O'
    while is_game_running:
        display_board(board)
        
        ### TO DO ###
        # in each new iteration of the while loop the program should 
        # alternate the value of `current_player` from `X` to `O`
        match current_player:
             case "X":
                 current_player = "O"
             case "O":
                current_player = "X"
      # current_player = 'X'
        
        ### TO DO ###
        # based on the value of the variables `game_mode` and `current_player` 
        # the programm should should choose betwen the functions
        # get_random_ai_coordinates or get_umbeatable_ai_coordinates or get_human_coordinates
        x, y = get_human_coordinates(board, current_player)
        
        board[x][y] = current_player
        
        ### TO DO ###
        # based on the values of `winning_player` and `its_a_tie` the program
        # should either stop displaying a winning/tie message 
        # OR continue the while loop
        winning_player = get_winning_player(board)
        if winning_player:
          is_game_running = False
          print("Wygral gracz", winning_player)
          continue # continue zeby nie wykonac instrukcji nizej
        its_a_tie = is_board_full(board)
        if its_a_tie:
          print("Remis")
          is_game_running = False
    # Dodatkowy display_board zeby wypisac stan planszy na koniec.
    display_board(board)


if __name__ == "__main__":
    main()