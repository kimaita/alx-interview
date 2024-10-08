#!/usr/bin/python3
"""Method for calculating island perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of an island represented by a matrix `grid`

    Args:
        grid - list of list of ints
    """
    perimeter = 0
    m = len(grid)
    n = len(grid[0])
    for row_idx, row in enumerate(grid):
        for col_idx, elem in enumerate(row):
            if elem:
                perimeter += 4

                # shared bottom/top border
                if row_idx < m - 1 and grid[row_idx + 1][col_idx]:
                    perimeter -= 2
                # shared left/right border
                if col_idx < n - 1 and grid[row_idx][col_idx + 1]:
                    perimeter -= 2

    return perimeter
