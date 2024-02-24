#!/usr/bin/python3
"""
Module contains 'solve_nqueens' function, which solves the N queens problem.
Function prints every possible solution to the problem.
"""


import sys


def solve_nqueens(n: int) -> list:
    """
    Solve the N queens problem.

    Args:
        n (int): The number of queens.

    Raises:
        SystemExit: If n is less than 4.

    Function iterates through each position in chessboard.
    If queen can be placed at position, it places the queen at position.
    Otherwise, it moves to next position.
    """

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def can_place(pos: int, ocuppied_positions: list) -> bool:
        for i in range(len(ocuppied_positions)):
            if pos == ocuppied_positions[i] or \
                pos - i == ocuppied_positions[i] - len(ocuppied_positions) or \
                    pos + i == ocuppied_positions[i] + len(ocuppied_positions):
                return False
        return True

    def place_queen(ocuppied_positions: list, target_row: int, n: int) -> None:
        if target_row == n:
            result.append(ocuppied_positions)
            return

        for column in range(n):
            if can_place(column, ocuppied_positions):
                place_queen(ocuppied_positions + [column], target_row + 1, n)

    result = []
    place_queen([], 0, n)
    return result


def print_result(result: list) -> None:
    """
    Print the result.

    Args:
        result (list): The result to print.

    Function iterates through each solution in the result.
    It prints each solution on a new line.
    """

    for res in result:
        print([[i, res[i]] for i in range(len(res))])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

print_result(solve_nqueens(n))
