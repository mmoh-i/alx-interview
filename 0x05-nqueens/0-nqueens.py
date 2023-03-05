#!/usr/bin/env python3
import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at (row, col) on the board.
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # If all checks pass, then it's safe to place a queen at (row, col)
    return True

def solve(board, col):
    """
    Solve the N queens puzzle recursively using backtracking.
    """
    # Base case: all queens have been placed
    if col >= len(board):
        print_board(board)
        return True

    # Try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen on the board
            board[i][col] = 1

            # Recur to place rest of the queens
            solve(board, col + 1)

            # Backtrack: remove the queen from the board
            board[i][col] = 0

    # If the queen can't be placed in any row in this column, return False
    return False

def print_board(board):
    """
    Print the board.
    """
    for row in board:
        print("".join(str(cell) for cell in row))

def main():
    """
    Parse the command line arguments and solve the N queens puzzle.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solve(board, 0)

if __name__ == "__main__":
    main()
