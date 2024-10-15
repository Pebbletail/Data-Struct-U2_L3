#Luke Brudnok
from random import choice

class TicTacToe:
  def __init__(self):
    self.__board = [['*']*3 for n in range(3)]
    self.__turn = choice(["X", "O"])

  def check_turn(self):
    return self.__turn
    
  def __check_win(self):
    win = False
    tie = False
    winToken = None

    #check for row win
    for row in range(3):
      if self.__board[row][0] != '*':
        if (self.__board[row][0] == self.__board[row][1] == self.__board[row][2]):
          win = True
          winToken = self.__board[row][0]
          break

    #check column win
    for column in range(3):
      if self.__board[0][column] != '*':
        if (self.__board[0][column] == self.__board[1][column] == self.__board[2][column]):
          win = True
          winToken = self.__board[0][column]
          break


    #check diagonal win
    if self.__board[1][1] == "X" or self.__board[1][1] == "O":
      temp = self.__board[1][1]

      if self.__board[0][0] == temp and self.__board[2][2] == temp:
        win = True
        winToken = temp
      elif self.__board[0][2] == temp and self.__board[2][0] == temp:
        win = True
        winToken = temp

    #check for tie
    if win == False:
      for row in self.__board:
        for el in row:
          if el == '*':
            tie = False
            break
          else:
            tie = True
    
    return win, tie, winToken

  def place_token(self, position):
    x = 0
    y = 0
    
    try:
      x = int(position[1])
      y = int(position[0])
      validXpos = (0 <= x and x <= 2)
      validYpos = (0 <= y and y <= 2)

      if validXpos and validYpos:
        if self.__board[y][x] == "*":
          self.__board[y][x] = self.__turn

          if self.__turn == "X":
            self.__turn = "O"
          else:
            self.__turn = "X"

        elif self.__turn == "X":
          print("invalid location")


    except:
      print("invalid location")


  def is_winner(self):
    win, tie, winToken = self.__check_win()
    
    return win, tie, winToken

  def __str__(self):
    string = ""
    for row in self.__board:
      string += (str(row) + "\n")
    return string