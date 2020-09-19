import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

board = [[O, X, X],
        [X, O, X],
        [X, EMPTY, X]]

actions = ttt.winner(board)

print (actions)