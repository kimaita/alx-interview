#!/usr/bin/python3
"""Solves a lockboxes problem: determine if all boxes can be opened"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    a method that determines if all the boxes can be opened.
    """
    found_keys = set(boxes[0])
    skipped = set()
    for box, keys in enumerate(boxes[1:], start=1):
        if box in found_keys:
            found_keys.update(keys)
        else:
            skipped.add(box)

    for box in found_keys.intersection(skipped):
        found_keys.update(boxes[box])

    if skipped.difference(found_keys):
        return False

    return True
