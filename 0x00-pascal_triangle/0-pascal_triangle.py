# usr/bin/python3
"""This module contains functions to generate Paschal's triangle"""


def pascal_triangle(n):
    """Returns a Paschal's triangle of depth n.

    Returns: list[list[int]]
    """
    triangle = []

    if n <= 0:
        return triangle

    triangle.append([1])
    triangle.append(generate_row(triangle, row) for row in range(1, n))

    return triangle


def generate_row(triangle, n):
    """Returns the nth(zero-indexed) row of Paschal's triangle

    Return: list[int]
    """
    row = [generate_number(triangle[n - 1], n, i) for i in range(0, n + 1)]
    return row


def generate_number(prev_row, row, elem_idx):
    """Generates the number `elem_idx` in `row`. These are 0-indexed.

    See https://www.cuemath.com/algebra/pascals-triangle/

    Returns: int
    """

    # check if first or last element:
    if elem_idx in {0, row}:
        return 1

    return prev_row[elem_idx - 1] + prev_row[elem_idx]
