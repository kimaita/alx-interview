# N Queens

The N queens puzzle is the challenge of placing N non-attacking queens on an `N×N` chessboard.

[0-nqueens](./0-nqueens.py) solves the N queens problem:

Usage: `nqueens N`

- If called with the wrong number of arguments, prints `Usage: nqueens N`, followed by a new line, and exits with the status 1
- `N` must be an integer greater or equal to 4.
  - If `N` is not an integer, prints `N must be a number`, followed by a new line, and exits with the status 1
  - If `N` is smaller than 4, prints `N must be at least 4`, followed by a new line, and exits with the status 1

The program should print every possible solution to the problem, one solution per line in no specific order

## Examples

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```
