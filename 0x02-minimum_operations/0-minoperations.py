#!/usr/bin/env python3
"""Contans a method for finding the minimum operations needed to achieve
a result.
"""


def minOperations(n: int) -> int:
    """Returns the minimum number of oprations needed to achieve n
    H characters starting with a single H.

    Available operations are `Copy All` and `Paste`

    Args:
        n(int) - number of H characters desired

    Returns:
        int - min number of operations to achieve n H's.
    """
    buf, filled, ops = 0, 1, 0
    rem = n - filled

    while rem:
        if rem % filled:
            buf = buf or 1
            # paste
            filled += buf
            ops += 1
        else:
            # copy all
            buf = filled
            # paste
            filled += buf
            ops += 2
        rem = n - filled
    return ops
