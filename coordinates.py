def get_human_coordinates(board, current_player):
    
    while True:
        coord = input("wprowadź współrzędne dla gracza w postaci A1, B3 itd.: ")
        coord = coord.upper()
        if len(coord) == 2:
          if coord[0] == "A":
              X = 0
          elif coord[0] == "B":
              X = 1
          elif coord[0] == "C":
              X = 2
          else:
              print("błędnie podane współrzędne")
              continue

          if coord[1] == "1":
              Y = 0
          elif coord[1] == "2":
              Y = 1
          elif coord[1] == "3":
              Y = 2
          else:
             print("błędnie podane współrzędne")
             continue

          if board[X][Y] == ".":
              #  return coord_list[coord]
            return X, Y
          else:
              print("to pole jest już zajęte")
        else:
          print("błędnie podane współrzędne")