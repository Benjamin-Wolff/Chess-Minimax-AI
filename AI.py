import random
from math import inf
from piece import *


def random_move(board):
    """
    Selects a random move from the valid moves for the current players turn
    :param board: the current board being used for the game (Board)
    :return: tuple representing move; format: ((sourceX, sourceY), (destX, destY))
    """
    moves = board.get_moves()
    if moves:
        return random.choice(moves)


def evaluate(board):
    """
    Provides a number representing the value of the board at a given state
    :param board: the current board being used for the game (Board)
    :return: integer representing boards value
    """

    return board.whiteScore - board.blackScore


def expectimax(board, depth, maximizing_color):
    """
    Expectimax algorithm used to find a move for the AI, assuming the player makes a random move
    :param board: the current board being used for the game (Board)
    :param depth: controls how deep to search the tree of possible moves (int)
    :param maximizing_color: color of the AI using this function to determine a move (tuple)
    :return: tuple representing move and eval; format: (move, eval)
    """

    # boolean to represent if white is the AI player
    white_player = maximizing_color == WHITE

    best_move, best_eval = max_expect_value(board, depth)

    return best_move, best_eval


def max_expect_value(board, depth):
    # if the depth is 0 or the game is over, simply return the current board evaluation
    if depth == 0 or board.gameover:
        return None, evaluate(board)

    best_eval = -inf
    possible_moves = board.get_moves()
    # shuffles the moves so the same move does not happen every time (of the best options)
    random.shuffle(possible_moves)
    best_move = possible_moves[0]

    # iterates through the possible moves to find the best move for white
    for move in possible_moves:
        # makes the move and finds the value from min_value
        board.make_move(move[0], move[1])
        current_eval = expect_value(board, depth - 1)[1]
        board.unmake_move()

        # updates the best move and evaluation if necessary
        if current_eval > best_eval:
            best_eval = current_eval
            best_move = move


    # returns the best move and its evaluation
    return best_move, best_eval

def expect_value(board, depth):
    # if the depth is 0 or the game is over, simply return the current board evaluation
    if depth == 0 or board.gameover:
        return None, evaluate(board)




def minimax(board, depth, maximizing_color):
    """
    Minimax algorithm used to find best move for the AI
    :param board: the current board being used for the game (Board)
    :param depth: controls how deep to search the tree of possible moves (int)
    :param maximizing_color: color of the AI using this function to determine a move (tuple)
    :return: tuple representing move and eval; format: (move, eval)
    """

    # boolean to represent if white is the AI player
    white_player = maximizing_color == WHITE

    if white_player:
        best_move, best_eval = max_value(board, depth, -inf, inf)
    else:
        best_move, best_eval = min_value(board, depth, -inf, inf)

    return best_move, best_eval


def max_value(board, depth, alpha, beta):
    """
    Max value function of minimax used to find the best move for white
    :param board: the current board being used for the game (Board)
    :param depth: controls how deep to search the tree of possible moves (int)
    :param alpha: the alpha value used to compare for alpha-beta pruning
    :param beta: the beta value used to compare for alpha-beta pruning
    :return: tuple representing move and eval; format: (move, eval)
    """

    # if the depth is 0 or the game is over, simply return the current board evaluation
    if depth == 0 or board.gameover:
        return None, evaluate(board)

    best_eval = -inf
    possible_moves = board.get_moves()
    # shuffles the moves so the same move does not happen every time (of the best options)
    random.shuffle(possible_moves)
    best_move = possible_moves[0]

    # iterates through the possible moves to find the best move for white
    for move in possible_moves:
        # makes the move and finds the value from min_value
        board.make_move(move[0], move[1])
        current_eval = min_value(board, depth - 1, alpha, beta)[1]
        board.unmake_move()

        # updates the best move and evaluation if necessary
        if current_eval > best_eval:
            best_eval = current_eval
            best_move = move

        # compares to beta value to prune if necessary
        if best_eval >= beta:
            return best_move, best_eval

        # updates alpha for future use
        alpha = max(alpha, best_eval)

    # returns the best move and its evaluation
    return best_move, best_eval


def min_value(board, depth, alpha, beta):
    """
    Min value function of minimax used to find the best move for black
    :param board: the current board being used for the game (Board)
    :param depth: controls how deep to search the tree of possible moves (int)
    :param alpha: the alpha value used to compare for alpha-beta pruning
    :param beta: the beta value used to compare for alpha-beta pruning
    :return: tuple representing move and eval; format: (move, eval)
    """

    # if the depth is 0 or the game is over, simply return the current board evaluation
    if depth == 0 or board.gameover:
        return None, evaluate(board)

    best_eval = inf
    possible_moves = board.get_moves()
    # shuffles the moves so the same move does not happen every time (of the best options)
    random.shuffle(possible_moves)
    best_move = possible_moves[0]

    # iterates through the possible moves to find the best move for black
    for move in possible_moves:
        # makes the move and finds the value from max_value
        board.make_move(move[0], move[1])
        current_eval = max_value(board, depth - 1, alpha, beta)[1]
        board.unmake_move()

        # updates the best move and evaluation if necessary
        if current_eval < best_eval:
            best_eval = current_eval
            best_move = move

        # compares to alpha value to prune if necessary
        if best_eval <= alpha:
            return best_move, best_eval

        # updates beta for future use
        beta = min(beta, best_eval)

    # returns the best move and its evaluation
    return best_move, best_eval
