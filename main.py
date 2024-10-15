#Luke Brudnok
from tic_tac_toe import TicTacToe
from random import choice
from random import randint

def start_game():
  game = TicTacToe()
  print("Tic Tac Toe")
  print("Type the row number, a space, followed by the column you would like to place the token\n  ex:'0 0' would the top left corner")
  return game

def player_turn(game):
  position = input("Enter position: ")
  position = position.split(" ")
  game.place_token(position)

def cpu_turn(game):
  position = randint(0, 2), randint(0, 2)
  game.place_token(position)

def check_game_state(game):
  return game.is_winner()

def main():
  game = start_game()
  state = False
  tie = False
  while state == False and tie == False:
    print(game)
    if game.check_turn() == "X":
      player_turn(game)
    elif game.check_turn() == "O":
      cpu_turn(game)
    state, tie, chip = check_game_state(game)

  print()
  print(game)
  if state:
    print(f"\n {chip} won!")
  elif tie:
    print("It's a tie!")


if __name__ == "__main__":
  main()


