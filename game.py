from board import Board
import time
import random
from Minimax import *
import numpy as np
# GAME LINK
# http://kevinshannon.com/connect4/


def main():
    board = Board()
    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        # Game=np.zeros((6,7))
        # convert(Game,game_board)
        # print(Game)

        # YOUR CODE GOES HERE
        bestColumn = chooseC(1,5,game_board,1,2)
        board.print_grid (game_board)
        print("answer: ", bestColumn)
        board.select_column(bestColumn)

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        # random_column = random.randint(0, 6)
        # board.select_column(random_column)

        time.sleep(2)


if __name__ == "__main__":
    main()
