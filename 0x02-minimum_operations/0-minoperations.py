#!/usr/bin/env python3
""""""


def minOperations(n: int) -> int:
    """"""
    buf, rem, filled, ops = 0, n, 1, 0

    while rem:
        if rem % filled:
            buf = buf or 1
            filled += buf
            ops += 1
        else:
            buf = filled
            ops += 1
            filled += buf
            ops += 1
        rem = n - filled
    return ops
