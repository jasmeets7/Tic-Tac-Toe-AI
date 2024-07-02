"""
Tic Tac Toe Player
"""

from math import inf as INFINITY
from functools import reduce
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
    """
    x = reduce(lambda acc, x: acc + x, [reduce(lambda acc, x: acc + 1 if x == X else acc, turns, 0) for turns in board], 0)
    o = reduce(lambda acc, y: acc + y, [reduce(lambda acc, y: acc + 1 if y == O else acc, turns, 0) for turns in board], 0)

    return O if x > o else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilities = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possibilities.add((row, col))
    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    av_ac = actions(board)
    if action not in av_ac:
        print("line 51", action, av_ac)
        raise Exception("Invalid move!")
    row, col = action
    _board = deepcopy(board)
    _board[row][col] = player(board=board)
    return _board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_winner(board, X):
        return X
    elif check_winner(board, O):
        return O
    else:
        return None

def check_winner(board, payer):
    checks = board + get_columns(board) + get_diagnols(board)
    for row in checks:
        if all(column == payer for column in row):
            return True
    return False

def get_diagnols(board):
    main_diagonal = [board[i][i] for i in range(len(board))]
    anti_diagonal = [board[i][len(board) - 1 - i] for i in range(len(board))]
    return [main_diagonal, anti_diagonal]

def get_columns(board):
    return [[board[row][col] for row in range(len(board))] for col in range(len(board[0]))]

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in [X, O]:
        return True
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    return True


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
    """
    if terminal(board):
        return None
    
    current_player = player(board)

    if current_player == X:
        value, best_action = -INFINITY, None
        for action in actions(board):
            new_value = min_value(result(board, action))
            if new_value > value:
                value, best_action = new_value, action
    else:
        value, best_action = INFINITY, None
        for action in actions(board):
            new_value = max_value(result(board, action))
            if new_value < value:
                value, best_action = new_value, action          
    return best_action


def max_value(board):
    value = -INFINITY
    if terminal(board):
        return utility(board)
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    value = INFINITY
    if terminal(board):
        return utility(board)
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
