"""
Tic Tac Toe Player
"""

import math
import copy

X, O, EMPTY = "X", "O", None

def initial_state():
    
    return [[EMPTY] * 3 for _ in range(3)]

def player(board):
    
    return X if sum(row.count(X) for row in board) <= sum(row.count(O) for row in board) else O

def actions(board):

    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):

    if action not in actions(board):
        raise ValueError("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):

    for mark in (X, O):
        if any(all(board[i][j] == mark for j in range(3)) for i in range(3)) or \
           any(all(board[j][i] == mark for j in range(3)) for i in range(3)) or \
           all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
            return mark
    return None

def terminal(board):

    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

def utility(board):

    return {X: 1, O: -1}.get(winner(board), 0)

def minimax(board):

    if terminal(board):
        return None
    current_player = player(board)
    best_action = max(actions(board), key=lambda a: min_value(result(board, a))) if current_player == X else \
                  min(actions(board), key=lambda a: max_value(result(board, a)))
    return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    return max(min_value(result(board, a)) for a in actions(board))

def min_value(board):
    if terminal(board):
        return utility(board)
    return min(max_value(result(board, a)) for a in actions(board))