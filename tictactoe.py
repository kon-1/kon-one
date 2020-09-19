"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.

     count X
     count O

     If x = o
        X
    else
        o
    """

    count_X=0
    count_O=0

    for row in board:
        for column in row:
            if column == "X":
                count_X += 1
            elif column == "O":
                count_O += 1
    
    if count_X == count_O or count_X < count_O:
        return "X"
    else:
        return "O"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.

    locate empty fields and return them as tuples
    """
    actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                actions.add(tuple((i, j)))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    deepcopy of the board
    
    if action is not in actions:
        return exception
    else:
        do the action
        return the board
    """

    if action not in actions(board):
        raise Exception("Bloody No!")

    board_copy = deepcopy(board)

    if player(board) == "X":
        board_copy[action[0]][action[1]] = X
        return board_copy
    else:
        board_copy[action[0]][action[1]] = O
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_won = 0
    o_won = 0
    diagonal = len(board) - 1 

    #check diagonal from upper-left to lower-right
    for i in range(len(board)):
        if board[i][i] == X:
            x_won += 1
        elif board[i][i] == O:
            o_won += 1   
    if x_won == 3:
        return X
    elif o_won == 3:
        return O
    x_won = o_won = 0
    
    #check diagonal from upper-right to lower-left
    for i in range(len(board)):
        if board[i][diagonal] == X:
            x_won += 1
        elif board[i][diagonal] == O:
            o_won += 1
        
        diagonal -= 1
    if x_won == 3:
        return X
    elif o_won == 3:
        return O
    x_won = o_won = 0

    #check rows
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == O:
                o_won += 1
            elif board[i][j] == X:
                x_won += 1
        if x_won == 3:
            return X
        elif o_won == 3:
            return O
        x_won = o_won = 0

    #check columns
    for k in range(len(board)):
        for i in range(len(board)):
            if board[i][k] == X:
                x_won += 1
            elif board[i][k] == O:
                o_won += 1      
        if x_won == 3:
            return X
        elif o_won == 3:
            return O
        x_won = o_won = 0
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    if all spaces are filled or winner(board) is not None:
        return True
    """

    if not(None in [j for i in board for j in i]) or winner(board) is not None:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    MAX picks action in Actions that has the highest value in MIN-VALUE(Results(board, action))
    MIN picks action in Actions that has the smallest value in MAX-VALUE(Results(board, action))
    """
    if terminal(board):
        return None

    # if player(board) == X:
    #     v = -math.inf
    #     best_action = None

    #     for action in actions(board):
    #         v_curr = MIN_VALUE(result(board, action))
    #         if v_curr > v:
    #             v = v_curr
    #             best_action = action
    #     return best_action
    # else:
    #     v = math.inf
    #     best_action = None

    #     for action in actions(board):
    #         v_curr = MAX_VALUE(result(board, action))
    #         if v_curr < v:
    #             v = v_curr
    #             best_action = action
    #     return best_action

    if player(board) == X:
        return MAX_VALUE(board)[1]
    else:
        return MIN_VALUE(board)[1]

def MAX_VALUE(board):
    best_action = None
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        next_value = max(v, MIN_VALUE(result(board, action))[0])
        if next_value > v:
            v = next_value
            best_action = action
    return [v, action]

def MIN_VALUE(board):
    best_action = None
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        next_value = min(v, MAX_VALUE(result(board, action))[0])
        if next_value < v:
            v = next_value
            best_action = action
    return [v, action]
