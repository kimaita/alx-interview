#!/usr/bin/python3
"""Methods for calculating island perimeter"""


def count_cell(grid, row_idx, col_idx):
    """Returns the perimeter of a single cell."""
    sides = 0
    try:
        sides += grid[row_idx - 1][col_idx] ^ 1
        sides += grid[row_idx + 1][col_idx] ^ 1
        sides += grid[row_idx][col_idx + 1] ^ 1
        sides += grid[row_idx][col_idx - 1] ^ 1
    except IndexError:
        if row_idx == 0:
            sides += 1
        if row_idx == len(grid) - 1:
            sides += 1

        if col_idx == 0:
            sides += 1
        if col_idx == len(grid[row_idx]):
            sides += 1

    return sides


def island_perimeter(grid):
    """Returns the perimeter of an island represented by a matrix `grid`

    Args:
        grid - list of list of ints
    """
    perimeter = 0
    for row_idx, row in enumerate(grid):
        for col_idx, elem in enumerate(row):
            if elem:
                perimeter += count_cell(grid, row_idx, col_idx)

    return perimeter
